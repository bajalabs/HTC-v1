"""
Product Management utilities for the enhanced HTS database.
Handles product classification, search, and data management.
"""

import json
import sqlite3
import logging
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import re

logger = logging.getLogger(__name__)


class ProductManager:
    """Manages product data and classification in the HTS database."""
    
    def __init__(self, db_connection: sqlite3.Connection):
        self.conn = db_connection
        self.conn.row_factory = sqlite3.Row
    
    def add_product(self, product_data: Dict) -> int:
        """Add a new product to the database."""
        cursor = self.conn.cursor()
        
        # Validate required fields
        required_fields = ['product_name', 'subheading_code']
        for field in required_fields:
            if field not in product_data or not product_data[field]:
                raise ValueError(f"Required field '{field}' is missing or empty")
        
        # Get subheading_id from code
        cursor.execute("SELECT subheading_id FROM subheadings WHERE subheading_code = ?", 
                      (product_data['subheading_code'],))
        result = cursor.fetchone()
        if not result:
            raise ValueError(f"Subheading code {product_data['subheading_code']} not found")
        
        subheading_id = result[0]
        
        # Ensure JSON fields are properly formatted
        json_fields = ['brand_names', 'typical_uses', 'origin_countries', 'seasonal_availability', 
                      'hazard_classifications', 'certification_requirements', 'packaging_types']
        
        for field in json_fields:
            if field in product_data and isinstance(product_data[field], (list, dict)):
                product_data[field] = json.dumps(product_data[field])
        
        # Insert product
        cursor.execute("""
            INSERT INTO products (
                product_name, common_name, scientific_name, brand_names,
                subheading_id, category_id, description, technical_specs,
                typical_uses, origin_countries, seasonal_availability,
                shelf_life_days, storage_requirements, hazard_classifications,
                certification_requirements, packaging_types, unit_weight_kg,
                unit_dimensions, is_controlled, is_prohibited, confidence_score,
                data_sources
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            product_data.get('product_name'),
            product_data.get('common_name'),
            product_data.get('scientific_name'),
            product_data.get('brand_names'),
            subheading_id,
            product_data.get('category_id'),
            product_data.get('description'),
            product_data.get('technical_specs'),
            product_data.get('typical_uses'),
            product_data.get('origin_countries'),
            product_data.get('seasonal_availability'),
            product_data.get('shelf_life_days'),
            product_data.get('storage_requirements'),
            product_data.get('hazard_classifications'),
            product_data.get('certification_requirements'),
            product_data.get('packaging_types'),
            product_data.get('unit_weight_kg'),
            product_data.get('unit_dimensions'),
            product_data.get('is_controlled', 0),
            product_data.get('is_prohibited', 0),
            product_data.get('confidence_score', 1.0),
            product_data.get('data_sources')
        ))
        
        product_id = cursor.lastrowid
        self.conn.commit()
        
        logger.info(f"Added product '{product_data['product_name']}' with ID {product_id}")
        return product_id
    
    def search_products(self, query: str, filters: Dict = None, limit: int = 50) -> List[Dict]:
        """Search products using full-text search and filters."""
        cursor = self.conn.cursor()
        
        # Build search query
        search_conditions = []
        params = []
        
        if query:
            # Use FTS5 search
            search_conditions.append("""
                product_id IN (
                    SELECT record_id FROM search_index 
                    WHERE record_type = 'product' AND search_index MATCH ?
                )
            """)
            params.append(query)
        
        # Apply filters
        if filters:
            if 'subheading_code' in filters:
                search_conditions.append("sh.subheading_code = ?")
                params.append(filters['subheading_code'])
            
            if 'is_controlled' in filters:
                search_conditions.append("p.is_controlled = ?")
                params.append(filters['is_controlled'])
            
            if 'is_prohibited' in filters:
                search_conditions.append("p.is_prohibited = ?")
                params.append(filters['is_prohibited'])
            
            if 'origin_country' in filters:
                search_conditions.append("json_extract(p.origin_countries, '$[*]') LIKE ?")
                params.append(f"%{filters['origin_country']}%")
        
        where_clause = ""
        if search_conditions:
            where_clause = "WHERE " + " AND ".join(search_conditions)
        
        sql = f"""
            SELECT p.*, sh.subheading_code, sh.title_en as subheading_title,
                   c.chapter_code, c.title_en as chapter_title,
                   s.section_number, s.title_en as section_title
            FROM products p
            JOIN subheadings sh ON p.subheading_id = sh.subheading_id
            JOIN headings h ON sh.heading_id = h.heading_id
            JOIN chapters c ON h.chapter_id = c.chapter_id
            JOIN sections s ON c.section_id = s.section_id
            {where_clause}
            ORDER BY p.product_name
            LIMIT ?
        """
        params.append(limit)
        
        cursor.execute(sql, params)
        results = cursor.fetchall()
        
        return [dict(row) for row in results]
    
    def get_product_details(self, product_id: int) -> Optional[Dict]:
        """Get complete product details including classification hierarchy."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            SELECT * FROM v_products_complete WHERE product_id = ?
        """, (product_id,))
        
        result = cursor.fetchone()
        if not result:
            return None
        
        product = dict(result)
        
        # Get additional details
        # Product media
        cursor.execute("SELECT * FROM product_media WHERE product_id = ?", (product_id,))
        product['media'] = [dict(row) for row in cursor.fetchall()]
        
        # Product variations
        cursor.execute("SELECT * FROM product_variations WHERE product_id = ?", (product_id,))
        product['variations'] = [dict(row) for row in cursor.fetchall()]
        
        # Classification notes
        cursor.execute("""
            SELECT * FROM classification_notes 
            WHERE reference_type = 'product' AND reference_id = ?
            ORDER BY priority_level DESC, note_sequence
        """, (product_id,))
        product['notes'] = [dict(row) for row in cursor.fetchall()]
        
        return product
    
    def classify_product_by_description(self, description: str) -> List[Dict]:
        """Suggest HTS classifications based on product description."""
        cursor = self.conn.cursor()
        
        # Extract keywords from description
        keywords = self._extract_keywords(description)
        
        # Search across multiple levels
        suggestions = []
        
        # Search in products
        for keyword in keywords[:5]:  # Limit to top 5 keywords
            cursor.execute("""
                SELECT DISTINCT sh.subheading_code, sh.title_en, 
                       COUNT(*) as match_count,
                       'product_match' as match_type
                FROM products p
                JOIN subheadings sh ON p.subheading_id = sh.subheading_id
                WHERE p.product_name LIKE ? OR p.common_name LIKE ? OR p.description LIKE ?
                GROUP BY sh.subheading_id
                ORDER BY match_count DESC
                LIMIT 5
            """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
            
            suggestions.extend([dict(row) for row in cursor.fetchall()])
        
        # Search in subheadings directly
        query_terms = " ".join(keywords[:3])
        cursor.execute("""
            SELECT sh.subheading_code, sh.title_en, 
                   1.0 as match_count,
                   'classification_match' as match_type
            FROM subheadings sh
            WHERE sh.title_en MATCH ? OR sh.description MATCH ?
            LIMIT 10
        """, (query_terms, query_terms))
        
        suggestions.extend([dict(row) for row in cursor.fetchall()])
        
        # Remove duplicates and sort by relevance
        unique_suggestions = {}
        for suggestion in suggestions:
            code = suggestion['subheading_code']
            if code not in unique_suggestions or suggestion['match_count'] > unique_suggestions[code]['match_count']:
                unique_suggestions[code] = suggestion
        
        return list(unique_suggestions.values())[:10]
    
    def get_classification_guidance(self, subheading_code: str) -> Dict:
        """Get classification guidance for a specific subheading."""
        cursor = self.conn.cursor()
        
        # Get subheading details
        cursor.execute("""
            SELECT sh.*, h.heading_code, h.title_en as heading_title,
                   c.chapter_code, c.title_en as chapter_title,
                   s.section_number, s.title_en as section_title
            FROM subheadings sh
            JOIN headings h ON sh.heading_id = h.heading_id
            JOIN chapters c ON h.chapter_id = c.chapter_id
            JOIN sections s ON c.section_id = s.section_id
            WHERE sh.subheading_code = ?
        """, (subheading_code,))
        
        subheading = cursor.fetchone()
        if not subheading:
            return {}
        
        guidance = dict(subheading)
        
        # Get notes at all levels (section, chapter, heading, subheading)
        cursor.execute("""
            SELECT cn.*, 'section' as level FROM classification_notes cn
            JOIN sections s ON cn.reference_id = s.section_id
            WHERE cn.reference_type = 'section' AND s.section_number = ?
            UNION ALL
            SELECT cn.*, 'chapter' as level FROM classification_notes cn
            JOIN chapters c ON cn.reference_id = c.chapter_id
            WHERE cn.reference_type = 'chapter' AND c.chapter_code = ?
            UNION ALL
            SELECT cn.*, 'heading' as level FROM classification_notes cn
            JOIN headings h ON cn.reference_id = h.heading_id
            WHERE cn.reference_type = 'heading' AND h.heading_code = ?
            UNION ALL
            SELECT cn.*, 'subheading' as level FROM classification_notes cn
            WHERE cn.reference_type = 'subheading' AND cn.reference_id = ?
            ORDER BY level, priority_level DESC, note_sequence
        """, (guidance['section_number'], guidance['chapter_code'], 
              guidance['heading_code'], guidance['subheading_id']))
        
        guidance['notes'] = [dict(row) for row in cursor.fetchall()]
        
        # Get examples
        cursor.execute("""
            SELECT * FROM classification_examples 
            WHERE subheading_id = ?
            ORDER BY example_type, title
        """, (guidance['subheading_id'],))
        
        guidance['examples'] = [dict(row) for row in cursor.fetchall()]
        
        # Get sample products
        cursor.execute("""
            SELECT product_name, common_name, scientific_name, description
            FROM products 
            WHERE subheading_id = ?
            ORDER BY confidence_score DESC, product_name
            LIMIT 10
        """, (guidance['subheading_id'],))
        
        guidance['sample_products'] = [dict(row) for row in cursor.fetchall()]
        
        # Get alternative names
        cursor.execute("""
            SELECT alternative_name, name_type
            FROM alternative_names
            WHERE reference_type = 'subheading' AND reference_id = ?
            ORDER BY name_type, alternative_name
        """, (guidance['subheading_id'],))
        
        guidance['alternative_names'] = [dict(row) for row in cursor.fetchall()]
        
        return guidance
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract meaningful keywords from text."""
        # Simple keyword extraction - in production, use more sophisticated NLP
        
        # Remove common stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'shall', 'can'
        }
        
        # Clean and tokenize
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text.lower())
        words = text.split()
        
        # Filter out stop words and short words
        keywords = [word for word in words if len(word) > 2 and word not in stop_words]
        
        # Return unique keywords, sorted by frequency (simple count)
        word_counts = {}
        for word in keywords:
            word_counts[word] = word_counts.get(word, 0) + 1
        
        return sorted(word_counts.keys(), key=lambda x: word_counts[x], reverse=True)
    
    def add_product_media(self, product_id: int, media_data: Dict) -> int:
        """Add media (images, videos, documents) to a product."""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            INSERT INTO product_media (
                product_id, media_type, file_url, file_name, file_size_bytes,
                mime_type, caption, alt_text, is_primary, sort_order
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            product_id,
            media_data.get('media_type'),
            media_data.get('file_url'),
            media_data.get('file_name'),
            media_data.get('file_size_bytes'),
            media_data.get('mime_type'),
            media_data.get('caption'),
            media_data.get('alt_text'),
            media_data.get('is_primary', 0),
            media_data.get('sort_order', 0)
        ))
        
        media_id = cursor.lastrowid
        self.conn.commit()
        
        return media_id
    
    def bulk_import_products(self, products_data: List[Dict]) -> Dict:
        """Import multiple products in bulk."""
        results = {
            'success_count': 0,
            'error_count': 0,
            'errors': []
        }
        
        for i, product_data in enumerate(products_data):
            try:
                product_id = self.add_product(product_data)
                results['success_count'] += 1
                logger.debug(f"Added product {i+1}: {product_data.get('product_name')}")
                
            except Exception as e:
                results['error_count'] += 1
                error_info = {
                    'row_number': i + 1,
                    'product_name': product_data.get('product_name', 'Unknown'),
                    'error': str(e)
                }
                results['errors'].append(error_info)
                logger.error(f"Failed to add product {i+1}: {e}")
        
        logger.info(f"Bulk import completed: {results['success_count']} success, {results['error_count']} errors")
        return results


