"""
Database utility functions for HTS database management.
"""

import sqlite3
import logging
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
import json

logger = logging.getLogger(__name__)


class HTSDatabase:
    """Database connection and utility class for HTS database."""
    
    def __init__(self, db_path: str = "database/hts.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._connection = None
    
    def connect(self) -> sqlite3.Connection:
        """Create or get database connection."""
        if self._connection is None:
            self._connection = sqlite3.connect(self.db_path)
            self._connection.execute("PRAGMA foreign_keys = ON")
            # Set row factory for dict-like access
            self._connection.row_factory = sqlite3.Row
        return self._connection
    
    def close(self):
        """Close database connection."""
        if self._connection:
            self._connection.close()
            self._connection = None
    
    def create_tables(self, schema_file: str = "schema/sql/sqlite/create_tables.sql"):
        """Create database tables from schema file."""
        schema_path = Path(schema_file)
        if not schema_path.exists():
            raise FileNotFoundError(f"Schema file not found: {schema_path}")
        
        conn = self.connect()
        try:
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = f.read()
            
            # Execute schema using executescript for better SQL parsing
            conn.executescript(schema)
            logger.info("Database tables created successfully")
            
        except Exception as e:
            logger.error(f"Failed to create tables: {e}")
            raise
    
    def insert_sections(self, sections: List[Dict]) -> int:
        """Insert sections data."""
        conn = self.connect()
        cursor = conn.cursor()
        
        inserted = 0
        for section in sections:
            try:
                cursor.execute("""
                    INSERT INTO sections (
                        section_number, section_range, title_en, title_short,
                        description, chapter_count, confidence_score, source_reference
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    section.get('section_number'),
                    section.get('section_range'),
                    section.get('title_en'),
                    section.get('title_short'),
                    section.get('description'),
                    section.get('chapter_count'),
                    section.get('confidence_score', 1.0),
                    section.get('source_reference', 'AI_generated')
                ))
                inserted += 1
            except sqlite3.Error as e:
                logger.error(f"Failed to insert section {section.get('section_number')}: {e}")
        
        conn.commit()
        logger.info(f"Inserted {inserted} sections")
        return inserted
    
    def insert_chapters(self, chapters: List[Dict]) -> int:
        """Insert chapters data."""
        conn = self.connect()
        cursor = conn.cursor()
        
        inserted = 0
        for chapter in chapters:
            try:
                # Get section_id from section_number
                section_id = self.get_section_id(chapter.get('section_number'))
                if not section_id:
                    logger.error(f"Section not found for chapter {chapter.get('chapter_code')}")
                    continue
                
                cursor.execute("""
                    INSERT INTO chapters (
                        section_id, chapter_code, title_en, title_short,
                        description, heading_count, general_notes,
                        confidence_score, source_reference
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    section_id,
                    chapter.get('chapter_code'),
                    chapter.get('title_en'),
                    chapter.get('title_short'),
                    chapter.get('description'),
                    chapter.get('heading_count'),
                    chapter.get('general_notes'),
                    chapter.get('confidence_score', 1.0),
                    chapter.get('source_reference', 'AI_generated')
                ))
                inserted += 1
            except sqlite3.Error as e:
                logger.error(f"Failed to insert chapter {chapter.get('chapter_code')}: {e}")
        
        conn.commit()
        logger.info(f"Inserted {inserted} chapters")
        return inserted
    
    def insert_headings(self, headings: List[Dict]) -> int:
        """Insert headings data."""
        conn = self.connect()
        cursor = conn.cursor()
        
        inserted = 0
        for heading in headings:
            try:
                # Get chapter_id from chapter_code
                chapter_code = heading.get('heading_code')[:2] if heading.get('heading_code') else None
                chapter_id = self.get_chapter_id(chapter_code)
                if not chapter_id:
                    logger.error(f"Chapter not found for heading {heading.get('heading_code')}")
                    continue
                
                cursor.execute("""
                    INSERT INTO headings (
                        chapter_id, heading_code, title_en, title_short,
                        description, subheading_count, is_residual,
                        confidence_score, source_reference
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    chapter_id,
                    heading.get('heading_code'),
                    heading.get('title_en'),
                    heading.get('title_short'),
                    heading.get('description'),
                    heading.get('subheading_count'),
                    heading.get('is_residual', False),
                    heading.get('confidence_score', 1.0),
                    heading.get('source_reference', 'AI_generated')
                ))
                inserted += 1
            except sqlite3.Error as e:
                logger.error(f"Failed to insert heading {heading.get('heading_code')}: {e}")
        
        conn.commit()
        logger.info(f"Inserted {inserted} headings")
        return inserted
    
    def insert_subheadings(self, subheadings: List[Dict]) -> int:
        """Insert subheadings data."""
        conn = self.connect()
        cursor = conn.cursor()
        
        inserted = 0
        for subheading in subheadings:
            try:
                # Get heading_id from heading_code
                heading_code = subheading.get('subheading_code')[:4] if subheading.get('subheading_code') else None
                heading_id = self.get_heading_id(heading_code)
                if not heading_id:
                    logger.error(f"Heading not found for subheading {subheading.get('subheading_code')}")
                    continue
                
                cursor.execute("""
                    INSERT INTO subheadings (
                        heading_id, subheading_code, title_en, title_short,
                        description, unit_of_quantity, is_leaf_node, is_residual,
                        confidence_score, source_reference
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    heading_id,
                    subheading.get('subheading_code'),
                    subheading.get('title_en'),
                    subheading.get('title_short'),
                    subheading.get('description'),
                    subheading.get('unit_of_quantity'),
                    subheading.get('is_leaf_node', True),
                    subheading.get('is_residual', False),
                    subheading.get('confidence_score', 1.0),
                    subheading.get('source_reference', 'AI_generated')
                ))
                inserted += 1
            except sqlite3.Error as e:
                logger.error(f"Failed to insert subheading {subheading.get('subheading_code')}: {e}")
        
        conn.commit()
        logger.info(f"Inserted {inserted} subheadings")
        return inserted
    
    def get_section_id(self, section_number: str) -> Optional[int]:
        """Get section ID by section number."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT section_id FROM sections WHERE section_number = ?", (section_number,))
        result = cursor.fetchone()
        return result[0] if result else None
    
    def get_chapter_id(self, chapter_code: str) -> Optional[int]:
        """Get chapter ID by chapter code."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT chapter_id FROM chapters WHERE chapter_code = ?", (chapter_code,))
        result = cursor.fetchone()
        return result[0] if result else None
    
    def get_heading_id(self, heading_code: str) -> Optional[int]:
        """Get heading ID by heading code."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT heading_id FROM headings WHERE heading_code = ?", (heading_code,))
        result = cursor.fetchone()
        return result[0] if result else None
    
    def count_records(self, table_name: str) -> int:
        """Count records in a table."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        return cursor.fetchone()[0]
    
    def get_statistics(self) -> Dict[str, int]:
        """Get database statistics."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM v_statistics")
        result = cursor.fetchone()
        
        if result:
            return dict(result)
        else:
            return {
                'total_sections': self.count_records('sections'),
                'total_chapters': self.count_records('chapters'),
                'total_headings': self.count_records('headings'),
                'total_subheadings': self.count_records('subheadings'),
                'total_countries': 0
            }
    
    def validate_hierarchy(self) -> List[Dict]:
        """Validate database hierarchy integrity."""
        issues = []
        conn = self.connect()
        cursor = conn.cursor()
        
        # Check for orphaned chapters
        cursor.execute("""
            SELECT c.chapter_code FROM chapters c
            LEFT JOIN sections s ON c.section_id = s.section_id
            WHERE s.section_id IS NULL
        """)
        orphaned_chapters = cursor.fetchall()
        if orphaned_chapters:
            issues.append({
                'type': 'orphaned_chapters',
                'count': len(orphaned_chapters),
                'items': [row[0] for row in orphaned_chapters]
            })
        
        # Check for orphaned headings
        cursor.execute("""
            SELECT h.heading_code FROM headings h
            LEFT JOIN chapters c ON h.chapter_id = c.chapter_id
            WHERE c.chapter_id IS NULL
        """)
        orphaned_headings = cursor.fetchall()
        if orphaned_headings:
            issues.append({
                'type': 'orphaned_headings',
                'count': len(orphaned_headings),
                'items': [row[0] for row in orphaned_headings]
            })
        
        # Check for orphaned subheadings
        cursor.execute("""
            SELECT sh.subheading_code FROM subheadings sh
            LEFT JOIN headings h ON sh.heading_id = h.heading_id
            WHERE h.heading_id IS NULL
        """)
        orphaned_subheadings = cursor.fetchall()
        if orphaned_subheadings:
            issues.append({
                'type': 'orphaned_subheadings',
                'count': len(orphaned_subheadings),
                'items': [row[0] for row in orphaned_subheadings]
            })
        
        return issues
    
    def backup_database(self, backup_path: str = None) -> str:
        """Create a backup of the database."""
        if backup_path is None:
            timestamp = int(time.time())
            backup_path = f"database/backups/hts_backup_{timestamp}.db"
        
        backup_path = Path(backup_path)
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        
        conn = self.connect()
        backup = sqlite3.connect(backup_path)
        conn.backup(backup)
        backup.close()
        
        logger.info(f"Database backed up to {backup_path}")
        return str(backup_path)