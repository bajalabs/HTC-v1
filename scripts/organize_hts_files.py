#!/usr/bin/env python3
"""
HTS File Organization Script
Organizes HTS files into chapter-specific directories with proper naming.
"""

import os
import shutil
import json
import csv
from pathlib import Path

def load_file_mapping(mapping_file):
    """Load the file mapping from analysis results."""
    try:
        with open(mapping_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Mapping file {mapping_file} not found. Please run analyze_hts_files.py first.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error reading mapping file: {e}")
        return []

def create_chapter_directories(base_dir, chapters):
    """Create directory structure for chapters."""
    chapters_dir = Path(base_dir) / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)
    
    created_dirs = []
    for chapter_num in chapters:
        chapter_dir = chapters_dir / f"chapter-{chapter_num:02d}"
        chapter_dir.mkdir(exist_ok=True)
        created_dirs.append(chapter_dir)
    
    return chapters_dir, created_dirs

def copy_and_rename_files(mapping_data, output_base_dir):
    """Copy and rename files according to mapping."""
    chapters = [item['chapter_number'] for item in mapping_data]
    chapters_dir, created_dirs = create_chapter_directories(output_base_dir, chapters)
    
    successful_copies = 0
    failed_copies = []
    
    for item in mapping_data:
        chapter_num = item['chapter_number']
        chapter_name = item['chapter_name']
        timestamp_dir = item['timestamp_dir']
        
        # Target directory
        target_dir = chapters_dir / f"chapter-{chapter_num:02d}"
        
        # File extensions and paths
        files_to_copy = [
            ('csv', item['csv_path'], f"chapter-{chapter_num:02d}-{chapter_name}.csv"),
            ('json', item['json_path'], f"chapter-{chapter_num:02d}-{chapter_name}.json"),
            ('xlsx', item['xlsx_path'], f"chapter-{chapter_num:02d}-{chapter_name}.xlsx")
        ]
        
        print(f"Processing Chapter {chapter_num}: {chapter_name}")
        
        for file_type, source_path, target_filename in files_to_copy:
            if source_path and Path(source_path).exists():
                target_path = target_dir / target_filename
                
                try:
                    shutil.copy2(source_path, target_path)
                    print(f"  ✓ Copied {file_type.upper()}: {target_filename}")
                    successful_copies += 1
                except Exception as e:
                    error_msg = f"Failed to copy {source_path} to {target_path}: {e}"
                    print(f"  ✗ {error_msg}")
                    failed_copies.append(error_msg)
            else:
                print(f"  - Skipped {file_type.upper()}: file not found")
    
    return successful_copies, failed_copies

def validate_organization(chapters_dir):
    """Validate that files were organized correctly."""
    validation_results = []
    
    for chapter_dir in sorted(chapters_dir.glob("chapter-*")):
        if not chapter_dir.is_dir():
            continue
            
        chapter_name = chapter_dir.name
        files = list(chapter_dir.glob("*"))
        
        csv_files = [f for f in files if f.suffix == '.csv']
        json_files = [f for f in files if f.suffix == '.json']
        xlsx_files = [f for f in files if f.suffix == '.xlsx']
        
        result = {
            'chapter': chapter_name,
            'total_files': len(files),
            'csv_count': len(csv_files),
            'json_count': len(json_files),
            'xlsx_count': len(xlsx_files),
            'complete': len(csv_files) == 1 and len(json_files) == 1 and len(xlsx_files) == 1
        }
        
        validation_results.append(result)
        
        status = "✓" if result['complete'] else "⚠"
        print(f"{status} {chapter_name}: {result['csv_count']} CSV, {result['json_count']} JSON, {result['xlsx_count']} Excel")
    
    return validation_results

def generate_organization_report(validation_results, output_dir, successful_copies, failed_copies):
    """Generate a report of the organization process."""
    report_path = Path(output_dir) / "organization_report.md"
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# HTS File Organization Report\n\n")
        
        # Summary statistics
        total_chapters = len(validation_results)
        complete_chapters = sum(1 for r in validation_results if r['complete'])
        total_files = sum(r['total_files'] for r in validation_results)
        
        f.write("## Summary\n\n")
        f.write(f"- **Total Chapters Processed**: {total_chapters}\n")
        f.write(f"- **Complete Chapters**: {complete_chapters}\n")
        f.write(f"- **Total Files Organized**: {total_files}\n")
        f.write(f"- **Successful Copies**: {successful_copies}\n")
        f.write(f"- **Failed Copies**: {len(failed_copies)}\n\n")
        
        # Chapter details
        f.write("## Chapter Details\n\n")
        f.write("| Chapter | CSV | JSON | Excel | Status |\n")
        f.write("|---------|-----|------|-------|--------|\n")
        
        for result in validation_results:
            status = "Complete" if result['complete'] else "Incomplete"
            f.write(f"| {result['chapter']} | {result['csv_count']} | {result['json_count']} | {result['xlsx_count']} | {status} |\n")
        
        # Failed copies
        if failed_copies:
            f.write("\n## Failed Copies\n\n")
            for error in failed_copies:
                f.write(f"- {error}\n")
        
        f.write(f"\n## Directory Structure Created\n\n")
        f.write("```\n")
        f.write("HTS/\n")
        f.write("└── chapters/\n")
        for result in validation_results:
            f.write(f"    ├── {result['chapter']}/\n")
            if result['csv_count'] > 0:
                f.write(f"    │   ├── {result['chapter']}-*.csv\n")
            if result['json_count'] > 0:
                f.write(f"    │   ├── {result['chapter']}-*.json\n")
            if result['xlsx_count'] > 0:
                f.write(f"    │   └── {result['chapter']}-*.xlsx\n")
        f.write("```\n")
    
    print(f"Organization report saved to {report_path}")

def main():
    """Main function to organize files."""
    # Import configuration
    try:
        from config import ANALYSIS_OUTPUT_DIR
        mapping_file = f"{ANALYSIS_OUTPUT_DIR}/file_mapping.json"
        output_base_dir = "../"
    except ImportError:
        # Fallback to default paths
        mapping_file = "../analysis/file_mapping.json"
        output_base_dir = "../"
    
    print("Starting HTS file organization...")
    
    # Load mapping data
    mapping_data = load_file_mapping(mapping_file)
    if not mapping_data:
        return
    
    print(f"Found mapping for {len(mapping_data)} chapters")
    
    # Copy and rename files
    successful_copies, failed_copies = copy_and_rename_files(mapping_data, output_base_dir)
    
    # Validate organization
    chapters_dir = Path(output_base_dir) / "chapters"
    print(f"\nValidating organization in {chapters_dir}...")
    validation_results = validate_organization(chapters_dir)
    
    # Generate report
    generate_organization_report(validation_results, "../analysis", successful_copies, failed_copies)
    
    # Summary
    complete_chapters = sum(1 for r in validation_results if r['complete'])
    print(f"\n🎉 Organization complete!")
    print(f"📁 {len(validation_results)} chapters organized")
    print(f"✅ {complete_chapters} chapters have all 3 file formats")
    print(f"📄 {successful_copies} files successfully copied")
    
    if failed_copies:
        print(f"⚠️  {len(failed_copies)} copy operations failed")

if __name__ == "__main__":
    main()
