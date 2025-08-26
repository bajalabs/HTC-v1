#!/usr/bin/env python3
"""
JSON Files Organization Script
Finds and organizes all JSON HTS files by chapter.
"""

import os
import csv
import json
import shutil
from pathlib import Path
from collections import defaultdict
import re

# Chapter names mapping
CHAPTER_NAMES = {
    1: "live-animals", 2: "meat-and-edible-meat-offal", 3: "fish-and-crustaceans",
    4: "dairy-produce-birds-eggs", 5: "products-of-animal-origin", 
    7: "edible-vegetables-and-roots", 8: "edible-fruit-and-nuts",
    9: "coffee-tea-mate-spices", 10: "cereals", 11: "milling-industry-products",
    12: "oil-seeds-oleaginous-fruits", 13: "lac-gums-resins-vegetable-extracts",
    14: "vegetable-plaiting-materials", 15: "animal-vegetable-fats-oils",
    16: "meat-fish-preparations", 17: "sugars-sugar-confectionery",
    18: "cocoa-cocoa-preparations", 19: "cereal-flour-starch-preparations",
    20: "vegetable-fruit-preparations", 21: "miscellaneous-edible-preparations",
    22: "beverages-spirits-vinegar", 23: "food-industry-residues-animal-feed",
    24: "tobacco-manufactured-tobacco", 25: "salt-sulfur-earths-stone",
    26: "ores-slag-ash", 27: "mineral-fuels-oils", 28: "inorganic-chemicals",
    29: "organic-chemicals", 30: "pharmaceutical-products", 31: "fertilizers",
    32: "tanning-dyeing-extracts", 33: "essential-oils-perfumery",
    34: "soap-organic-surface-agents", 35: "albuminoidal-substances",
    36: "explosives-pyrotechnics", 37: "photographic-cinematographic-goods",
    38: "miscellaneous-chemical-products", 39: "plastics-articles-thereof",
    40: "rubber-articles-thereof", 41: "raw-hides-skins-leather",
    42: "leather-articles-saddlery", 43: "furskins-artificial-fur",
    44: "wood-articles-wood-charcoal", 45: "cork-articles-cork",
    46: "straw-plaiting-materials", 47: "wood-pulp-fibrous-material",
    48: "paper-paperboard-articles", 49: "printed-books-newspapers",
    50: "silk", 51: "wool-animal-hair", 52: "cotton",
    53: "vegetable-textile-fibers", 54: "man-made-filaments",
    55: "man-made-staple-fibers", 56: "wadding-felt-nonwovens",
    57: "carpets-textile-floor-coverings", 58: "special-woven-fabrics",
    59: "impregnated-coated-textile-fabrics", 60: "knitted-crocheted-fabrics",
    61: "knitted-crocheted-apparel", 62: "not-knitted-crocheted-apparel",
    63: "textile-articles-worn-clothing", 64: "footwear-gaiters",
    65: "headgear-parts-thereof", 66: "umbrellas-walking-sticks",
    67: "prepared-feathers-artificial-flowers", 68: "stone-plaster-cement-articles",
    69: "ceramic-products", 70: "glass-glassware",
    71: "pearls-precious-stones-metals", 72: "iron-steel",
    73: "iron-steel-articles", 74: "copper-articles-thereof",
    75: "nickel-articles-thereof", 76: "aluminum-articles-thereof",
    78: "lead-articles-thereof", 79: "zinc-articles-thereof",
    80: "tin-articles-thereof", 81: "base-metals-cermets",
    82: "tools-implements-cutlery", 83: "miscellaneous-base-metal-articles",
    84: "nuclear-reactors-boilers-machinery", 85: "electrical-machinery-equipment",
    86: "railway-locomotives-rolling-stock", 87: "vehicles-parts-accessories",
    88: "aircraft-spacecraft-parts", 89: "ships-boats-floating-structures",
    90: "optical-photographic-instruments", 91: "clocks-watches-parts",
    92: "musical-instruments-parts", 93: "arms-ammunition-parts",
    94: "furniture-bedding-lamps", 95: "toys-games-sports",
    96: "miscellaneous-manufactured-articles", 97: "works-of-art-collectors-pieces",
    98: "special-classification-provisions", 99: "temporary-legislation-modifications"
}

def find_json_files(playwright_dir):
    """Find all JSON files in timestamp directories."""
    base_path = Path(playwright_dir)
    timestamp_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}\.\d{3}Z$')
    
    json_files = []
    
    for item in base_path.iterdir():
        if item.is_dir() and timestamp_pattern.match(item.name):
            json_file = item / "htsdata.json"
            if json_file.exists():
                json_files.append({
                    'timestamp_dir': item.name,
                    'json_file': json_file,
                    'csv_file': item / "htsdata.csv"  # For chapter identification
                })
    
    return json_files

def identify_chapter_from_json(json_file):
    """Try to identify chapter directly from JSON file."""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Handle different JSON structures
            if isinstance(data, list) and len(data) > 0:
                # Get first data item (skip header if exists)
                first_data = data[0]
                
                # Check different possible field names for HTS number
                hts_number = None
                if isinstance(first_data, dict):
                    # Try different possible field names
                    for field_name in ['htsno', 'HTS Number', 'HTS_Number', 'hts_number', 'HTS', 'hts']:
                        if field_name in first_data:
                            hts_number = str(first_data[field_name]).strip('"').strip()
                            break
                # Check if it's a list where first element is HTS number
                elif isinstance(first_data, list) and len(first_data) > 0:
                    hts_number = str(first_data[0]).strip('"').strip()
                
                # Extract chapter number
                if hts_number and len(hts_number) >= 2:
                    # Handle cases where HTS number might be just "92" or "9201"
                    if hts_number.isdigit():
                        chapter_num = int(hts_number[:2])
                        if 1 <= chapter_num <= 99:
                            return chapter_num
                        
    except Exception as e:
        print(f"Error reading JSON {json_file}: {e}")
    
    return None

