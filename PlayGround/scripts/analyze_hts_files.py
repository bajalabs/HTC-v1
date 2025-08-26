#!/usr/bin/env python3
"""
HTS File Analysis Script
Analyzes downloaded HTS files to identify which chapter each file contains
and creates a mapping for organization.
"""

import os
import csv
import json
from pathlib import Path
import re
from datetime import datetime

# Chapter names mapping based on HTS structure
CHAPTER_NAMES = {
    1: "live-animals",
    2: "meat-and-edible-meat-offal",
    3: "fish-and-crustaceans",
    4: "dairy-produce-birds-eggs",
    5: "products-of-animal-origin",
    7: "edible-vegetables-and-roots",  # Chapter 6 was skipped
    8: "edible-fruit-and-nuts",
    9: "coffee-tea-mate-spices",
    10: "cereals",
    11: "milling-industry-products",
    12: "oil-seeds-oleaginous-fruits",
    13: "lac-gums-resins-vegetable-extracts",
    14: "vegetable-plaiting-materials",
    15: "animal-vegetable-fats-oils",
    16: "meat-fish-preparations",
    17: "sugars-sugar-confectionery",
    18: "cocoa-cocoa-preparations",
    19: "cereal-flour-starch-preparations",
    20: "vegetable-fruit-preparations",
    21: "miscellaneous-edible-preparations",
    22: "beverages-spirits-vinegar",
    23: "food-industry-residues-animal-feed",
    24: "tobacco-manufactured-tobacco",
    25: "salt-sulfur-earths-stone",
    26: "ores-slag-ash",
    27: "mineral-fuels-oils",
    28: "inorganic-chemicals",
    29: "organic-chemicals",
    30: "pharmaceutical-products",
    31: "fertilizers",
    32: "tanning-dyeing-extracts",
    33: "essential-oils-perfumery",
    34: "soap-organic-surface-agents",
    35: "albuminoidal-substances",
    36: "explosives-pyrotechnics",
    37: "photographic-cinematographic-goods",
    38: "miscellaneous-chemical-products",
    39: "plastics-articles-thereof",
    40: "rubber-articles-thereof",
    41: "raw-hides-skins-leather",
    42: "leather-articles-saddlery",
    43: "furskins-artificial-fur",
    44: "wood-articles-wood-charcoal",
    45: "cork-articles-cork",
    46: "straw-plaiting-materials",
    47: "wood-pulp-fibrous-material",
    48: "paper-paperboard-articles",
    49: "printed-books-newspapers",
    50: "silk",
    51: "wool-animal-hair",
    52: "cotton",
    53: "vegetable-textile-fibers",
    54: "man-made-filaments",
    55: "man-made-staple-fibers",
    56: "wadding-felt-nonwovens",
    57: "carpets-textile-floor-coverings",
    58: "special-woven-fabrics",
    59: "impregnated-coated-textile-fabrics",
    60: "knitted-crocheted-fabrics",
    61: "knitted-crocheted-apparel",
    62: "not-knitted-crocheted-apparel",
    63: "textile-articles-worn-clothing",
    64: "footwear-gaiters",
    65: "headgear-parts-thereof",
    66: "umbrellas-walking-sticks",
    67: "prepared-feathers-artificial-flowers",
    68: "stone-plaster-cement-articles",
    69: "ceramic-products",
    70: "glass-glassware",
    71: "pearls-precious-stones-metals",
    72: "iron-steel",
    73: "iron-steel-articles",
    74: "copper-articles-thereof",
    75: "nickel-articles-thereof",
    76: "aluminum-articles-thereof",
    78: "lead-articles-thereof",  # Chapter 77 was reserved/empty
    79: "zinc-articles-thereof",
    80: "tin-articles-thereof",
    81: "base-metals-cermets",
    82: "tools-implements-cutlery",
    83: "miscellaneous-base-metal-articles",
    84: "nuclear-reactors-boilers-machinery",
    85: "electrical-machinery-equipment",
    86: "railway-locomotives-rolling-stock",
    87: "vehicles-parts-accessories",
    88: "aircraft-spacecraft-parts",
    89: "ships-boats-floating-structures",
    90: "optical-photographic-instruments",
    91: "clocks-watches-parts",
    92: "musical-instruments-parts",
    93: "arms-ammunition-parts",
    94: "furniture-bedding-lamps",
    95: "toys-games-sports",
    96: "miscellaneous-manufactured-articles",
    97: "works-of-art-collectors-pieces",
    98: "special-classification-provisions",
    99: "temporary-legislation-modifications"
}

def find_hts_files(base_dir):
    """Find all HTS data files in timestamp directories."""
    files_found = []
    base_path = Path(base_dir)
    
    if not base_path.exists():
        print(f"Directory {base_dir} does not exist!")
        return files_found
    
    # Look for timestamp directories
    timestamp_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}\.\d{3}Z$')
    
    for item in base_path.iterdir():
        if item.is_dir() and timestamp_pattern.match(item.name):
            # Check for HTS files in this timestamp directory
            csv_file = item / "htsdata.csv"
            json_file = item / "htsdata.json"
            xlsx_file = item / "htsdata.xlsx"
            
            if csv_file.exists():
                files_found.append({
                    'timestamp_dir': item.name,
                    'csv_file': csv_file,
                    'json_file': json_file if json_file.exists() else None,
                    'xlsx_file': xlsx_file if xlsx_file.exists() else None
                })
    
    return files_found

