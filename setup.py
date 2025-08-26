#!/usr/bin/env python3
"""
HTS Database Setup Script
Automates the complete setup process for the HTS Database system
"""

import os
import sys
import subprocess
import sqlite3
from pathlib import Path

def print_status(message, status="INFO"):
    """Print formatted status message"""
    colors = {
        "INFO": "\033[94m",     # Blue
        "SUCCESS": "\033[92m",  # Green  
        "WARNING": "\033[93m",  # Yellow
        "ERROR": "\033[91m",    # Red
        "RESET": "\033[0m"      # Reset
    }
    print(f"{colors.get(status, '')}{status}: {message}{colors['RESET']}")

def check_python_version():
    """Check if Python version is compatible"""
    print_status("Checking Python version...")
    
    if sys.version_info < (3, 8):
        print_status("Python 3.8 or higher is required", "ERROR")
        return False
    
    print_status(f"Python {sys.version.split()[0]} - Compatible ✓", "SUCCESS")
    return True

def check_dependencies():
    """Check if required packages are available"""
    print_status("Checking dependencies...")
    
    required_packages = ['pandas', 'sqlite3', 'openpyxl']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print_status(f"  {package} ✓", "SUCCESS")
        except ImportError:
            missing_packages.append(package)
            print_status(f"  {package} ✗", "ERROR")
    
    if missing_packages:
        print_status(f"Missing packages: {', '.join(missing_packages)}", "WARNING")
        return False, missing_packages
    
    return True, []

def install_dependencies(packages):
    """Install missing dependencies"""
    print_status("Installing missing dependencies...")
    
    try:
        for package in packages:
            print_status(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print_status(f"  {package} installed ✓", "SUCCESS")
        return True
    except subprocess.CalledProcessError as e:
        print_status(f"Failed to install dependencies: {e}", "ERROR")
        return False

def verify_data_structure():
    """Verify that required data directories exist"""
    print_status("Verifying data structure...")
    
    required_dirs = [
        'chapters',
        'HTS', 
        'hts-local-database',
        'scripts',
        'docs'
    ]
    
    missing_dirs = []
    for dir_name in required_dirs:
        if not os.path.isdir(dir_name):
            missing_dirs.append(dir_name)
        else:
            print_status(f"  {dir_name}/ ✓", "SUCCESS")
    
    if missing_dirs:
        print_status(f"Missing directories: {', '.join(missing_dirs)}", "ERROR")
        return False
    
    # Count data files
    try:
        csv_files = len(list(Path('chapters').glob('*/chapter-*.csv')))
        json_files = len(list(Path('chapters').glob('*/chapter-*.json')))
        xlsx_files = len(list(Path('chapters').glob('*/chapter-*.xlsx')))
        
        print_status(f"  Data files: {csv_files} CSV, {json_files} JSON, {xlsx_files} XLSX", "INFO")
        
        if csv_files < 90:  # Should have ~95 files
            print_status("Warning: Missing chapter data files", "WARNING")
        
    except Exception as e:
        print_status(f"Could not count data files: {e}", "WARNING")
    
    return True

def setup_database():
    """Set up the SQLite database"""
    print_status("Setting up database...")
    
    db_path = 'hts-local-database'
    if not os.path.isdir(db_path):
        print_status("hts-local-database directory not found", "ERROR")
        return False
    
    # Change to database directory
    original_dir = os.getcwd()
    os.chdir(db_path)
    
    try:
        # Run database build script
        if os.path.exists('scripts/build_database.py'):
            print_status("Building database...")
            result = subprocess.run([sys.executable, 'scripts/build_database.py'], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print_status("Database built successfully ✓", "SUCCESS")
            else:
                print_status(f"Database build failed: {result.stderr}", "ERROR")
                return False
        else:
            print_status("Database build script not found", "ERROR")
            return False
        
        # Verify database
        if os.path.exists('database/hts.db'):
            # Check database size and basic structure
            db_size = os.path.getsize('database/hts.db') / (1024 * 1024)  # MB
            print_status(f"Database created: {db_size:.1f}MB ✓", "SUCCESS")
            
            # Quick database test
            try:
                conn = sqlite3.connect('database/hts.db')
                cursor = conn.cursor()
                
                # Count records in main tables
                cursor.execute("SELECT COUNT(*) FROM sections")
                sections_count = cursor.fetchone()[0]
                
                cursor.execute("SELECT COUNT(*) FROM chapters")
                chapters_count = cursor.fetchone()[0]
                
                conn.close()
                
                print_status(f"  Database contains: {sections_count} sections, {chapters_count} chapters ✓", "SUCCESS")
                
            except Exception as e:
                print_status(f"Database verification failed: {e}", "WARNING")
        
    except Exception as e:
        print_status(f"Database setup failed: {e}", "ERROR")
        return False
    finally:
        os.chdir(original_dir)
    
    return True

def test_installation():
    """Test the installation by running basic queries"""
    print_status("Testing installation...")
    
    try:
        # Change to database directory for testing
        sys.path.insert(0, 'hts-local-database')
        
        from utils.database import HTSDatabase
        
        db = HTSDatabase()
        
        # Test basic functionality
        sections = db.get_all_sections()
        print_status(f"  Loaded {len(sections)} sections ✓", "SUCCESS")
        
        chapters = db.get_all_chapters()
        print_status(f"  Loaded {len(chapters)} chapters ✓", "SUCCESS")
        
        # Test search functionality
        results = db.search_products("animals")
        print_status(f"  Search test: found {len(results)} results ✓", "SUCCESS")
        
        print_status("Installation test completed successfully ✓", "SUCCESS")
        return True
        
    except Exception as e:
        print_status(f"Installation test failed: {e}", "ERROR")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("🚢 HTS Database Setup")
    print("=" * 60)
    
    # Step 1: Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Step 2: Check dependencies
    deps_ok, missing_deps = check_dependencies()
    if not deps_ok:
        install_choice = input(f"Install missing dependencies ({', '.join(missing_deps)})? [Y/n]: ")
        if install_choice.lower() not in ['n', 'no']:
            if not install_dependencies(missing_deps):
                print_status("Failed to install dependencies", "ERROR")
                sys.exit(1)
        else:
            print_status("Cannot proceed without dependencies", "ERROR")
            sys.exit(1)
    
    # Step 3: Verify data structure  
    if not verify_data_structure():
        print_status("Data structure verification failed", "ERROR")
        sys.exit(1)
    
    # Step 4: Set up database
    if not setup_database():
        print_status("Database setup failed", "ERROR")
        sys.exit(1)
    
    # Step 5: Test installation
    if not test_installation():
        print_status("Installation test failed", "ERROR")
        sys.exit(1)
    
    # Success!
    print()
    print("=" * 60)
    print_status("🎉 Setup completed successfully!", "SUCCESS")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Read the documentation: docs/quick-start.md")
    print("2. Try some examples: docs/examples.md") 
    print("3. Explore the database: cd hts-local-database && python")
    print("   >>> from utils.database import HTSDatabase")
    print("   >>> db = HTSDatabase()")
    print("   >>> results = db.search_products('your search term')")
    print()

if __name__ == "__main__":
    main()