class NotesManager:
    """Manages classification notes, examples, and guidance."""
    
    def __init__(self, db_connection: sqlite3.Connection):
        self.conn = db_connection
        self.conn.row_factory = sqlite3.Row
    
    def add_note(self, note_data: Dict) -> int:
        """Add a classification note."""
        cursor = self.conn.cursor()
        
        # Get reference ID based on type
        reference_id = self._get_reference_id(note_data['reference_type'], note_data['reference_code'])
        if not reference_id:
            raise ValueError(f"Reference {note_data['reference_type']} {note_data['reference_code']} not found")
        
        cursor.execute("""
            INSERT INTO classification_notes (
                reference_type, reference_id, note_type, note_sequence, title,
                note_text, note_text_html, legal_reference, country_specific,
                language_code, effective_date, expiry_date, is_binding,
                priority_level, created_by
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            note_data['reference_type'],
            reference_id,
            note_data.get('note_type', 'general'),
            note_data.get('note_sequence', 1),
            note_data.get('title'),
            note_data['note_text'],
            note_data.get('note_text_html'),
            note_data.get('legal_reference'),
            note_data.get('country_specific'),
            note_data.get('language_code', 'en'),
            note_data.get('effective_date'),
            note_data.get('expiry_date'),
            note_data.get('is_binding', 0),
            note_data.get('priority_level', 1),
            note_data.get('created_by')
        ))
        
        note_id = cursor.lastrowid
        self.conn.commit()
        
        return note_id
    
    def _get_reference_id(self, reference_type: str, reference_code: str) -> Optional[int]:
        """Get reference ID for a given type and code."""
        cursor = self.conn.cursor()
        
        if reference_type == 'section':
            cursor.execute("SELECT section_id FROM sections WHERE section_number = ?", (reference_code,))
        elif reference_type == 'chapter':
            cursor.execute("SELECT chapter_id FROM chapters WHERE chapter_code = ?", (reference_code,))
        elif reference_type == 'heading':
            cursor.execute("SELECT heading_id FROM headings WHERE heading_code = ?", (reference_code,))
        elif reference_type == 'subheading':
            cursor.execute("SELECT subheading_id FROM subheadings WHERE subheading_code = ?", (reference_code,))
        else:
            return None
        
        result = cursor.fetchone()
        return result[0] if result else None