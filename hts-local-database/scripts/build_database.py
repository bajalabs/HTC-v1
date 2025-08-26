#!/usr/bin/env python3
"""
Main orchestrator script for building the complete HTS database.
Coordinates all phases of the AI-driven population process.
"""

import sqlite3
import logging
import sys
import json
from pathlib import Path
from datetime import datetime
import time

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.database import HTSDatabase
from scripts.populate_sections import main as populate_sections_main
from scripts.populate_chapters import main as populate_chapters_main

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def print_banner():
    """Print startup banner."""
    print()
    print("🚀 HTS Database Builder - AI-Driven Population")
    print("=" * 60)
    print("📊 Target Statistics:")
    print("   • Sections:     21 (I-XXI)")
    print("   • Chapters:     97 (01-97, excluding 77)")
    print("   • Headings:     ~1,228 (4-digit codes)")
    print("   • Subheadings:  ~5,612 (6-digit codes)")
    print("=" * 60)
    print()


def create_database_structure():
    """Initialize the database structure."""
    logger.info("📋 Initializing database structure...")
    
    try:
        db = HTSDatabase()
        db.create_tables()
        logger.info("✅ Database structure created successfully")
        return db
    except Exception as e:
        logger.error(f"❌ Failed to create database structure: {e}")
        raise


def populate_sections():
    """Populate the 21 HS sections."""
    logger.info("\n📚 PHASE 1: Populating Sections")
    logger.info("-" * 40)
    
    try:
        sections = populate_sections_main()
        logger.info(f"✅ Phase 1 complete: {len(sections)} sections populated")
        return len(sections)
    except Exception as e:
        logger.error(f"❌ Phase 1 failed: {e}")
        raise


def populate_chapters():
    """Populate the 97 HS chapters."""
    logger.info("\n📖 PHASE 2: Populating Chapters")
    logger.info("-" * 40)
    
    try:
        chapters = populate_chapters_main()
        logger.info(f"✅ Phase 2 complete: {len(chapters)} chapters populated")
        return len(chapters)
    except Exception as e:
        logger.error(f"❌ Phase 2 failed: {e}")
        raise


def populate_headings():
    """Populate the ~1,228 HS headings."""
    logger.info("\n📑 PHASE 3: Populating Headings")
    logger.info("-" * 40)
    
    logger.info("⚠️  Headings population not yet implemented")
    logger.info("    This phase will be implemented next")
    return 0


def populate_subheadings():
    """Populate the ~5,612 HS subheadings."""
    logger.info("\n📄 PHASE 4: Populating Subheadings")
    logger.info("-" * 40)
    
    logger.info("⚠️  Subheadings population not yet implemented")
    logger.info("    This phase will be implemented next")
    return 0


def validate_database(db: HTSDatabase):
    """Validate the database hierarchy and integrity."""
    logger.info("\n✅ PHASE 5: Validating Database")
    logger.info("-" * 40)
    
    try:
        # Get statistics
        stats = db.get_statistics()
        logger.info("📊 Current database statistics:")
        for table, count in stats.items():
            logger.info(f"   • {table.replace('total_', '').title()}: {count:,}")
        
        # Validate hierarchy
        issues = db.validate_hierarchy()
        if issues:
            logger.warning(f"⚠️  Found {len(issues)} validation issues:")
            for issue in issues:
                logger.warning(f"   • {issue['type']}: {issue['count']} items")
        else:
            logger.info("✅ No hierarchy issues found")
        
        return len(issues)
        
    except Exception as e:
        logger.error(f"❌ Validation failed: {e}")
        return -1


def create_backup(db: HTSDatabase):
    """Create a backup of the database."""
    logger.info("\n💾 Creating Database Backup")
    logger.info("-" * 40)
    
    try:
        backup_path = db.backup_database()
        logger.info(f"✅ Backup created: {backup_path}")
        return backup_path
    except Exception as e:
        logger.error(f"❌ Backup failed: {e}")
        return None


