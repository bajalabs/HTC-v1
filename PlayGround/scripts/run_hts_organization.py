#!/usr/bin/env python3
"""
HTS Organization Runner
Executes the complete workflow to analyze and organize HTS files.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_script(script_path, description):
    """Run a Python script and handle errors."""
    print(f"\n{'='*60}")
    print(f"🚀 {description}")
    print(f"{'='*60}")
    
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

def check_prerequisites():
    """Check if required directories and files exist."""
    print("🔍 Checking prerequisites...")
    
    # Check if playwright-mcp-output directory exists
    playwright_dir = Path("../playwright-mcp-output11")
    if not playwright_dir.exists():
        print(f"❌ Playwright output directory not found: {playwright_dir}")
        print("   Please make sure the HTS download completed successfully.")
        return False
    
    # Check if we have timestamp directories
    timestamp_dirs = [d for d in playwright_dir.iterdir() 
                     if d.is_dir() and d.name.count('T') == 1 and d.name.count('Z') == 1]
    
    if len(timestamp_dirs) == 0:
        print(f"❌ No timestamp directories found in {playwright_dir}")
        return False
    
    print(f"✅ Found {len(timestamp_dirs)} timestamp directories")
    
    # Check for HTS data files
    sample_files = 0
    for ts_dir in timestamp_dirs[:5]:  # Check first 5
        csv_file = ts_dir / "htsdata.csv"
        if csv_file.exists():
            sample_files += 1
    
    if sample_files == 0:
        print("❌ No htsdata.csv files found in timestamp directories")
        return False
    
    print(f"✅ Found HTS data files in sample directories")
    return True

def main():
    """Main execution function."""
    print("🎯 HTS File Organization Workflow")
    print("This script will analyze and organize all downloaded HTS files")
    print()
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites not met. Exiting.")
        return
    
    # Create required directories
    os.makedirs("../analysis", exist_ok=True)
    print("✅ Created analysis directory")
    
    # Step 1: Analyze files
    success = run_script("analyze_hts_files.py", "ANALYZING HTS FILES")
    if not success:
        print("\n❌ Analysis failed. Cannot proceed with organization.")
        return
    
    # Step 2: Organize files
    success = run_script("organize_hts_files.py", "ORGANIZING HTS FILES")
    if not success:
        print("\n❌ Organization failed.")
        return
    
    # Final summary
    print(f"\n{'='*60}")
    print("🎉 HTS FILE ORGANIZATION COMPLETE!")
    print(f"{'='*60}")
    print()
    print("📁 Your files are now organized in:")
    print("   └── HTS/chapters/")
    print("       ├── chapter-01/")
    print("       ├── chapter-02/")
    print("       ├── ...")
    print("       └── chapter-97/")
    print()
    print("📊 Analysis results available in:")
    print("   └── HTS/analysis/")
    print("       ├── file_mapping.csv")
    print("       ├── file_mapping.json")
    print("       ├── analysis_summary.md")
    print("       └── organization_report.md")
    print()
    print("🎯 Next steps:")
    print("   1. Review the organization_report.md for any issues")
    print("   2. Verify your chapter files contain the expected data")
    print("   3. Begin your HTS analysis!")

if __name__ == "__main__":
    main()
