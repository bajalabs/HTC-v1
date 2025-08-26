#!/usr/bin/env python3
"""
Analyze missing files between playwright source and organized chapters
"""

import json
import csv
from pathlib import Path
from collections import defaultdict

def analyze_playwright_folder():
    """Analyze what we have in the playwright folder"""
    playwright_dir = Path("../playwright-mcp-output11")
    
    chapters_found = {
        'csv': set(),
        'json': set(), 
        'xlsx': set()
    }
    
    print("🔍 Analyzing playwright folder...")
    
    for item in playwright_dir.iterdir():
        if item.is_dir() and item.name.startswith('2025-'):
            # Check each file type
            csv_file = item / "htsdata.csv"
            json_file = item / "htsdata.json"
            xlsx_file = item / "htsdata.xlsx"
            
            # Identify chapter from CSV
            if csv_file.exists():
                try:
                    with open(csv_file, 'r', encoding='utf-8') as f:
                        reader = csv.reader(f)
                        header = next(reader)
                        first_row = next(reader)
                        hts_number = first_row[0].strip('"').strip()
                        if len(hts_number) >= 2 and hts_number.isdigit():
                            chapter_num = int(hts_number[:2])
                            chapters_found['csv'].add(chapter_num)
                except:
                    pass
            
            # Identify chapter from JSON
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
                                    chapters_found['json'].add(chapter_num)
                except:
                    pass
    
    return chapters_found

def analyze_chapters_folder():
    """Analyze what we have in the chapters folder"""
    chapters_dir = Path("../chapters")
    
    chapters_organized = {
        'csv': set(),
        'json': set(),
        'xlsx': set()
    }
    
    print("🔍 Analyzing chapters folder...")
    
    for item in chapters_dir.iterdir():
        if item.is_dir() and item.name.startswith('chapter-'):
            chapter_num = int(item.name.split('-')[1])
            
            # Check what files exist
            if list(item.glob("*.csv")):
                chapters_organized['csv'].add(chapter_num)
            if list(item.glob("*.json")):
                chapters_organized['json'].add(chapter_num)
            if list(item.glob("*.xlsx")):
                chapters_organized['xlsx'].add(chapter_num)
    
    return chapters_organized

def main():
    print("📊 Missing Files Analysis")
    print("=" * 50)
    
    # Analyze both folders
    playwright_chapters = analyze_playwright_folder()
    organized_chapters = analyze_chapters_folder()
    
    print(f"\n📁 PLAYWRIGHT FOLDER:")
    print(f"  CSV chapters:   {len(playwright_chapters['csv'])} chapters")
    print(f"  JSON chapters:  {len(playwright_chapters['json'])} chapters") 
    print(f"  Excel chapters: {len(playwright_chapters['xlsx'])} chapters")
    
    print(f"\n📁 CHAPTERS FOLDER:")
    print(f"  CSV chapters:   {len(organized_chapters['csv'])} chapters")
    print(f"  JSON chapters:  {len(organized_chapters['json'])} chapters")
    print(f"  Excel chapters: {len(organized_chapters['xlsx'])} chapters")
    
    # Find missing files
    print(f"\n❌ MISSING FILES:")
    
    missing_csv = playwright_chapters['csv'] - organized_chapters['csv']
    missing_json = playwright_chapters['json'] - organized_chapters['json']
    missing_xlsx = playwright_chapters['xlsx'] - organized_chapters['xlsx']
    
    if missing_csv:
        print(f"  Missing CSV chapters:   {sorted(missing_csv)}")
    else:
        print(f"  Missing CSV chapters:   None")
        
    if missing_json:
        print(f"  Missing JSON chapters:  {sorted(missing_json)}")
    else:
        print(f"  Missing JSON chapters:  None")
        
    if missing_xlsx:
        print(f"  Missing Excel chapters: {sorted(missing_xlsx)}")
    else:
        print(f"  Missing Excel chapters: None")
    
    # Show chapters available in playwright but not organized
    print(f"\n📋 CHAPTERS IN PLAYWRIGHT BY FORMAT:")
    print(f"  CSV:   {sorted(playwright_chapters['csv'])}")
    print(f"  JSON:  {sorted(playwright_chapters['json'])}")
    print(f"  Excel: {sorted(playwright_chapters['xlsx'])}")
    
    print(f"\n📋 CHAPTERS ORGANIZED BY FORMAT:")
    print(f"  CSV:   {sorted(organized_chapters['csv'])}")
    print(f"  JSON:  {sorted(organized_chapters['json'])}")
    print(f"  Excel: {sorted(organized_chapters['xlsx'])}")

if __name__ == "__main__":
    main()
