#!/usr/bin/env python3
"""
HTS Database Data Validator
Comprehensive validation tool for HTS data integrity and quality
"""

import os
import json
import pandas as pd
from pathlib import Path
import sqlite3
from datetime import datetime
import sys

class HTSDataValidator:
    """Validate HTS database for completeness and accuracy"""
    
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.chapters_dir = self.base_dir / "chapters" 
        self.hts_dir = self.base_dir / "HTS"
        self.db_path = self.base_dir / "hts-local-database" / "database" / "hts.db"
        self.errors = []
        self.warnings = []
        self.stats = {}
        
    def log_error(self, message):
        """Log an error"""
        self.errors.append(message)
        print(f"❌ ERROR: {message}")
    
    def log_warning(self, message):
        """Log a warning"""
        self.warnings.append(message)
        print(f"⚠️  WARNING: {message}")
    
    def log_info(self, message):
        """Log info message"""
        print(f"ℹ️  INFO: {message}")
    
    def log_success(self, message):
        """Log success message"""
        print(f"✅ SUCCESS: {message}")

    def validate_file_structure(self):
        """Validate basic file and directory structure"""
        self.log_info("Validating file structure...")
        
        # Check main directories
        required_dirs = [
            "chapters", "HTS", "hts-local-database", 
            "scripts", "docs", "analysis"
        ]
        
        for dir_name in required_dirs:
            dir_path = self.base_dir / dir_name
            if not dir_path.exists():
                self.log_error(f"Missing directory: {dir_name}")
            else:
                self.log_success(f"Directory exists: {dir_name}")
        
        # Check for essential files
        essential_files = [
            "README.md", "LICENSE", "CONTRIBUTING.md", 
            "setup.py", ".gitignore"
        ]
        
        for file_name in essential_files:
            file_path = self.base_dir / file_name
            if not file_path.exists():
                self.log_warning(f"Missing file: {file_name}")
            else:
                self.log_success(f"File exists: {file_name}")

    def validate_chapter_data(self):
        """Validate chapter data files"""
        self.log_info("Validating chapter data files...")
        
        if not self.chapters_dir.exists():
            self.log_error("Chapters directory not found")
            return
        
        chapter_stats = {
            'total_chapters': 0,
            'csv_files': 0,
            'json_files': 0,
            'xlsx_files': 0,
            'missing_files': [],
            'empty_files': [],
            'chapters_found': []
        }
        
        # Expected chapters (1-97, excluding 77, 85 typically)
        expected_chapters = set(range(1, 98)) - {77, 85}
        
        for chapter_dir in sorted(self.chapters_dir.glob("chapter-*")):
            if not chapter_dir.is_dir():
                continue
                
            chapter_num = self.extract_chapter_number(chapter_dir.name)
            if chapter_num:
                chapter_stats['chapters_found'].append(chapter_num)
                chapter_stats['total_chapters'] += 1
                
                # Check for required files
                csv_file = list(chapter_dir.glob("*.csv"))
                json_file = list(chapter_dir.glob("*.json"))
                xlsx_file = list(chapter_dir.glob("*.xlsx"))
                
                if csv_file:
                    chapter_stats['csv_files'] += 1
                    if self.is_file_empty(csv_file[0]):
                        chapter_stats['empty_files'].append(f"{chapter_dir.name}/CSV")
                else:
                    chapter_stats['missing_files'].append(f"{chapter_dir.name}/CSV")
                
                if json_file:
                    chapter_stats['json_files'] += 1
                    if self.is_file_empty(json_file[0]):
                        chapter_stats['empty_files'].append(f"{chapter_dir.name}/JSON")
                else:
                    chapter_stats['missing_files'].append(f"{chapter_dir.name}/JSON")
                
                if xlsx_file:
                    chapter_stats['xlsx_files'] += 1
                else:
                    chapter_stats['missing_files'].append(f"{chapter_dir.name}/XLSX")
        
        # Report findings
        self.log_info(f"Found {chapter_stats['total_chapters']} chapters")
        self.log_info(f"Files: {chapter_stats['csv_files']} CSV, {chapter_stats['json_files']} JSON, {chapter_stats['xlsx_files']} XLSX")
        
        # Check for missing chapters
        found_chapters = set(chapter_stats['chapters_found'])
        missing_chapters = expected_chapters - found_chapters
        
        if missing_chapters:
            self.log_warning(f"Missing chapters: {sorted(missing_chapters)}")
        
        # Check for missing files
        if chapter_stats['missing_files']:
            self.log_warning(f"Missing files: {len(chapter_stats['missing_files'])}")
            for missing in chapter_stats['missing_files'][:10]:  # Show first 10
                self.log_warning(f"  {missing}")
        
        # Check for empty files
        if chapter_stats['empty_files']:
            self.log_error(f"Empty files found: {chapter_stats['empty_files']}")
        
        self.stats['chapter_data'] = chapter_stats
        
        if not chapter_stats['missing_files'] and not chapter_stats['empty_files']:
            self.log_success("Chapter data validation passed")

    def validate_hts_structure(self):
        """Validate HTS sectional organization"""
        self.log_info("Validating HTS structure...")
        
        if not self.hts_dir.exists():
            self.log_error("HTS directory not found")
            return
        
        # Expected sections
        expected_sections = [f"Section_{['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI'][i]}" for i in range(21)]
        
        hts_stats = {
            'sections_found': 0,
            'chapters_in_hts': 0,
            'data_files_in_hts': 0,
            'missing_sections': [],
            'orphan_files': []
        }
        
        sections_found = []
        for item in self.hts_dir.iterdir():
            if item.is_dir() and item.name.startswith("Section_"):
                sections_found.append(item.name)
                hts_stats['sections_found'] += 1
                
                # Count chapters in each section
                for chapter_dir in item.glob("Chapter_*"):
                    if chapter_dir.is_dir():
                        hts_stats['chapters_in_hts'] += 1
                        
                        # Count data files
                        data_files = list(chapter_dir.glob("chapter-*.csv")) + list(chapter_dir.glob("chapter-*.json")) + list(chapter_dir.glob("chapter-*.xlsx"))
                        hts_stats['data_files_in_hts'] += len(data_files)
        
        self.log_info(f"HTS structure: {hts_stats['sections_found']} sections, {hts_stats['chapters_in_hts']} chapters, {hts_stats['data_files_in_hts']} data files")
        
        self.stats['hts_structure'] = hts_stats

    def validate_database(self):
        """Validate SQLite database"""
        self.log_info("Validating database...")
        
        if not self.db_path.exists():
            self.log_error(f"Database not found at {self.db_path}")
            return
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            db_stats = {
                'tables': {},
                'indexes': 0,
                'size_mb': os.path.getsize(self.db_path) / (1024 * 1024)
            }
            
            # Get table information
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            
            for (table_name,) in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                db_stats['tables'][table_name] = count
                
                self.log_info(f"  {table_name}: {count} records")
            
            # Check for indexes
            cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='index'")
            db_stats['indexes'] = cursor.fetchone()[0]
            
            # Test search functionality if available
            if 'products_fts' in db_stats['tables']:
                cursor.execute("SELECT COUNT(*) FROM products_fts WHERE products_fts MATCH 'animals'")
                search_results = cursor.fetchone()[0]
                self.log_info(f"  Search test: {search_results} results for 'animals'")
            
            conn.close()
            
            self.log_success(f"Database validation passed - {db_stats['size_mb']:.1f}MB, {sum(db_stats['tables'].values())} total records")
            self.stats['database'] = db_stats
            
        except Exception as e:
            self.log_error(f"Database validation failed: {e}")

    def validate_data_consistency(self):
        """Validate data consistency across formats"""
        self.log_info("Validating data consistency...")
        
        sample_chapters = [1, 10, 50, 84]  # Sample from different sections
        consistency_issues = []
        
        for chapter_num in sample_chapters:
            chapter_dir = self.chapters_dir / f"chapter-{chapter_num:02d}"
            if not chapter_dir.exists():
                continue
            
            csv_files = list(chapter_dir.glob("*.csv"))
            json_files = list(chapter_dir.glob("*.json"))
            
            if csv_files and json_files:
                try:
                    # Compare CSV and JSON data
                    csv_data = pd.read_csv(csv_files[0])
                    
                    with open(json_files[0], 'r') as f:
                        json_data = json.load(f)
                    
                    csv_rows = len(csv_data)
                    json_rows = len(json_data) if isinstance(json_data, list) else 1
                    
                    if abs(csv_rows - json_rows) > 5:  # Allow small discrepancies
                        consistency_issues.append(f"Chapter {chapter_num}: CSV has {csv_rows} rows, JSON has {json_rows} rows")
                    
                except Exception as e:
                    consistency_issues.append(f"Chapter {chapter_num}: Failed to compare formats - {e}")
        
        if consistency_issues:
            for issue in consistency_issues:
                self.log_warning(issue)
        else:
            self.log_success("Data consistency check passed")
        
        self.stats['consistency_issues'] = len(consistency_issues)

    def generate_report(self):
        """Generate validation report"""
        report = {
            'validation_date': datetime.now().isoformat(),
            'stats': self.stats,
            'errors': self.errors,
            'warnings': self.warnings,
            'summary': {
                'total_errors': len(self.errors),
                'total_warnings': len(self.warnings),
                'status': 'PASS' if len(self.errors) == 0 else 'FAIL'
            }
        }
        
        # Save detailed report
        report_path = self.base_dir / f"validation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Print summary
        print("\n" + "="*60)
        print("📊 VALIDATION SUMMARY")
        print("="*60)
        
        if self.stats.get('chapter_data'):
            cd = self.stats['chapter_data']
            print(f"📁 Chapter Data: {cd['total_chapters']} chapters, {cd['csv_files']} CSV files")
        
        if self.stats.get('hts_structure'):
            hs = self.stats['hts_structure']
            print(f"🏗️  HTS Structure: {hs['sections_found']} sections, {hs['chapters_in_hts']} chapters")
        
        if self.stats.get('database'):
            db = self.stats['database']
            print(f"🗄️  Database: {db['size_mb']:.1f}MB, {sum(db['tables'].values())} records")
        
        print(f"⚠️  Warnings: {len(self.warnings)}")
        print(f"❌ Errors: {len(self.errors)}")
        print(f"📊 Status: {report['summary']['status']}")
        
        print(f"\n📄 Detailed report saved: {report_path}")
        
        return report

    def extract_chapter_number(self, dir_name):
        """Extract chapter number from directory name"""
        try:
            # Extract number from chapter-XX format
            parts = dir_name.split('-')
            if len(parts) >= 2:
                return int(parts[1])
        except:
            pass
        return None
    
    def is_file_empty(self, file_path):
        """Check if file is empty or nearly empty"""
        try:
            return os.path.getsize(file_path) < 100  # Less than 100 bytes
        except:
            return True

def main():
    """Main validation function"""
    print("🔍 HTS Database Validation Tool")
    print("="*60)
    
    # Get base directory from command line or use current
    base_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    validator = HTSDataValidator(base_dir)
    
    # Run all validations
    validator.validate_file_structure()
    validator.validate_chapter_data()
    validator.validate_hts_structure()
    validator.validate_database()
    validator.validate_data_consistency()
    
    # Generate and save report
    report = validator.generate_report()
    
    # Exit with appropriate code
    exit_code = 0 if report['summary']['status'] == 'PASS' else 1
    sys.exit(exit_code)

if __name__ == "__main__":
    main()