def identify_chapter_from_csv(csv_file):
    """Identify HTS chapter number from CSV file content."""
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  # Skip header
            
            # Read first few data rows to find HTS numbers
            for i, row in enumerate(reader):
                if i >= 10:  # Check first 10 rows max
                    break
                
                if len(row) > 0 and row[0]:  # First column should be HTS Number
                    hts_number = row[0].strip('"').strip()
                    
                    # Extract chapter number from HTS code
                    if len(hts_number) >= 2:
                        try:
                            chapter_num = int(hts_number[:2])
                            if chapter_num > 0 and chapter_num <= 99:
                                return chapter_num
                        except ValueError:
                            continue
    
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")
    
    return None

def analyze_all_files(base_dir):
    """Analyze all HTS files and create mapping."""
    files = find_hts_files(base_dir)
    print(f"Found {len(files)} timestamp directories with HTS files")
    
    chapter_mapping = {}
    analysis_results = []
    
    for file_info in files:
        timestamp_dir = file_info['timestamp_dir']
        csv_file = file_info['csv_file']
        
        print(f"Analyzing {timestamp_dir}...")
        
        chapter_num = identify_chapter_from_csv(csv_file)
        
        if chapter_num:
            chapter_name = CHAPTER_NAMES.get(chapter_num, f"chapter-{chapter_num}")
            
            result = {
                'timestamp_dir': timestamp_dir,
                'chapter_number': chapter_num,
                'chapter_name': chapter_name,
                'has_csv': file_info['csv_file'] is not None,
                'has_json': file_info['json_file'] is not None,
                'has_xlsx': file_info['xlsx_file'] is not None,
                'csv_path': str(file_info['csv_file']),
                'json_path': str(file_info['json_file']) if file_info['json_file'] else '',
                'xlsx_path': str(file_info['xlsx_file']) if file_info['xlsx_file'] else ''
            }
            
            analysis_results.append(result)
            chapter_mapping[chapter_num] = file_info
            
            print(f"  → Chapter {chapter_num}: {chapter_name}")
        else:
            print(f"  → Could not identify chapter for {timestamp_dir}")
    
    return analysis_results, chapter_mapping

def save_analysis_results(results, output_dir):
    """Save analysis results to files."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Save as CSV
    csv_output = os.path.join(output_dir, "file_mapping.csv")
    with open(csv_output, 'w', newline='', encoding='utf-8') as f:
        if results:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
    
    # Save as JSON
    json_output = os.path.join(output_dir, "file_mapping.json")
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    # Generate summary
    summary_output = os.path.join(output_dir, "analysis_summary.md")
    with open(summary_output, 'w', encoding='utf-8') as f:
        f.write("# HTS File Analysis Summary\n\n")
        f.write(f"Analysis completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Total files analyzed: {len(results)}\n\n")
        
        # Chapter distribution
        chapters_found = sorted([r['chapter_number'] for r in results])
        f.write(f"Chapters found: {', '.join(map(str, chapters_found))}\n\n")
        
        # Missing chapters
        expected_chapters = set(range(1, 100)) - {6, 77}  # Exclude known missing chapters
        found_chapters = set(chapters_found)
        missing_chapters = expected_chapters - found_chapters
        
        if missing_chapters:
            f.write(f"Missing chapters: {', '.join(map(str, sorted(missing_chapters)))}\n\n")
        else:
            f.write("All expected chapters found!\n\n")
        
        # Detailed listing
        f.write("## Chapter Details\n\n")
        for result in sorted(results, key=lambda x: x['chapter_number']):
            f.write(f"- **Chapter {result['chapter_number']}**: {result['chapter_name']}\n")
            f.write(f"  - Directory: {result['timestamp_dir']}\n")
            f.write(f"  - Files: CSV={result['has_csv']}, JSON={result['has_json']}, Excel={result['has_xlsx']}\n\n")
    
    print(f"Analysis results saved to {output_dir}")

def main():
    """Main function to run the analysis."""
    # Import configuration
    try:
        from config import PLAYWRIGHT_OUTPUT_DIR, ANALYSIS_OUTPUT_DIR
        playwright_output_dir = PLAYWRIGHT_OUTPUT_DIR
        analysis_output_dir = ANALYSIS_OUTPUT_DIR
    except ImportError:
        # Fallback to default paths
        playwright_output_dir = "../playwright-mcp-output11"
        analysis_output_dir = "../analysis"
    
    print("Starting HTS file analysis...")
    print(f"Looking for files in: {playwright_output_dir}")
    
    results, mapping = analyze_all_files(playwright_output_dir)
    
    if results:
        save_analysis_results(results, analysis_output_dir)
        print(f"\nAnalysis complete! Found {len(results)} chapters.")
        print(f"Results saved to {analysis_output_dir}")
    else:
        print("No HTS files found or no chapters could be identified.")

if __name__ == "__main__":
    main()
