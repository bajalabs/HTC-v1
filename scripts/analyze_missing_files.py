#!/usr/bin/env python3
import json
import csv
from pathlib import Path

def main():
    print("📊 Missing Files Analysis")
    print("=" * 50)
    
    playwright_dir = Path("../playwright-mcp-output11")
    chapters_dir = Path("../chapters")
    
    # Analyze playwright folder
    playwright_csv = set()
    playwright_json = set()
    
    for item in playwright_dir.iterdir():
        if item.is_dir() and item.name.startswith('2025-'):
            csv_file = item / "htsdata.csv"
            json_file = item / "htsdata.json"
            
            if csv_file.exists():
                try:
                    with open(csv_file, 'r', encoding='utf-8') as f:
                        reader = csv.reader(f)
                        header = next(reader)
                        first_row = next(reader)
                        hts_number = first_row[0].strip('"').strip()
                        if len(hts_number) >= 2 and hts_number.isdigit():
                            chapter_num = int(hts_number[:2])
                            playwright_csv.add(chapter_num)
                except:
                    pass
            
            if json_file.exists():
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, list) and len(data) > 0:
                            first_data = data[0]
                            if isinstance(first_data, dict) and 'htsno' in first_data:
                                hts_number = str(first_data['htsno']).strip()
                                if len(hts_number) >= 2 and hts_number.isdigit():
                                    chapter_num = int(hts_number[:2])
                                    playwright_json.add(chapter_num)
                except:
                    pass
    
    # Analyze chapters folder
    organized_csv = set()
    organized_json = set()
    
    for item in chapters_dir.iterdir():
        if item.is_dir() and item.name.startswith('chapter-'):
            chapter_num = int(item.name.split('-')[1])
            
            if list(item.glob("*.csv")):
                organized_csv.add(chapter_num)
            if list(item.glob("*.json")):
                organized_json.add(chapter_num)
    
    print(f"\n📁 PLAYWRIGHT FOLDER:")
    print(f"  CSV chapters:   {len(playwright_csv)} - {sorted(playwright_csv)}")
    print(f"  JSON chapters:  {len(playwright_json)} - {sorted(playwright_json)}")
    
    print(f"\n📁 CHAPTERS FOLDER:")
    print(f"  CSV chapters:   {len(organized_csv)} - {sorted(organized_csv)}")
    print(f"  JSON chapters:  {len(organized_json)} - {sorted(organized_json)}")
    
    missing_json = playwright_json - organized_json
    print(f"\n❌ MISSING JSON CHAPTERS: {sorted(missing_json) if missing_json else 'None'}")

if __name__ == "__main__":
    main()
