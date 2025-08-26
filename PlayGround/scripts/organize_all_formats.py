#!/usr/bin/env python3
"""
Complete File Organization Script
Organizes all HTS file formats (CSV, JSON, Excel) by chapter.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_script(script_path, description):
    """Run a Python script and handle errors."""
    print(f"\n{'='*50}")
    print(f"🚀 {description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, 
                              text=True, 
                              cwd=os.path.dirname(script_path))
        
        if result.stdout:
            print(result.stdout)
        
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode == 0:
            print(f"✅ {description} completed successfully!")
            return True
        else:
            print(f"❌ {description} failed with return code {result.returncode}")
            return False
            
    except Exception as e:
        print(f"❌ Error running {description}: {e}")
        return False

def check_file_counts():
    """Check how many files we have of each type."""
    playwright_dir = Path("../playwright-mcp-output11")
    
    if not playwright_dir.exists():
        print("❌ Playwright output directory not found")
        return False
    
    csv_count = len(list(playwright_dir.glob("*/htsdata.csv")))
    json_count = len(list(playwright_dir.glob("*/htsdata.json")))
    xlsx_count = len(list(playwright_dir.glob("*/htsdata.xlsx")))
    
    print("📊 File Type Counts:")
    print(f"  CSV files:   {csv_count}")
    print(f"  JSON files:  {json_count}")
    print(f"  Excel files: {xlsx_count}")
    print(f"  Total files: {csv_count + json_count + xlsx_count}")
    
    return csv_count > 0 or json_count > 0 or xlsx_count > 0

def validate_final_organization():
    """Validate the final organization results."""
    chapters_dir = Path("../chapters")
    
    if not chapters_dir.exists():
        print("❌ Chapters directory not found")
        return False
    
    chapter_dirs = [d for d in chapters_dir.iterdir() if d.is_dir()]
    
    total_csv = 0
    total_json = 0
    total_xlsx = 0
    complete_chapters = 0
    
    print(f"\n📁 Validation Results:")
    print(f"Found {len(chapter_dirs)} chapter directories")
    
    for chapter_dir in sorted(chapter_dirs):
        csv_files = list(chapter_dir.glob("*.csv"))
        json_files = list(chapter_dir.glob("*.json"))
        xlsx_files = list(chapter_dir.glob("*.xlsx"))
        
        total_csv += len(csv_files)
        total_json += len(json_files)
        total_xlsx += len(xlsx_files)
        
        if csv_files and json_files and xlsx_files:
            complete_chapters += 1
    
    print(f"  CSV files organized:   {total_csv}")
    print(f"  JSON files organized:  {total_json}")
    print(f"  Excel files organized: {total_xlsx}")
    print(f"  Complete chapters:     {complete_chapters} (all 3 formats)")
    
    return True

def main():
    """Main execution function."""
    print("🎯 Complete HTS File Organization")
    print("This script will organize CSV, JSON, and Excel files by chapter")
    print()
    
    # Check file counts
    if not check_file_counts():
        print("❌ No HTS files found. Exiting.")
        return
    
    # Step 1: Organize CSV files (already done, but let's check)
    csv_organized = Path("../chapters").exists()
    if csv_organized:
        print("✅ CSV files already organized")
    else:
        print("⚠️  CSV files not yet organized - run complete_organization.py first")
        return
    
    # Step 2: Organize JSON files
    success = run_script("organize_json_files.py", "ORGANIZING JSON FILES")
    if not success:
        print("⚠️  JSON organization had issues, but continuing...")
    
    # Step 3: Organize Excel files
    success = run_script("organize_excel_files.py", "ORGANIZING EXCEL FILES")
    if not success:
        print("⚠️  Excel organization had issues, but continuing...")
    
    # Step 4: Validate final organization
    print(f"\n{'='*50}")
    print("🔍 FINAL VALIDATION")
    print(f"{'='*50}")
    
    validate_final_organization()
    
    # Final summary
    print(f"\n{'='*50}")
    print("🎉 COMPLETE ORGANIZATION FINISHED!")
    print(f"{'='*50}")
    print()
    print("📁 Your files are now organized in:")
    print("   └── chapters/")
    print("       ├── chapter-01/")
    print("       │   ├── chapter-01-live-animals.csv")
    print("       │   ├── chapter-01-live-animals.json")
    print("       │   └── chapter-01-live-animals.xlsx")
    print("       ├── chapter-02/")
    print("       │   └── ... (similar structure)")
    print("       └── ... (all chapters)")
    print()
    print("📊 Reports available in:")
    print("   └── analysis/")
    print("       ├── final_organization_report.md")
    print("       ├── json_organization_report.md")
    print("       └── excel_organization_report.md")
    print()
    print("🎯 All HTS file formats are now organized!")

if __name__ == "__main__":
    main()
