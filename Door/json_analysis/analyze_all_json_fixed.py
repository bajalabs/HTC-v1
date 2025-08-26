#!/usr/bin/env python3
import json
import re
from pathlib import Path
from collections import defaultdict

def analyze_json_file(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, list) and len(data) > 0:
            first_data = data[0]
            
            hts_number = None
            if isinstance(first_data, dict):
                for field_name in ['htsno', 'HTS Number', 'HTS_Number', 'hts_number', 'HTS', 'hts']:
                    if field_name in first_data:
                        hts_number = str(first_data[field_name]).strip('"').strip()
                        break
            elif isinstance(first_data, list) and len(first_data) > 0:
                hts_number = str(first_data[0]).strip('"').strip()
            
            if hts_number and len(hts_number) >= 2:
                # Extract first 2 digits, handling decimal points and other characters
                match = re.match(r'^(\d{2})', hts_number)
                if match:
                    chapter_num = int(match.group(1))
                    if 1 <= chapter_num <= 99:
                        return chapter_num, hts_number, len(data)
                    
        return None, None, len(data) if isinstance(data, list) else 0
        
    except Exception as e:
        return None, f"Error: {e}", 0

def main():
    print("🔍 FIXED JSON Analysis (Handling Decimal HTS Numbers)")
    print("=" * 70)
    
    json_files = list(Path(".").glob("*.json"))
    print(f"Found {len(json_files)} JSON files to analyze")
    print()
    
    chapters_found = defaultdict(list)
    unidentified_files = []
    
    for json_file in sorted(json_files):
        chapter_num, hts_info, record_count = analyze_json_file(json_file)
        
        if chapter_num:
            chapters_found[chapter_num].append({
                'file': json_file.name,
                'hts_number': hts_info,
                'records': record_count
            })
            print(f"✅ Chapter {chapter_num:02d}: {json_file.name} (HTS: {hts_info})")
        else:
            unidentified_files.append(json_file.name)
            print(f"❓ UNIDENTIFIED: {json_file.name}")
    
    print(f"\n📋 FIXED SUMMARY:")
    print(f"Total files: {len(json_files)}")
    print(f"Identified: {sum(len(files) for files in chapters_found.values())}")
    print(f"Unidentified: {len(unidentified_files)}")
    print(f"Unique chapters: {len(chapters_found)}")
    
    print(f"\n📊 CHAPTERS FOUND: {sorted(chapters_found.keys())}")
    
    # Show chapters with multiple files
    print(f"\n📂 CHAPTERS WITH MULTIPLE FILES:")
    for chapter_num in sorted(chapters_found.keys()):
        files = chapters_found[chapter_num]
        if len(files) > 1:
            print(f"  Chapter {chapter_num:02d}: {len(files)} files")
            for file_info in files:
                print(f"    - {file_info['hts_number']}")
    
    if unidentified_files:
        print(f"\n❓ REMAINING UNIDENTIFIED FILES ({len(unidentified_files)}):")
        for filename in unidentified_files:
            print(f"  - {filename}")

if __name__ == "__main__":
    main()
