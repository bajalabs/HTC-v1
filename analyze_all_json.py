#!/usr/bin/env python3
"""
Comprehensive JSON Analysis Script
Analyzes all 96 JSON files to identify chapters and find what we're missing
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def analyze_json_file(json_file):
    """Analyze a single JSON file to extract chapter information"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, list) and len(data) > 0:
            first_data = data[0]
            
            # Try different field names for HTS number
            hts_number = None
            if isinstance(first_data, dict):
                for field_name in ['htsno', 'HTS Number', 'HTS_Number', 'hts_number', 'HTS', 'hts']:
                    if field_name in first_data:
                        hts_number = str(first_data[field_name]).strip('"').strip()
                        break
            elif isinstance(first_data, list) and len(first_data) > 0:
                hts_number = str(first_data[0]).strip('"').strip()
            
            if hts_number and len(hts_number) >= 2:
                if hts_number.isdigit():
                    chapter_num = int(hts_number[:2])
                    if 1 <= chapter_num <= 99:
                        return chapter_num, hts_number, len(data)
                    
        return None, None, len(data) if isinstance(data, list) else 0
        
    except Exception as e:
        return None, f"Error: {e}", 0

def main():
    print("🔍 Comprehensive JSON Analysis")
    print("=" * 60)
    
    json_files = list(Path(".").glob("*.json"))
    print(f"Found {len(json_files)} JSON files to analyze")
    print()
    
    # Track chapters and files
    chapters_found = defaultdict(list)
    unidentified_files = []
    error_files = []
    
    print("📊 Analyzing each JSON file:")
    print("-" * 60)
    
    for json_file in sorted(json_files):
        chapter_num, hts_info, record_count = analyze_json_file(json_file)
        
        if chapter_num:
            chapters_found[chapter_num].append({
                'file': json_file.name,
                'hts_number': hts_info,
                'records': record_count
            })
            print(f"✅ {json_file.name}: Chapter {chapter_num:02d} (HTS: {hts_info}, Records: {record_count})")
        elif "Error:" in str(hts_info):
            error_files.append({'file': json_file.name, 'error': hts_info})
            print(f"❌ {json_file.name}: {hts_info}")
        else:
            unidentified_files.append({'file': json_file.name, 'records': record_count})
            print(f"❓ {json_file.name}: Could not identify chapter (Records: {record_count})")
    
    print()
    print("📋 SUMMARY RESULTS")
    print("=" * 60)
    
    print(f"Total JSON files analyzed: {len(json_files)}")
    print(f"Successfully identified: {sum(len(files) for files in chapters_found.values())}")
    print(f"Unidentified files: {len(unidentified_files)}")
    print(f"Error files: {len(error_files)}")
    print(f"Unique chapters found: {len(chapters_found)}")
    
    print(f"\n📊 CHAPTERS IDENTIFIED:")
    print("-" * 40)
    
    all_chapters = sorted(chapters_found.keys())
    for chapter_num in all_chapters:
        files = chapters_found[chapter_num]
        print(f"Chapter {chapter_num:02d}: {len(files)} file(s)")
        for file_info in files:
            print(f"  - {file_info['file']} (HTS: {file_info['hts_number']}, Records: {file_info['records']})")
    
    if unidentified_files:
        print(f"\n❓ UNIDENTIFIED FILES ({len(unidentified_files)}):")
        print("-" * 40)
        for file_info in unidentified_files:
            print(f"  - {file_info['file']} (Records: {file_info['records']})")
    
    if error_files:
        print(f"\n❌ ERROR FILES ({len(error_files)}):")
        print("-" * 40)
        for file_info in error_files:
            print(f"  - {file_info['file']}: {file_info['error']}")
    
    # Compare with organized chapters
    print(f"\n🔍 COMPARISON WITH ORGANIZED CHAPTERS:")
    print("-" * 40)
    
    chapters_dir = Path("../chapters")
    if chapters_dir.exists():
        organized_json_chapters = set()
        for item in chapters_dir.iterdir():
            if item.is_dir() and item.name.startswith('chapter-'):
                chapter_num = int(item.name.split('-')[1])
                if list(item.glob("*.json")):
                    organized_json_chapters.add(chapter_num)
        
        found_chapters_set = set(chapters_found.keys())
        
        print(f"Chapters found in JSON analysis: {len(found_chapters_set)}")
        print(f"Chapters with JSON in organized folder: {len(organized_json_chapters)}")
        
        missing_from_organized = found_chapters_set - organized_json_chapters
        extra_in_organized = organized_json_chapters - found_chapters_set
        
        if missing_from_organized:
            print(f"\n🚨 CHAPTERS MISSING FROM ORGANIZED FOLDER:")
            print(f"   {sorted(missing_from_organized)}")
        
        if extra_in_organized:
            print(f"\n🤔 CHAPTERS IN ORGANIZED BUT NOT IN ANALYSIS:")
            print(f"   {sorted(extra_in_organized)}")
        
        if not missing_from_organized and not extra_in_organized:
            print(f"\n✅ PERFECT MATCH: All chapters match between analysis and organized folder!")
    
    print(f"\n🎯 FINAL CHAPTER LIST:")
    print(f"   {sorted(chapters_found.keys())}")

if __name__ == "__main__":
    main()