def print_summary(stats: dict):
    """Print build summary."""
    print("\n" + "=" * 60)
    print("✅ DATABASE BUILD SUMMARY")
    print("=" * 60)
    
    print(f"📊 Records Populated:")
    print(f"   • Sections:     {stats.get('sections', 0):,}")
    print(f"   • Chapters:     {stats.get('chapters', 0):,}")
    print(f"   • Headings:     {stats.get('headings', 0):,}")
    print(f"   • Subheadings:  {stats.get('subheadings', 0):,}")
    
    print(f"\n🔍 Quality Metrics:")
    print(f"   • Validation Issues: {stats.get('validation_issues', 0)}")
    print(f"   • Build Duration:    {stats.get('duration', 'Unknown')}")
    
    if stats.get('backup_path'):
        print(f"\n💾 Backup Location:")
        print(f"   • Path: {stats.get('backup_path')}")
    
    print(f"\n🎯 Completion Status:")
    total_target = 21 + 97 + 1228 + 5612  # Approximate targets
    total_actual = sum([
        stats.get('sections', 0),
        stats.get('chapters', 0), 
        stats.get('headings', 0),
        stats.get('subheadings', 0)
    ])
    completion_pct = (total_actual / total_target) * 100 if total_target > 0 else 0
    print(f"   • Progress: {completion_pct:.1f}% ({total_actual:,} of ~{total_target:,} records)")
    
    print("=" * 60)


def save_manifest(stats: dict):
    """Save build manifest file."""
    logger.info("📋 Saving build manifest...")
    
    manifest = {
        "version": "2.0",
        "build_date": datetime.now().isoformat(),
        "hs_version": "2022",
        "statistics": {
            "sections": stats.get('sections', 0),
            "chapters": stats.get('chapters', 0),
            "headings": stats.get('headings', 0),
            "subheadings": stats.get('subheadings', 0)
        },
        "build_info": {
            "duration": stats.get('duration', 'Unknown'),
            "validation_issues": stats.get('validation_issues', 0),
            "backup_created": stats.get('backup_path') is not None,
            "phases_completed": []
        }
    }
    
    # Determine completed phases
    if stats.get('sections', 0) > 0:
        manifest["build_info"]["phases_completed"].append("sections")
    if stats.get('chapters', 0) > 0:
        manifest["build_info"]["phases_completed"].append("chapters")
    if stats.get('headings', 0) > 0:
        manifest["build_info"]["phases_completed"].append("headings")
    if stats.get('subheadings', 0) > 0:
        manifest["build_info"]["phases_completed"].append("subheadings")
    
    # Save to file
    manifest_path = Path("data/csv/manifest.json")
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    logger.info(f"✅ Manifest saved to {manifest_path}")


def main():
    """Main orchestrator function."""
    start_time = datetime.now()
    stats = {"start_time": start_time}
    
    try:
        # Print banner
        print_banner()
        
        # Phase 0: Database Setup
        logger.info("🔧 PHASE 0: Database Setup")
        logger.info("-" * 40)
        db = create_database_structure()
        
        # Phase 1: Sections
        stats['sections'] = populate_sections()
        
        # Phase 2: Chapters  
        stats['chapters'] = populate_chapters()
        
        # Phase 3: Headings (placeholder)
        stats['headings'] = populate_headings()
        
        # Phase 4: Subheadings (placeholder)
        stats['subheadings'] = populate_subheadings()
        
        # Phase 5: Validation
        stats['validation_issues'] = validate_database(db)
        
        # Phase 6: Backup
        stats['backup_path'] = create_backup(db)
        
        # Calculate duration
        end_time = datetime.now()
        stats['end_time'] = end_time
        stats['duration'] = str(end_time - start_time)
        
        # Print summary
        print_summary(stats)
        
        # Save manifest
        save_manifest(stats)
        
        logger.info("\n🎉 Database build completed successfully!")
        
    except Exception as e:
        logger.error(f"\n💥 Build failed: {e}")
        stats['error'] = str(e)
        stats['end_time'] = datetime.now()
        stats['duration'] = str(stats['end_time'] - start_time)
        print_summary(stats)
        sys.exit(1)
    
    finally:
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    # Allow command line arguments for specific phases
    if len(sys.argv) > 1:
        if sys.argv[1] == "--sections":
            populate_sections()
        elif sys.argv[1] == "--chapters": 
            populate_chapters()
        elif sys.argv[1] == "--init":
            create_database_structure()
        elif sys.argv[1] == "--help":
            print("Usage: python build_database.py [--init|--sections|--chapters|--help]")
        else:
            main()
    else:
        main()