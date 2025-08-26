#!/usr/bin/env python3
"""
Complete HTS File Organization Script
Finds all HTS files (CSV, JSON, Excel) and organizes them by chapter.
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

def find_all_hts_files(playwright_dir):
    """Find all HTS files (CSV, JSON, Excel) in timestamp directories."""
    base_path = Path(playwright_dir)
    timestamp_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}\.\d{3}Z$')
    
    all_files = []
    
    for item in base_path.iterdir():
        if item.is_dir() and timestamp_pattern.match(item.name):
            files_in_dir = {
                'timestamp_dir': item.name,
                'csv_file': None,
                'json_file': None,
                'xlsx_file': None
            }
            
            # Check for all three file types
            csv_file = item / "htsdata.csv"
            json_file = item / "htsdata.json"
            xlsx_file = item / "htsdata.xlsx"
            
            if csv_file.exists():
                files_in_dir['csv_file'] = csv_file
            if json_file.exists():
                files_in_dir['json_file'] = json_file
            if xlsx_file.exists():
                files_in_dir['xlsx_file'] = xlsx_file
            
            # Only include if at least one file exists
            if any([files_in_dir['csv_file'], files_in_dir['json_file'], files_in_dir['xlsx_file']]):
                all_files.append(files_in_dir)
    
    return all_files

def identify_chapter_from_file(file_path):
    """Identify chapter from any HTS file (CSV, JSON, or Excel)."""
    if not file_path or not file_path.exists():
        return None
    
    try:
        if file_path.suffix == '.csv':
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)
                first_row = next(reader)
                hts_number = first_row[0].strip('"').strip()
                
        elif file_path.suffix == '.json':
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 1:
                    # Assuming first item is header, second is data
                    first_data = data[1] if len(data) > 1 else data[0]
                    if isinstance(first_data, dict) and 'HTS Number' in first_data:
                        hts_number = first_data['HTS Number'].strip('"').strip()
                    elif isinstance(first_data, list) and len(first_data) > 0:
                        hts_number = str(first_data[0]).strip('"').strip()
                    else:
                        return None
                else:
                    return None
        else:
            # For Excel files, we'll use the CSV file from the same directory
            csv_file = file_path.parent / "htsdata.csv"
            if csv_file.exists():
                return identify_chapter_from_file(csv_file)
            return None
        
        # Extract chapter number
        if len(hts_number) >= 2:
            chapter_num = int(hts_number[:2])
            if 1 <= chapter_num <= 99:
                return chapter_num
                
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return None

def organize_files_by_chapter(playwright_dir, output_dir):
    """Organize all HTS files by chapter."""
    print("🔍 Finding all HTS files...")
    all_files = find_all_hts_files(playwright_dir)
    print(f"Found {len(all_files)} timestamp directories with HTS files")
    
    # Group files by chapter
    chapter_files = defaultdict(lambda: {'csv': None, 'json': None, 'xlsx': None})
    
    print("📊 Analyzing files to identify chapters...")
    for file_info in all_files:
        # Try to identify chapter from any available file
        chapter_num = None
        
        # Try CSV first (most reliable)
        if file_info['csv_file']:
            chapter_num = identify_chapter_from_file(file_info['csv_file'])
        
        # If no CSV, try JSON
        if not chapter_num and file_info['json_file']:
            chapter_num = identify_chapter_from_file(file_info['json_file'])
        
        # If still no chapter, try using Excel via CSV
        if not chapter_num and file_info['xlsx_file']:
            chapter_num = identify_chapter_from_file(file_info['xlsx_file'])
        
        if chapter_num:
            chapter_name = CHAPTER_NAMES.get(chapter_num, f"chapter-{chapter_num}")
            print(f"  Chapter {chapter_num}: {chapter_name} ({file_info['timestamp_dir']})")
            
            # Store file paths for this chapter (only keep one of each type)
            if not chapter_files[chapter_num]['csv'] and file_info['csv_file']:
                chapter_files[chapter_num]['csv'] = file_info['csv_file']
            if not chapter_files[chapter_num]['json'] and file_info['json_file']:
                chapter_files[chapter_num]['json'] = file_info['json_file']
            if not chapter_files[chapter_num]['xlsx'] and file_info['xlsx_file']:
                chapter_files[chapter_num]['xlsx'] = file_info['xlsx_file']
        else:
            print(f"  Could not identify chapter for {file_info['timestamp_dir']}")
    
    # Create chapter directories and copy files
    chapters_dir = Path(output_dir) / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)
    
    print("📁 Creating chapter directories and copying files...")
    successful_copies = 0
    
    for chapter_num in sorted(chapter_files.keys()):
        chapter_name = CHAPTER_NAMES.get(chapter_num, f"chapter-{chapter_num}")
        chapter_dir = chapters_dir / f"chapter-{chapter_num:02d}"
        chapter_dir.mkdir(exist_ok=True)
        
        print(f"\n📂 Chapter {chapter_num}: {chapter_name}")
        
        # Copy each file type
        for file_type, source_path in chapter_files[chapter_num].items():
            if source_path and source_path.exists():
                target_filename = f"chapter-{chapter_num:02d}-{chapter_name}.{file_type}"
                target_path = chapter_dir / target_filename
                
                try:
                    shutil.copy2(source_path, target_path)
                    print(f"  ✅ {file_type.upper()}: {target_filename}")
                    successful_copies += 1
                except Exception as e:
                    print(f"  ❌ {file_type.upper()}: {e}")
            else:
                print(f"  ⚪ {file_type.upper()}: not available")
    
    return chapter_files, successful_copies

def generate_final_report(chapter_files, successful_copies, output_dir):
    """Generate final organization report."""
    report_path = Path(output_dir) / "analysis" / "final_organization_report.md"
    report_path.parent.mkdir(exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Final HTS Organization Report\n\n")
        
        total_chapters = len(chapter_files)
        complete_chapters = sum(1 for files in chapter_files.values() 
                              if all(files[ft] for ft in ['csv', 'json', 'xlsx']))
        
        f.write("## Summary\n\n")
        f.write(f"- **Total Chapters Found**: {total_chapters}\n")
        f.write(f"- **Chapters with All 3 Formats**: {complete_chapters}\n")
        f.write(f"- **Total Files Copied**: {successful_copies}\n\n")
        
        f.write("## Chapter Details\n\n")
        f.write("| Chapter | Name | CSV | JSON | Excel |\n")
        f.write("|---------|------|-----|------|-------|\n")
        
        for chapter_num in sorted(chapter_files.keys()):
            chapter_name = CHAPTER_NAMES.get(chapter_num, f"chapter-{chapter_num}")
            files = chapter_files[chapter_num]
            csv_status = "✅" if files['csv'] else "❌"
            json_status = "✅" if files['json'] else "❌"
            xlsx_status = "✅" if files['xlsx'] else "❌"
            
            f.write(f"| {chapter_num:02d} | {chapter_name} | {csv_status} | {json_status} | {xlsx_status} |\n")
        
        missing_chapters = set(range(1, 100)) - {6, 77} - set(chapter_files.keys())
        if missing_chapters:
            f.write(f"\n## Missing Chapters\n\n")
            f.write(f"Chapters not found: {', '.join(map(str, sorted(missing_chapters)))}\n")
    
    print(f"📋 Final report saved to {report_path}")

def main():
    """Main function."""
    playwright_dir = "../playwright-mcp-output11"
    output_dir = "../"
    
    print("🎯 Complete HTS File Organization")
    print("=" * 50)
    
    chapter_files, successful_copies = organize_files_by_chapter(playwright_dir, output_dir)
    generate_final_report(chapter_files, successful_copies, output_dir)
    
    # Final summary
    total_chapters = len(chapter_files)
    complete_chapters = sum(1 for files in chapter_files.values() 
                          if all(files[ft] for ft in ['csv', 'json', 'xlsx']))
    
    print(f"\n🎉 Organization Complete!")
    print(f"📊 {total_chapters} chapters organized")
    print(f"✅ {complete_chapters} chapters have all 3 formats")
    print(f"📄 {successful_copies} files successfully copied")
    print(f"📁 Files organized in: chapters/")

if __name__ == "__main__":
    main()
