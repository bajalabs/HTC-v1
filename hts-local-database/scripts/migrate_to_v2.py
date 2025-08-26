#!/usr/bin/env python3
"""
Database migration script to upgrade HTS Database from v1 to v2.
Adds comprehensive product system, notes, cross-references, and enhanced search.
"""

import sqlite3
import logging
import sys
import json
from pathlib import Path
from datetime import datetime
import shutil

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from utils.database import HTSDatabase

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DatabaseMigrationV2:
    """Handles migration from HTS Database v1 to v2."""
    
    def __init__(self, db_path: str = "database/hts.db"):
        self.db_path = Path(db_path)
        self.backup_path = None
        self.db = HTSDatabase(str(self.db_path))
        
    def create_backup(self) -> str:
        """Create a backup before migration."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = Path("database/backups")
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        self.backup_path = backup_dir / f"hts_v1_backup_{timestamp}.db"
        
        logger.info(f"Creating backup at {self.backup_path}")
        shutil.copy2(self.db_path, self.backup_path)
        logger.info("✅ Backup created successfully")
        
        return str(self.backup_path)
    
    def check_current_version(self) -> str:
        """Check the current database version."""
        conn = self.db.connect()
        cursor = conn.cursor()
        
        # Check if v2 tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
        if cursor.fetchone():
            return "v2"
        
        # Check if v1 tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sections'")
        if cursor.fetchone():
            return "v1"
        
        return "empty"
    
    def apply_v2_schema(self):
        """Apply the v2 enhanced schema."""
        logger.info("Applying v2 enhanced schema...")
        
        schema_path = Path("schema/sql/sqlite/enhanced_schema_v2.sql")
        if not schema_path.exists():
            raise FileNotFoundError(f"Enhanced schema file not found: {schema_path}")
        
        conn = self.db.connect()
        
        try:
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema_sql = f.read()
            
            # Execute schema modifications
            conn.executescript(schema_sql)
            conn.commit()
            
            logger.info("✅ v2 schema applied successfully")
            
        except Exception as e:
            logger.error(f"❌ Failed to apply v2 schema: {e}")
            conn.rollback()
            raise
    
    def populate_sample_products(self):
        """Add sample products to demonstrate the new system."""
        logger.info("Adding sample products...")
        
        sample_products = [
            {
                "product_name": "Fresh Atlantic Salmon",
                "common_name": "Atlantic Salmon",
                "scientific_name": "Salmo salar",
                "subheading_code": "030211",
                "description": "Fresh Atlantic salmon, whole fish or fillets, suitable for human consumption",
                "typical_uses": json.dumps(["food", "sashimi", "grilling", "baking"]),
                "origin_countries": json.dumps(["NO", "CA", "CL", "FO"]),
                "seasonal_availability": json.dumps({"peak_months": [6, 7, 8, 9], "available_year_round": True}),
                "storage_requirements": "Keep refrigerated at 0-4°C, use within 2-3 days of purchase",
                "unit_weight_kg": 2.5,
                "is_controlled": 0,
                "is_prohibited": 0
            },
            {
                "product_name": "Raw Cane Sugar",
                "common_name": "Sugar Cane",
                "scientific_name": "Saccharum officinarum",
                "subheading_code": "170111",
                "description": "Raw sugar derived from sugar cane, not refined, for food processing",
                "typical_uses": json.dumps(["food_processing", "refining", "industrial"]),
                "origin_countries": json.dumps(["BR", "IN", "TH", "AU", "MX"]),
                "shelf_life_days": 730,
                "storage_requirements": "Store in dry, cool place, protect from moisture",
                "is_controlled": 0,
                "is_prohibited": 0
            },
            {
                "product_name": "Wheat Flour, All-Purpose",
                "common_name": "All-Purpose Flour",
                "scientific_name": "Triticum aestivum",
                "subheading_code": "110100",
                "description": "Refined wheat flour suitable for baking and cooking",
                "typical_uses": json.dumps(["baking", "cooking", "food_production"]),
                "origin_countries": json.dumps(["US", "CA", "RU", "UA", "AU"]),
                "shelf_life_days": 365,
                "storage_requirements": "Store in cool, dry place, protect from insects and rodents",
                "packaging_types": json.dumps(["bags", "bulk", "containers"]),
                "unit_weight_kg": 25.0,
                "is_controlled": 0,
                "is_prohibited": 0
            },
            {
                "product_name": "Crude Petroleum Oil",
                "common_name": "Crude Oil",
                "subheading_code": "270900",
                "description": "Petroleum oils and oils obtained from bituminous minerals, crude",
                "typical_uses": json.dumps(["refining", "petrochemicals", "energy"]),
                "origin_countries": json.dumps(["SA", "RU", "US", "IR", "IQ"]),
                "hazard_classifications": json.dumps(["flammable", "environmental_hazard"]),
                "certification_requirements": json.dumps(["safety_data_sheet", "transport_permit"]),
                "is_controlled": 1,
                "is_prohibited": 0
            },
            {
                "product_name": "Cotton T-Shirts, Men's",
                "common_name": "Cotton T-Shirts",
                "subheading_code": "610910",
                "description": "Men's cotton t-shirts, knitted or crocheted, short-sleeved",
                "typical_uses": json.dumps(["clothing", "casual_wear", "workwear"]),
                "origin_countries": json.dumps(["BD", "VN", "CN", "IN", "TR"]),
                "packaging_types": json.dumps(["individual", "bulk", "hanging"]),
                "unit_dimensions": json.dumps({"length": 70, "width": 50, "height": 1, "unit": "cm"}),
                "is_controlled": 0,
                "is_prohibited": 0
            }
        ]
        
        conn = self.db.connect()
        cursor = conn.cursor()
        
        inserted_count = 0
        
        for product_data in sample_products:
            try:
                # Get subheading_id from code
                cursor.execute("SELECT subheading_id FROM subheadings WHERE subheading_code = ?", 
                              (product_data["subheading_code"],))
                result = cursor.fetchone()
                
                if result:
                    subheading_id = result[0]
                    
                    cursor.execute("""
                        INSERT INTO products (
                            product_name, common_name, scientific_name, subheading_id,
                            description, typical_uses, origin_countries, seasonal_availability,
                            shelf_life_days, storage_requirements, hazard_classifications,
                            certification_requirements, packaging_types, unit_weight_kg,
                            unit_dimensions, is_controlled, is_prohibited
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        product_data.get("product_name"),
                        product_data.get("common_name"),
                        product_data.get("scientific_name"),
                        subheading_id,
                        product_data.get("description"),
                        product_data.get("typical_uses"),
                        product_data.get("origin_countries"),
                        product_data.get("seasonal_availability"),
                        product_data.get("shelf_life_days"),
                        product_data.get("storage_requirements"),
                        product_data.get("hazard_classifications"),
                        product_data.get("certification_requirements"),
                        product_data.get("packaging_types"),
                        product_data.get("unit_weight_kg"),
                        product_data.get("unit_dimensions"),
                        product_data.get("is_controlled", 0),
                        product_data.get("is_prohibited", 0)
                    ))
                    inserted_count += 1
                else:
                    logger.warning(f"Subheading {product_data['subheading_code']} not found, skipping product {product_data['product_name']}")
                    
            except sqlite3.Error as e:
                logger.error(f"Failed to insert product {product_data.get('product_name')}: {e}")
        
        conn.commit()
        logger.info(f"✅ Added {inserted_count} sample products")
        
        return inserted_count
    
    def populate_sample_notes(self):
        """Add sample classification notes."""
        logger.info("Adding sample classification notes...")
        
        sample_notes = [
            {
                "reference_type": "section",
                "reference_code": "I",
                "note_type": "general",
                "title": "Section I Coverage",
                "note_text": "This section covers live animals and products obtained from them. It includes meat and edible meat offal, fish, dairy produce, eggs, honey, and other products of animal origin.",
                "priority_level": 1
            },
            {
                "reference_type": "chapter", 
                "reference_code": "03",
                "note_type": "explanatory",
                "title": "Fish Classification Rules",
                "note_text": "Fish are classified according to their species and processing state. Live fish are always classified in heading 0301, while dead fish are classified based on their preparation (fresh, frozen, dried, etc.).",
                "priority_level": 2
            },
            {
                "reference_type": "subheading",
                "reference_code": "030211",
                "note_type": "example",
                "title": "Atlantic Salmon Examples",
                "note_text": "Includes fresh Atlantic salmon (Salmo salar) whether whole, headed and gutted, or in fillets. Does not include smoked, salted, or otherwise preserved salmon.",
                "priority_level": 1
            }
        ]
        
        conn = self.db.connect()
        cursor = conn.cursor()
        
        inserted_count = 0
        
        for note in sample_notes:
            try:
                # Get reference ID based on type and code
                reference_id = None
                if note["reference_type"] == "section":
                    cursor.execute("SELECT section_id FROM sections WHERE section_number = ?", (note["reference_code"],))
                elif note["reference_type"] == "chapter":
                    cursor.execute("SELECT chapter_id FROM chapters WHERE chapter_code = ?", (note["reference_code"],))
                elif note["reference_type"] == "subheading":
                    cursor.execute("SELECT subheading_id FROM subheadings WHERE subheading_code = ?", (note["reference_code"],))
                
                result = cursor.fetchone()
                if result:
                    reference_id = result[0]
                    
                    cursor.execute("""
                        INSERT INTO classification_notes (
                            reference_type, reference_id, note_type, title, note_text, priority_level
                        ) VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        note["reference_type"],
                        reference_id,
                        note["note_type"],
                        note["title"],
                        note["note_text"],
                        note["priority_level"]
                    ))
                    inserted_count += 1
                else:
                    logger.warning(f"Reference {note['reference_type']} {note['reference_code']} not found")
                    
            except sqlite3.Error as e:
                logger.error(f"Failed to insert note: {e}")
        
        conn.commit()
        logger.info(f"✅ Added {inserted_count} sample notes")
        
        return inserted_count
    
    def populate_alternative_names(self):
        """Add alternative names and synonyms."""
        logger.info("Adding alternative names...")
        
        # Sample alternative names
        alt_names = [
            {"ref_type": "subheading", "ref_code": "030211", "alt_name": "Fresh Salmon", "name_type": "common"},
            {"ref_type": "subheading", "ref_code": "030211", "alt_name": "Atlantic Salmon Fillets", "name_type": "trade_name"},
            {"ref_type": "subheading", "ref_code": "170111", "alt_name": "Raw Sugar", "name_type": "common"},
            {"ref_type": "subheading", "ref_code": "170111", "alt_name": "Cane Sugar, Raw", "name_type": "trade_name"},
            {"ref_type": "chapter", "ref_code": "03", "alt_name": "Fisheries Products", "name_type": "common"},
            {"ref_type": "section", "ref_code": "I", "alt_name": "Animal Products", "name_type": "common"}
        ]
        
        conn = self.db.connect()
        cursor = conn.cursor()
        inserted_count = 0
        
        for alt_name in alt_names:
            try:
                # Get reference ID
                reference_id = None
                if alt_name["ref_type"] == "section":
                    cursor.execute("SELECT section_id FROM sections WHERE section_number = ?", (alt_name["ref_code"],))
                elif alt_name["ref_type"] == "chapter":
                    cursor.execute("SELECT chapter_id FROM chapters WHERE chapter_code = ?", (alt_name["ref_code"],))
                elif alt_name["ref_type"] == "subheading":
                    cursor.execute("SELECT subheading_id FROM subheadings WHERE subheading_code = ?", (alt_name["ref_code"],))
                
                result = cursor.fetchone()
                if result:
                    reference_id = result[0]
                    
                    cursor.execute("""
                        INSERT INTO alternative_names (
                            reference_type, reference_id, alternative_name, name_type
                        ) VALUES (?, ?, ?, ?)
                    """, (
                        alt_name["ref_type"],
                        reference_id,
                        alt_name["alt_name"],
                        alt_name["name_type"]
                    ))
                    inserted_count += 1
                    
            except sqlite3.Error as e:
                logger.error(f"Failed to insert alternative name: {e}")
        
        conn.commit()
        logger.info(f"✅ Added {inserted_count} alternative names")
        
        return inserted_count
    
    def update_search_index(self):
        """Populate the enhanced search index."""
        logger.info("Updating search index...")
        
        conn = self.db.connect()
        cursor = conn.cursor()
        
        # Clear existing search index
        cursor.execute("DELETE FROM search_index")
        
        # Add subheadings to search index
        cursor.execute("""
            INSERT INTO search_index (record_type, record_id, code, title_en, description)
            SELECT 'subheading', subheading_id, subheading_code, title_en, description
            FROM subheadings
            WHERE title_en IS NOT NULL
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
        
        conn.commit()
        logger.info("✅ Search index updated")
    
    def validate_migration(self) -> dict:
        """Validate the migration results."""
        logger.info("Validating migration...")
        
        conn = self.db.connect()
        cursor = conn.cursor()
        
        # Count records in new tables
        validation_results = {}
        
        new_tables = [
            'products', 'product_categories', 'product_media', 'product_variations',
            'classification_notes', 'classification_examples', 'classification_faq',
            'alternative_names', 'cross_references', 'external_mappings',
            'duty_rates', 'trade_restrictions', 'trade_agreements'
        ]
        
        for table in new_tables:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                validation_results[table] = count
            except sqlite3.Error as e:
                logger.warning(f"Could not count records in {table}: {e}")
                validation_results[table] = -1
        
        # Check search index
        cursor.execute("SELECT COUNT(*) FROM search_index")
        validation_results['search_index'] = cursor.fetchone()[0]
        
        logger.info("Validation results:")
        for table, count in validation_results.items():
            if count >= 0:
                logger.info(f"  • {table}: {count:,} records")
            else:
                logger.warning(f"  • {table}: Error counting records")
        
        return validation_results
    
    def run_migration(self):
        """Run the complete migration process."""
        logger.info("🚀 Starting HTS Database Migration v1 → v2")
        logger.info("=" * 60)
        
        try:
            # Check current version
            current_version = self.check_current_version()
            logger.info(f"Current database version: {current_version}")
            
            if current_version == "v2":
                logger.info("Database is already at v2. No migration needed.")
                return True
            
            if current_version == "empty":
                logger.error("Database is empty. Please run the initial population first.")
                return False
            
            # Create backup
            backup_path = self.create_backup()
            
            # Apply v2 schema
            self.apply_v2_schema()
            
            # Populate sample data
            products_added = self.populate_sample_products()
            notes_added = self.populate_sample_notes()
            alt_names_added = self.populate_alternative_names()
            
            # Update search index
            self.update_search_index()
            
            # Validate migration
            validation_results = self.validate_migration()
            
            # Summary
            logger.info("\n" + "=" * 60)
            logger.info("✅ MIGRATION COMPLETED SUCCESSFULLY!")
            logger.info("=" * 60)
            logger.info(f"📊 Migration Summary:")
            logger.info(f"   • Sample products added: {products_added}")
            logger.info(f"   • Sample notes added: {notes_added}")
            logger.info(f"   • Alternative names added: {alt_names_added}")
            logger.info(f"   • Search index records: {validation_results.get('search_index', 0):,}")
            logger.info(f"🔒 Backup location: {backup_path}")
            logger.info("=" * 60)
            
            return True
            
        except Exception as e:
            logger.error(f"💥 Migration failed: {e}")
            if self.backup_path:
                logger.info(f"💡 Restore from backup: {self.backup_path}")
            return False
        
        finally:
            self.db.close()


def main():
    """Main migration function."""
    migration = DatabaseMigrationV2()
    success = migration.run_migration()
    
    if success:
        print("\n🎉 Your HTS database has been successfully upgraded to v2!")
        print("   New features include products, notes, cross-references, and enhanced search.")
    else:
        print("\n❌ Migration failed. Check the logs above for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()