#!/usr/bin/env python3
"""
Main orchestrator script for building the comprehensive HTS database v2.
Includes products, notes, cross-references, and enhanced search capabilities.
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
from utils.product_manager import ProductManager, NotesManager
from utils.validation_engine import ValidationEngine
from scripts.populate_sections import main as populate_sections_main
from scripts.populate_chapters import main as populate_chapters_main
from scripts.populate_headings import main as populate_headings_main

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def print_banner():
    """Print startup banner for v2."""
    print()
    print("🚀 HTS Database Builder v2.0 - Comprehensive System")
    print("=" * 70)
    print("📊 Enhanced Target Statistics:")
    print("   • Sections:      21 (I-XXI)")
    print("   • Chapters:      97 (01-97, excluding 77)")
    print("   • Headings:      ~1,228 (4-digit codes)")
    print("   • Subheadings:   ~5,612 (6-digit codes)")
    print("   • Products:      Unlimited (with full details)")
    print("   • Notes:         Classification guidance & examples")
    print("   • Cross-refs:    Alternative names & mappings")
    print("   • Search:        Full-text search with FTS5")
    print("=" * 70)
    print("✨ New in v2: Products, Notes, Cross-references, Enhanced Search")
    print()


def create_database_structure():
    """Initialize the v2 database structure."""
    logger.info("📋 Initializing v2 database structure...")
    
    try:
        db = HTSDatabase()
        
        # Check if we need to run migration
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
        has_v2_tables = cursor.fetchone() is not None
        
        if not has_v2_tables:
            logger.info("🔄 V2 tables not found. Running migration...")
            from scripts.migrate_to_v2 import DatabaseMigrationV2
            migration = DatabaseMigrationV2()
            if not migration.run_migration():
                raise RuntimeError("Migration to v2 failed")
        else:
            logger.info("✅ V2 database structure already exists")
        
        return db
        
    except Exception as e:
        logger.error(f"❌ Failed to create database structure: {e}")
        raise


def populate_core_classification():
    """Populate the core classification hierarchy (sections → chapters → headings)."""
    logger.info("\n📚 PHASE 1: Core Classification Hierarchy")
    logger.info("-" * 50)
    
    stats = {}
    
    # Phase 1.1: Sections
    logger.info("📖 Phase 1.1: Sections")
    try:
        sections = populate_sections_main()
        stats['sections'] = len(sections)
        logger.info(f"✅ {stats['sections']} sections populated")
    except Exception as e:
        logger.error(f"❌ Sections population failed: {e}")
        stats['sections'] = 0
    
    # Phase 1.2: Chapters
    logger.info("📋 Phase 1.2: Chapters") 
    try:
        chapters = populate_chapters_main()
        stats['chapters'] = len(chapters)
        logger.info(f"✅ {stats['chapters']} chapters populated")
    except Exception as e:
        logger.error(f"❌ Chapters population failed: {e}")
        stats['chapters'] = 0
    
    # Phase 1.3: Headings
    logger.info("📄 Phase 1.3: Headings")
    try:
        headings = populate_headings_main()
        stats['headings'] = len(headings)
        logger.info(f"✅ {stats['headings']} headings populated")
    except Exception as e:
        logger.error(f"❌ Headings population failed: {e}")
        stats['headings'] = 0
    
    # Phase 1.4: Subheadings (placeholder for now)
    logger.info("📝 Phase 1.4: Subheadings")
    logger.info("⚠️  Subheadings population will be implemented in future versions")
    stats['subheadings'] = 0
    
    return stats


def populate_enhanced_data(db: HTSDatabase):
    """Populate enhanced data (products, notes, examples)."""
    logger.info("\n🔬 PHASE 2: Enhanced Data Population")
    logger.info("-" * 50)
    
    conn = db.connect()
    product_manager = ProductManager(conn)
    notes_manager = NotesManager(conn)
    
    stats = {}
    
    # Add sample products for demonstration
    logger.info("🏷️  Adding sample products...")
    
    sample_products = [
        {
            "product_name": "Fresh Whole Chicken",
            "common_name": "Chicken",
            "scientific_name": "Gallus gallus domesticus",
            "subheading_code": "0207",  # Using heading code since we don't have subheadings yet
            "description": "Fresh whole chicken, dressed weight, suitable for roasting or other cooking methods",
            "typical_uses": ["food", "cooking", "roasting", "grilling"],
            "origin_countries": ["US", "BR", "CN", "TH"],
            "storage_requirements": "Keep refrigerated at 0-4°C, use within 3-5 days",
            "shelf_life_days": 7,
            "unit_weight_kg": 1.5,
            "is_controlled": 0,
            "is_prohibited": 0,
            "confidence_score": 1.0
        },
        {
            "product_name": "Raw Honey",
            "common_name": "Honey",
            "description": "Pure, unprocessed honey from bee colonies, amber colored",
            "subheading_code": "0409",
            "typical_uses": ["food", "sweetener", "baking", "natural_remedy"],
            "origin_countries": ["NZ", "AR", "CN", "TR", "US"],
            "storage_requirements": "Store at room temperature in dry place, avoid direct sunlight",
            "shelf_life_days": 1095,  # 3 years
            "unit_weight_kg": 0.5,
            "packaging_types": ["jar", "squeeze_bottle", "bulk"],
            "is_controlled": 0,
            "is_prohibited": 0,
            "confidence_score": 1.0
        }
    ]
    
    # Try to add products using heading codes instead of subheading codes
    conn = db.connect()
    cursor = conn.cursor()
    products_added = 0
    
    for product_data in sample_products:
        try:
            # Try to find a heading that matches
            cursor.execute("SELECT heading_id FROM headings WHERE heading_code = ?", 
                          (product_data["subheading_code"],))
            result = cursor.fetchone()
            
            if result:
                # For demo purposes, create a dummy subheading entry
                cursor.execute("""
                    INSERT OR IGNORE INTO subheadings (
                        heading_id, subheading_code, title_en, description, 
                        is_leaf_node, confidence_score
                    ) VALUES (?, ?, ?, ?, 1, 1.0)
                """, (
                    result[0],
                    product_data["subheading_code"] + "00",  # Add 00 to make it 6 digits
                    product_data["product_name"] + " (auto-generated)",
                    "Auto-generated subheading for product classification"
                ))
                
                # Now add the product
                product_data["subheading_code"] = product_data["subheading_code"] + "00"
                product_id = product_manager.add_product(product_data)
                products_added += 1
                logger.info(f"   ✅ Added product: {product_data['product_name']}")
            else:
                logger.warning(f"   ⚠️  Heading {product_data['subheading_code']} not found, skipping {product_data['product_name']}")
                
        except Exception as e:
            logger.error(f"   ❌ Failed to add product {product_data['product_name']}: {e}")
    
    stats['products'] = products_added
    
    # Add sample notes
    logger.info("📝 Adding sample notes...")
    
    sample_notes = [
        {
            "reference_type": "heading",
            "reference_code": "0207",
            "note_type": "explanatory",
            "title": "Poultry Classification Guide",
            "note_text": "This heading covers meat and edible offal of domestic fowls (chickens), ducks, geese, turkeys, and guinea fowls, whether fresh, chilled, or frozen. Include whole birds, cuts, and giblets."
        },
        {
            "reference_type": "heading", 
            "reference_code": "0409",
            "note_type": "general",
            "title": "Natural Honey Definition",
            "note_text": "Natural honey is the natural sweet substance produced by honey bees from the nectar of plants or from secretions on plants. Must not contain added sweeteners or other substances."
        }
    ]
    
    notes_added = 0
    for note_data in sample_notes:
        try:
            note_id = notes_manager.add_note(note_data)
            notes_added += 1
            logger.info(f"   ✅ Added note: {note_data['title']}")
        except Exception as e:
            logger.error(f"   ❌ Failed to add note {note_data['title']}: {e}")
    
    stats['notes'] = notes_added
    
    return stats


def run_comprehensive_validation(db: HTSDatabase):
    """Run comprehensive validation on the database."""
    logger.info("\n✅ PHASE 3: Comprehensive Validation")
    logger.info("-" * 50)
    
    try:
        conn = db.connect()
        validator = ValidationEngine(conn)
        
        # Run full validation
        validation_results = validator.validate_all()
        
        # Generate and display report
        report = validator.generate_validation_report(validation_results)
        logger.info("📋 Validation Report:")
        print("\n" + report)
        
        # Save detailed results
        results_file = validator.save_validation_results(validation_results, "data/validation_results.json")
        logger.info(f"📁 Detailed results saved to: {results_file}")
        
        # Update quality scores
        validator.update_data_quality_scores(validation_results)
        
        return validation_results
        
    except Exception as e:
        logger.error(f"❌ Validation failed: {e}")
        return {'overall_status': 'error', 'summary': {'total_errors': 999}}


def update_search_system(db: HTSDatabase):
    """Update the enhanced search system."""
    logger.info("\n🔍 PHASE 4: Search System Update")
    logger.info("-" * 50)
    
    try:
        conn = db.connect()
        cursor = conn.cursor()
        
        # Clear and rebuild search index
        cursor.execute("DELETE FROM search_index")
        
        # Add classifications to search index
        cursor.execute("""
            INSERT INTO search_index (record_type, record_id, code, title_en, description)
            SELECT 'section', section_id, section_number, title_en, description
            FROM sections WHERE title_en IS NOT NULL
        """)
        
        cursor.execute("""
            INSERT INTO search_index (record_type, record_id, code, title_en, description)
            SELECT 'chapter', chapter_id, chapter_code, title_en, description
            FROM chapters WHERE title_en IS NOT NULL
        """)
        
        cursor.execute("""
            INSERT INTO search_index (record_type, record_id, code, title_en, description)
            SELECT 'heading', heading_id, heading_code, title_en, description
            FROM headings WHERE title_en IS NOT NULL
        """)
        
        cursor.execute("""
            INSERT INTO search_index (record_type, record_id, code, title_en, description)
            SELECT 'subheading', subheading_id, subheading_code, title_en, description
            FROM subheadings WHERE title_en IS NOT NULL
        """)
        
        # Add products to search index
        cursor.execute("""
            INSERT INTO search_index (record_type, record_id, code, title_en, description, product_names)
            SELECT 'product', p.product_id, sh.subheading_code, p.product_name, p.description,
                   p.product_name || ' ' || COALESCE(p.common_name, '') || ' ' || COALESCE(p.scientific_name, '')
            FROM products p
            JOIN subheadings sh ON p.subheading_id = sh.subheading_id
            WHERE p.product_name IS NOT NULL
        """)
        
        # Get count
        cursor.execute("SELECT COUNT(*) FROM search_index")
        search_records = cursor.fetchone()[0]
        
        conn.commit()
        logger.info(f"✅ Search index updated: {search_records:,} records")
        
        return search_records
        
    except Exception as e:
        logger.error(f"❌ Search update failed: {e}")
        return 0


def create_backup_and_export(db: HTSDatabase):
    """Create backup and export data."""
    logger.info("\n💾 PHASE 5: Backup & Export")
    logger.info("-" * 50)
    
    stats = {}
    
    try:
        # Create backup
        backup_path = db.backup_database()
        stats['backup_path'] = backup_path
        logger.info(f"✅ Backup created: {backup_path}")
        
        # Export basic CSV files
        conn = db.connect()
        cursor = conn.cursor()
        
        export_dir = Path("data/csv/core")
        export_dir.mkdir(parents=True, exist_ok=True)
        
        # Export core tables
        tables = ['sections', 'chapters', 'headings', 'subheadings', 'products']
        
        for table in tables:
            try:
                cursor.execute(f"SELECT * FROM {table}")
                rows = cursor.fetchall()
                
                if rows:
                    import csv
                    csv_file = export_dir / f"{table}.csv"
                    
                    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        # Write header
                        writer.writerow([description[0] for description in cursor.description])
                        # Write data
                        writer.writerows(rows)
                    
                    logger.info(f"   ✅ Exported {table}: {len(rows):,} records")
                else:
                    logger.info(f"   ⚠️  {table}: No records to export")
                    
            except Exception as e:
                logger.error(f"   ❌ Failed to export {table}: {e}")
        
        return stats
        
    except Exception as e:
        logger.error(f"❌ Backup/export failed: {e}")
        return {}


def print_comprehensive_summary(stats: dict):
    """Print comprehensive build summary."""
    print("\n" + "=" * 80)
    print("✅ COMPREHENSIVE HTS DATABASE v2.0 BUILD COMPLETE!")
    print("=" * 80)
    
    # Core classification stats
    print(f"📊 Core Classification Records:")
    print(f"   • Sections:     {stats.get('core_stats', {}).get('sections', 0):,}")
    print(f"   • Chapters:     {stats.get('core_stats', {}).get('chapters', 0):,}")
    print(f"   • Headings:     {stats.get('core_stats', {}).get('headings', 0):,}")
    print(f"   • Subheadings:  {stats.get('core_stats', {}).get('subheadings', 0):,}")
    
    # Enhanced data stats
    print(f"\n🔬 Enhanced Data Records:")
    print(f"   • Products:     {stats.get('enhanced_stats', {}).get('products', 0):,}")
    print(f"   • Notes:        {stats.get('enhanced_stats', {}).get('notes', 0):,}")
    print(f"   • Search Index: {stats.get('search_records', 0):,}")
    
    # Quality metrics
    validation = stats.get('validation_results', {})
    quality_score = validation.get('summary', {}).get('data_quality_score', 0.0)
    total_errors = validation.get('summary', {}).get('total_errors', 0)
    total_warnings = validation.get('summary', {}).get('total_warnings', 0)
    
    print(f"\n🔍 Quality Metrics:")
    print(f"   • Data Quality Score: {quality_score:.1%}")
    print(f"   • Validation Errors:  {total_errors}")
    print(f"   • Validation Warnings: {total_warnings}")
    print(f"   • Overall Status:     {validation.get('overall_status', 'unknown').upper()}")
    
    # System capabilities
    print(f"\n✨ System Capabilities:")
    print(f"   • Full-text search with FTS5")
    print(f"   • Product classification & management")
    print(f"   • Classification notes & examples")
    print(f"   • Alternative names & cross-references")
    print(f"   • Comprehensive validation engine")
    print(f"   • CSV export functionality")
    
    # Performance info
    print(f"\n⚡ Performance:")
    print(f"   • Build Duration:     {stats.get('duration', 'Unknown')}")
    
    if stats.get('backup_path'):
        print(f"   • Backup Location:    {Path(stats['backup_path']).name}")
    
    print(f"\n🎯 Next Steps:")
    print(f"   • Add more products via ProductManager API")
    print(f"   • Populate subheadings for complete HS6 coverage")
    print(f"   • Add country-specific tariff codes (8/10/12 digits)")
    print(f"   • Integrate with external APIs for live data")
    
    print("=" * 80)


def save_comprehensive_manifest(stats: dict):
    """Save comprehensive build manifest."""
    logger.info("📋 Saving comprehensive manifest...")
    
    core_stats = stats.get('core_stats', {})
    enhanced_stats = stats.get('enhanced_stats', {})
    validation = stats.get('validation_results', {})
    
    manifest = {
        "version": "2.0",
        "build_date": datetime.now().isoformat(),
        "hs_version": "2022",
        "database_type": "comprehensive",
        "core_classification": {
            "sections": core_stats.get('sections', 0),
            "chapters": core_stats.get('chapters', 0),
            "headings": core_stats.get('headings', 0),
            "subheadings": core_stats.get('subheadings', 0)
        },
        "enhanced_data": {
            "products": enhanced_stats.get('products', 0),
            "notes": enhanced_stats.get('notes', 0),
            "search_records": stats.get('search_records', 0)
        },
        "quality_metrics": {
            "data_quality_score": validation.get('summary', {}).get('data_quality_score', 0.0),
            "validation_errors": validation.get('summary', {}).get('total_errors', 0),
            "validation_warnings": validation.get('summary', {}).get('total_warnings', 0),
            "overall_status": validation.get('overall_status', 'unknown')
        },
        "build_info": {
            "duration": stats.get('duration', 'Unknown'),
            "backup_created": stats.get('backup_path') is not None,
            "features": [
                "full_text_search",
                "product_management", 
                "classification_notes",
                "validation_engine",
                "csv_export"
            ]
        }
    }
    
    manifest_path = Path("data/csv/manifest_v2.json")
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    logger.info(f"✅ Manifest saved to {manifest_path}")


def main():
    """Main comprehensive orchestrator function."""
    start_time = datetime.now()
    stats = {"start_time": start_time}
    
    try:
        # Print banner
        print_banner()
        
        # Phase 0: Database Setup
        logger.info("🔧 PHASE 0: Database Setup & Migration")
        logger.info("-" * 50)
        db = create_database_structure()
        
        # Phase 1: Core Classification
        stats['core_stats'] = populate_core_classification()
        
        # Phase 2: Enhanced Data
        stats['enhanced_stats'] = populate_enhanced_data(db)
        
        # Phase 3: Validation
        stats['validation_results'] = run_comprehensive_validation(db)
        
        # Phase 4: Search System
        stats['search_records'] = update_search_system(db)
        
        # Phase 5: Backup & Export
        backup_stats = create_backup_and_export(db)
        stats.update(backup_stats)
        
        # Calculate duration
        end_time = datetime.now()
        stats['end_time'] = end_time
        stats['duration'] = str(end_time - start_time)
        
        # Print comprehensive summary
        print_comprehensive_summary(stats)
        
        # Save manifest
        save_comprehensive_manifest(stats)
        
        logger.info("\n🎉 Comprehensive database build completed successfully!")
        
        return True
        
    except Exception as e:
        logger.error(f"\n💥 Build failed: {e}")
        stats['error'] = str(e)
        stats['end_time'] = datetime.now()
        stats['duration'] = str(stats['end_time'] - start_time)
        print_comprehensive_summary(stats)
        return False
    
    finally:
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)