def identify_chapter_from_csv(csv_file):
    """Identify chapter from corresponding CSV file (fallback method)."""
    if not csv_file.exists():
        return None
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            first_row = next(reader)
            hts_number = first_row[0].strip('"').strip()
            
            if len(hts_number) >= 2:
                chapter_num = int(hts_number[:2])
                if 1 <= chapter_num <= 99:
                    return chapter_num
                    
    except Exception as e:
        print(f"Error reading CSV {csv_file}: {e}")
    
    return None

def organize_json_files(playwright_dir, chapters_dir):
    """Organize JSON files by chapter."""
    print("🔍 Finding JSON files...")
    json_files = find_json_files(playwright_dir)
    print(f"Found {len(json_files)} JSON files")
    
    # Group files by chapter
    chapter_files = {}
    unidentified_files = []
    
    print("📊 Analyzing files to identify chapters...")
    for file_info in json_files:
        # Try to identify from JSON first, then fall back to CSV
        chapter_num = identify_chapter_from_json(file_info['json_file'])
        if not chapter_num:
            chapter_num = identify_chapter_from_csv(file_info['csv_file'])
        
        if chapter_num:
            chapter_name = CHAPTER_NAMES.get(chapter_num, f"chapter-{chapter_num}")
            print(f"  Chapter {chapter_num}: {chapter_name} ({file_info['timestamp_dir']})")
            
            # Only keep one JSON file per chapter (first one found)
            if chapter_num not in chapter_files:
                chapter_files[chapter_num] = file_info
            else:
                print(f"    (Duplicate found, keeping first one)")
        else:
            print(f"  Could not identify chapter for {file_info['timestamp_dir']}")
            unidentified_files.append(file_info)
    
    # Copy JSON files to chapter directories
    print("📁 Copying JSON files to chapter directories...")
    successful_copies = 0
    failed_copies = []
    
    for chapter_num, file_info in chapter_files.items():
        chapter_name = CHAPTER_NAMES.get(chapter_num, f"chapter-{chapter_num}")
        chapter_dir = Path(chapters_dir) / f"chapter-{chapter_num:02d}"
        
        # Create chapter directory if it doesn't exist
        chapter_dir.mkdir(parents=True, exist_ok=True)
        
        target_filename = f"chapter-{chapter_num:02d}-{chapter_name}.json"
        target_path = chapter_dir / target_filename
        
        try:
            shutil.copy2(file_info['json_file'], target_path)
            print(f"  ✅ Chapter {chapter_num:02d}: {target_filename}")
            successful_copies += 1
        except Exception as e:
            error_msg = f"Failed to copy {file_info['json_file']} to {target_path}: {e}"
            print(f"  ❌ Chapter {chapter_num:02d}: {error_msg}")
            failed_copies.append(error_msg)
    
    return chapter_files, unidentified_files, successful_copies, failed_copies

def generate_json_report(chapter_files, unidentified_files, successful_copies, failed_copies, output_dir):
    """Generate JSON organization report."""
    report_path = Path(output_dir) / "analysis" / "json_organization_report.md"
    report_path.parent.mkdir(exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# JSON Files Organization Report\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- **JSON Files Found**: {len(chapter_files) + len(unidentified_files)}\n")
        f.write(f"- **Chapters Identified**: {len(chapter_files)}\n")
        f.write(f"- **Unidentified Files**: {len(unidentified_files)}\n")
        f.write(f"- **Successful Copies**: {successful_copies}\n")
        f.write(f"- **Failed Copies**: {len(failed_copies)}\n\n")
        
        f.write("## Organized Chapters\n\n")
        f.write("| Chapter | Name | Source Directory |\n")
        f.write("|---------|------|------------------|\n")
        
        for chapter_num in sorted(chapter_files.keys()):
            chapter_name = CHAPTER_NAMES.get(chapter_num, f"chapter-{chapter_num}")
            source_dir = chapter_files[chapter_num]['timestamp_dir']
            f.write(f"| {chapter_num:02d} | {chapter_name} | {source_dir} |\n")
        
        if unidentified_files:
            f.write(f"\n## Unidentified Files\n\n")
            for file_info in unidentified_files:
                f.write(f"- {file_info['timestamp_dir']}\n")
        
        if failed_copies:
            f.write(f"\n## Failed Copies\n\n")
            for error in failed_copies:
                f.write(f"- {error}\n")
    
    print(f"📋 JSON report saved to {report_path}")

def main():
    """Main function."""
    playwright_dir = "../playwright-mcp-output11"
    chapters_dir = "../chapters"
    output_dir = "../"
    
    print("📊 JSON Files Organization")
    print("=" * 40)
    
    chapter_files, unidentified_files, successful_copies, failed_copies = organize_json_files(
        playwright_dir, chapters_dir
    )
    
    generate_json_report(
        chapter_files, unidentified_files, successful_copies, failed_copies, output_dir
    )
    
    # Final summary
    print(f"\n🎉 JSON Organization Complete!")
    print(f"📊 {len(chapter_files)} chapters with JSON files")
    print(f"✅ {successful_copies} JSON files successfully copied")
    if failed_copies:
        print(f"⚠️  {len(failed_copies)} copy operations failed")
    if unidentified_files:
        print(f"❓ {len(unidentified_files)} files could not be identified")

if __name__ == "__main__":
    main()
