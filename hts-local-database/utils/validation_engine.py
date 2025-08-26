"""
Comprehensive validation engine for the HTS database.
Validates data quality, integrity, and business rules.
"""

import sqlite3
import json
import re
import logging
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime, date
from pathlib import Path

logger = logging.getLogger(__name__)


class ValidationEngine:
    """Comprehensive validation engine for HTS database."""
    
    def __init__(self, db_connection: sqlite3.Connection):
        self.conn = db_connection
        self.conn.row_factory = sqlite3.Row
        self.validation_rules = self._load_validation_rules()
    
    def _load_validation_rules(self) -> List[Dict]:
        """Load validation rules from database and built-in rules."""
        cursor = self.conn.cursor()
        
        # Get custom rules from database
        try:
            cursor.execute("SELECT * FROM validation_rules WHERE is_active = 1")
            custom_rules = [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error:
            custom_rules = []
        
        # Built-in validation rules
        builtin_rules = [
            {
                'rule_name': 'valid_section_number',
                'table_name': 'sections',
                'column_name': 'section_number',
                'rule_type': 'format',
                'rule_expression': r'^(I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV|XVI|XVII|XVIII|XIX|XX|XXI)$',
                'error_message': 'Section number must be valid Roman numeral I-XXI',
                'severity': 'error'
            },
            {
                'rule_name': 'valid_chapter_code',
                'table_name': 'chapters',
                'column_name': 'chapter_code',
                'rule_type': 'format',
                'rule_expression': r'^\d{2}$',
                'error_message': 'Chapter code must be 2 digits',
                'severity': 'error'
            },
            {
                'rule_name': 'valid_heading_code',
                'table_name': 'headings',
                'column_name': 'heading_code',
                'rule_type': 'format',
                'rule_expression': r'^\d{4}$',
                'error_message': 'Heading code must be 4 digits',
                'severity': 'error'
            },
            {
                'rule_name': 'valid_subheading_code',
                'table_name': 'subheadings',
                'column_name': 'subheading_code',
                'rule_type': 'format',
                'rule_expression': r'^\d{6}$',
                'error_message': 'Subheading code must be 6 digits',
                'severity': 'error'
            },
            {
                'rule_name': 'no_chapter_77',
                'table_name': 'chapters',
                'column_name': 'chapter_code',
                'rule_type': 'logic',
                'rule_expression': 'chapter_code != "77"',
                'error_message': 'Chapter 77 is reserved and should not be used',
                'severity': 'error'
            },
            {
                'rule_name': 'confidence_score_range',
                'table_name': 'products',
                'column_name': 'confidence_score',
                'rule_type': 'range',
                'rule_expression': '0.0 <= confidence_score <= 1.0',
                'error_message': 'Confidence score must be between 0.0 and 1.0',
                'severity': 'warning'
            },
            {
                'rule_name': 'valid_json_format',
                'table_name': 'products',
                'column_name': 'typical_uses',
                'rule_type': 'json_format',
                'rule_expression': 'valid_json',
                'error_message': 'Typical uses must be valid JSON array',
                'severity': 'warning'
            }
        ]
        
        return builtin_rules + custom_rules
    
    def validate_all(self) -> Dict[str, Any]:
        """Run comprehensive validation on entire database."""
        logger.info("Starting comprehensive database validation...")
        
        validation_results = {
            'timestamp': datetime.now().isoformat(),
            'overall_status': 'passed',
            'summary': {
                'total_errors': 0,
                'total_warnings': 0,
                'total_checks': 0,
                'data_quality_score': 0.0
            },
            'table_results': {},
            'detailed_issues': []
        }
        
        # Core table validations
        tables_to_validate = ['sections', 'chapters', 'headings', 'subheadings', 'products']
        
        for table in tables_to_validate:
            table_results = self._validate_table(table)
            validation_results['table_results'][table] = table_results
            validation_results['summary']['total_errors'] += table_results['error_count']
            validation_results['summary']['total_warnings'] += table_results['warning_count']
            validation_results['summary']['total_checks'] += table_results['check_count']
            validation_results['detailed_issues'].extend(table_results['issues'])
        
        # Relationship validations
        relationship_results = self._validate_relationships()
        validation_results['table_results']['relationships'] = relationship_results
        validation_results['summary']['total_errors'] += relationship_results['error_count']
        validation_results['summary']['total_warnings'] += relationship_results['warning_count']
        
        # Business rule validations
        business_results = self._validate_business_rules()
        validation_results['table_results']['business_rules'] = business_results
        validation_results['summary']['total_errors'] += business_results['error_count']
        validation_results['summary']['total_warnings'] += business_results['warning_count']
        
        # Calculate overall data quality score
        total_issues = validation_results['summary']['total_errors'] + validation_results['summary']['total_warnings']
        if validation_results['summary']['total_checks'] > 0:
            validation_results['summary']['data_quality_score'] = max(0.0, 1.0 - (total_issues / validation_results['summary']['total_checks']))
        
        # Set overall status
        if validation_results['summary']['total_errors'] > 0:
            validation_results['overall_status'] = 'failed'
        elif validation_results['summary']['total_warnings'] > 0:
            validation_results['overall_status'] = 'passed_with_warnings'
        
        logger.info(f"Validation completed: {validation_results['overall_status']}")
        logger.info(f"Errors: {validation_results['summary']['total_errors']}, "
                   f"Warnings: {validation_results['summary']['total_warnings']}")
        
        return validation_results
    
    def _validate_table(self, table_name: str) -> Dict[str, Any]:
        """Validate a specific table."""
        logger.debug(f"Validating table: {table_name}")
        
        result = {
            'table_name': table_name,
            'error_count': 0,
            'warning_count': 0,
            'check_count': 0,
            'record_count': 0,
            'issues': []
        }
        
        cursor = self.conn.cursor()
        
        # Get record count
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        result['record_count'] = cursor.fetchone()[0]
        
        if result['record_count'] == 0:
            return result
        
        # Apply relevant validation rules
        table_rules = [rule for rule in self.validation_rules if rule['table_name'] == table_name]
        
        for rule in table_rules:
            try:
                issues = self._apply_validation_rule(rule)
                result['issues'].extend(issues)
                result['check_count'] += 1
                
                for issue in issues:
                    if issue['severity'] == 'error':
                        result['error_count'] += 1
                    elif issue['severity'] == 'warning':
                        result['warning_count'] += 1
                        
            except Exception as e:
                logger.error(f"Error applying rule {rule['rule_name']}: {e}")
        
        return result
    
    def _apply_validation_rule(self, rule: Dict) -> List[Dict]:
        """Apply a single validation rule."""
        issues = []
        cursor = self.conn.cursor()
        
        table = rule['table_name']
        column = rule['column_name']
        rule_type = rule['rule_type']
        expression = rule['rule_expression']
        
        try:
            if rule_type == 'format':
                # Regex format validation
                cursor.execute(f"SELECT rowid, {column} FROM {table} WHERE {column} IS NOT NULL")
                rows = cursor.fetchall()
                
                pattern = re.compile(expression)
                for row in rows:
                    if not pattern.match(str(row[1])):
                        issues.append({
                            'rule_name': rule['rule_name'],
                            'severity': rule['severity'],
                            'table_name': table,
                            'record_id': row[0],
                            'column_name': column,
                            'current_value': row[1],
                            'error_message': rule['error_message']
                        })
            
            elif rule_type == 'range':
                # Range validation
                if 'confidence_score' in expression:
                    cursor.execute(f"SELECT rowid, {column} FROM {table} WHERE {column} IS NOT NULL AND NOT ({expression})")
                    rows = cursor.fetchall()
                    
                    for row in rows:
                        issues.append({
                            'rule_name': rule['rule_name'],
                            'severity': rule['severity'],
                            'table_name': table,
                            'record_id': row[0],
                            'column_name': column,
                            'current_value': row[1],
                            'error_message': rule['error_message']
                        })
            
            elif rule_type == 'logic':
                # Logic validation
                cursor.execute(f"SELECT rowid, {column} FROM {table} WHERE NOT ({expression})")
                rows = cursor.fetchall()
                
                for row in rows:
                    issues.append({
                        'rule_name': rule['rule_name'],
                        'severity': rule['severity'],
                        'table_name': table,
                        'record_id': row[0],
                        'column_name': column,
                        'current_value': row[1],
                        'error_message': rule['error_message']
                    })
            
            elif rule_type == 'json_format':
                # JSON format validation
                cursor.execute(f"SELECT rowid, {column} FROM {table} WHERE {column} IS NOT NULL")
                rows = cursor.fetchall()
                
                for row in rows:
                    try:
                        if row[1]:
                            json.loads(row[1])
                    except (json.JSONDecodeError, TypeError):
                        issues.append({
                            'rule_name': rule['rule_name'],
                            'severity': rule['severity'],
                            'table_name': table,
                            'record_id': row[0],
                            'column_name': column,
                            'current_value': row[1],
                            'error_message': rule['error_message']
                        })
                        
        except Exception as e:
            logger.error(f"Error in rule {rule['rule_name']}: {e}")
            
        return issues
    
    def _validate_relationships(self) -> Dict[str, Any]:
        """Validate foreign key relationships and hierarchy integrity."""
        result = {
            'error_count': 0,
            'warning_count': 0,
            'check_count': 0,
            'issues': []
        }
        
        cursor = self.conn.cursor()
        
        # Check for orphaned chapters
        cursor.execute("""
            SELECT c.rowid, c.chapter_code, c.section_id
            FROM chapters c
            LEFT JOIN sections s ON c.section_id = s.section_id
            WHERE s.section_id IS NULL
        """)
        orphaned_chapters = cursor.fetchall()
        
        for row in orphaned_chapters:
            result['issues'].append({
                'rule_name': 'orphaned_chapter',
                'severity': 'error',
                'table_name': 'chapters',
                'record_id': row[0],
                'column_name': 'section_id',
                'current_value': row[2],
                'error_message': f'Chapter {row[1]} references non-existent section_id {row[2]}'
            })
            result['error_count'] += 1
        
        result['check_count'] += 1
        
        # Check for orphaned headings
        cursor.execute("""
            SELECT h.rowid, h.heading_code, h.chapter_id
            FROM headings h
            LEFT JOIN chapters c ON h.chapter_id = c.chapter_id
            WHERE c.chapter_id IS NULL
        """)
        orphaned_headings = cursor.fetchall()
        
        for row in orphaned_headings:
            result['issues'].append({
                'rule_name': 'orphaned_heading',
                'severity': 'error',
                'table_name': 'headings',
                'record_id': row[0],
                'column_name': 'chapter_id',
                'current_value': row[2],
                'error_message': f'Heading {row[1]} references non-existent chapter_id {row[2]}'
            })
            result['error_count'] += 1
        
        result['check_count'] += 1
        
        # Check for orphaned subheadings
        cursor.execute("""
            SELECT sh.rowid, sh.subheading_code, sh.heading_id
            FROM subheadings sh
            LEFT JOIN headings h ON sh.heading_id = h.heading_id
            WHERE h.heading_id IS NULL
        """)
        orphaned_subheadings = cursor.fetchall()
        
        for row in orphaned_subheadings:
            result['issues'].append({
                'rule_name': 'orphaned_subheading',
                'severity': 'error',
                'table_name': 'subheadings',
                'record_id': row[0],
                'column_name': 'heading_id',
                'current_value': row[2],
                'error_message': f'Subheading {row[1]} references non-existent heading_id {row[2]}'
            })
            result['error_count'] += 1
        
        result['check_count'] += 1
        
        # Check code hierarchy consistency
        cursor.execute("""
            SELECT h.rowid, h.heading_code, c.chapter_code
            FROM headings h
            JOIN chapters c ON h.chapter_id = c.chapter_id
            WHERE SUBSTR(h.heading_code, 1, 2) != c.chapter_code
        """)
        inconsistent_headings = cursor.fetchall()
        
        for row in inconsistent_headings:
            result['issues'].append({
                'rule_name': 'heading_code_mismatch',
                'severity': 'error',
                'table_name': 'headings',
                'record_id': row[0],
                'column_name': 'heading_code',
                'current_value': row[1],
                'error_message': f'Heading code {row[1]} does not match chapter code {row[2]}'
            })
            result['error_count'] += 1
        
        result['check_count'] += 1
        
        cursor.execute("""
            SELECT sh.rowid, sh.subheading_code, h.heading_code
            FROM subheadings sh
            JOIN headings h ON sh.heading_id = h.heading_id
            WHERE SUBSTR(sh.subheading_code, 1, 4) != h.heading_code
        """)
        inconsistent_subheadings = cursor.fetchall()
        
        for row in inconsistent_subheadings:
            result['issues'].append({
                'rule_name': 'subheading_code_mismatch',
                'severity': 'error',
                'table_name': 'subheadings',
                'record_id': row[0],
                'column_name': 'subheading_code',
                'current_value': row[1],
                'error_message': f'Subheading code {row[1]} does not match heading code {row[2]}'
            })
            result['error_count'] += 1
        
        result['check_count'] += 1
        
        return result
    
    def _validate_business_rules(self) -> Dict[str, Any]:
        """Validate business-specific rules."""
        result = {
            'error_count': 0,
            'warning_count': 0,
            'check_count': 0,
            'issues': []
        }
        
        cursor = self.conn.cursor()
        
        # Check for duplicate codes
        cursor.execute("""
            SELECT section_number, COUNT(*) as count
            FROM sections
            GROUP BY section_number
            HAVING COUNT(*) > 1
        """)
        duplicate_sections = cursor.fetchall()
        
        for row in duplicate_sections:
            result['issues'].append({
                'rule_name': 'duplicate_section_number',
                'severity': 'error',
                'table_name': 'sections',
                'record_id': None,
                'column_name': 'section_number',
                'current_value': row[0],
                'error_message': f'Section number {row[0]} appears {row[1]} times'
            })
            result['error_count'] += 1
        
        result['check_count'] += 1
        
        # Check for missing descriptions
        cursor.execute("SELECT COUNT(*) FROM products WHERE description IS NULL OR description = ''")
        missing_product_descriptions = cursor.fetchone()[0]
        
        if missing_product_descriptions > 0:
            result['issues'].append({
                'rule_name': 'missing_product_descriptions',
                'severity': 'warning',
                'table_name': 'products',
                'record_id': None,
                'column_name': 'description',
                'current_value': None,
                'error_message': f'{missing_product_descriptions} products are missing descriptions'
            })
            result['warning_count'] += 1
        
        result['check_count'] += 1
        
        # Check for products without proper scientific names
        try:
            cursor.execute("""
                SELECT COUNT(*) FROM products 
                WHERE (scientific_name IS NULL OR scientific_name = '') 
                AND product_name NOT LIKE '%manufactured%' 
                AND product_name NOT LIKE '%processed%'
            """)
            missing_scientific_names = cursor.fetchone()[0]
            
            if missing_scientific_names > 0:
                result['issues'].append({
                    'rule_name': 'missing_scientific_names',
                    'severity': 'warning',
                    'table_name': 'products',
                    'record_id': None,
                    'column_name': 'scientific_name',
                    'current_value': None,
                    'error_message': f'{missing_scientific_names} natural products are missing scientific names'
                })
                result['warning_count'] += 1
            
            result['check_count'] += 1
            
        except sqlite3.Error:
            # Products table may not exist yet
            pass
        
        return result
    
    def generate_validation_report(self, validation_results: Dict) -> str:
        """Generate a human-readable validation report."""
        report = []
        
        report.append("=" * 80)
        report.append("HTS DATABASE VALIDATION REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {validation_results['timestamp']}")
        report.append(f"Overall Status: {validation_results['overall_status'].upper()}")
        report.append(f"Data Quality Score: {validation_results['summary']['data_quality_score']:.2%}")
        report.append("")
        
        # Summary
        summary = validation_results['summary']
        report.append("SUMMARY")
        report.append("-" * 40)
        report.append(f"Total Checks: {summary['total_checks']}")
        report.append(f"Errors: {summary['total_errors']}")
        report.append(f"Warnings: {summary['total_warnings']}")
        report.append("")
        
        # Table-by-table results
        report.append("TABLE VALIDATION RESULTS")
        report.append("-" * 40)
        
        for table_name, table_result in validation_results['table_results'].items():
            status_icon = "✅" if table_result['error_count'] == 0 else "❌"
            warning_icon = "⚠️ " if table_result['warning_count'] > 0 else ""
            
            report.append(f"{status_icon} {warning_icon}{table_name.upper()}")
            
            if 'record_count' in table_result:
                report.append(f"   Records: {table_result['record_count']:,}")
            
            report.append(f"   Errors: {table_result['error_count']}")
            report.append(f"   Warnings: {table_result['warning_count']}")
            
            if table_result['error_count'] > 0 or table_result['warning_count'] > 0:
                report.append("   Issues:")
                for issue in table_result['issues']:
                    severity_icon = "🔴" if issue['severity'] == 'error' else "🟡"
                    report.append(f"     {severity_icon} {issue['error_message']}")
            
            report.append("")
        
        # Detailed issues
        if validation_results['detailed_issues']:
            report.append("DETAILED ISSUES")
            report.append("-" * 40)
            
            for issue in validation_results['detailed_issues'][:20]:  # Limit to first 20
                severity_icon = "🔴" if issue['severity'] == 'error' else "🟡"
                report.append(f"{severity_icon} {issue['table_name']}.{issue['column_name']}")
                report.append(f"   Rule: {issue['rule_name']}")
                report.append(f"   Message: {issue['error_message']}")
                if issue['record_id']:
                    report.append(f"   Record ID: {issue['record_id']}")
                if issue['current_value']:
                    report.append(f"   Current Value: {issue['current_value']}")
                report.append("")
            
            if len(validation_results['detailed_issues']) > 20:
                report.append(f"... and {len(validation_results['detailed_issues']) - 20} more issues")
                report.append("")
        
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def save_validation_results(self, validation_results: Dict, output_path: str = None) -> str:
        """Save validation results to file."""
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"validation_report_{timestamp}.json"
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(validation_results, f, indent=2, ensure_ascii=False, default=str)
        
        logger.info(f"Validation results saved to {output_file}")
        return str(output_file)
    
    def update_data_quality_scores(self, validation_results: Dict):
        """Update data quality scores in the database."""
        cursor = self.conn.cursor()
        
        try:
            # Calculate scores by table
            for table_name, table_result in validation_results['table_results'].items():
                if 'record_count' in table_result and table_result['record_count'] > 0:
                    total_issues = table_result['error_count'] + table_result['warning_count']
                    total_checks = table_result['check_count'] * table_result['record_count']
                    
                    if total_checks > 0:
                        completeness_score = max(0.0, 1.0 - (total_issues / total_checks))
                        accuracy_score = max(0.0, 1.0 - (table_result['error_count'] / total_checks))
                        overall_score = (completeness_score + accuracy_score) / 2
                    else:
                        completeness_score = accuracy_score = overall_score = 1.0
                    
                    # Update or insert quality score
                    cursor.execute("""
                        INSERT OR REPLACE INTO data_quality_scores (
                            record_type, record_id, completeness_score, accuracy_score,
                            consistency_score, freshness_score, overall_score,
                            validation_errors, last_validated, validation_method
                        ) VALUES (?, 0, ?, ?, 1.0, 1.0, ?, ?, ?, 'automated_validation')
                    """, (
                        table_name,
                        completeness_score,
                        accuracy_score,
                        overall_score,
                        json.dumps([issue['error_message'] for issue in table_result['issues']]),
                        datetime.now().isoformat()
                    ))
            
            self.conn.commit()
            logger.info("Data quality scores updated")
            
        except Exception as e:
            logger.error(f"Failed to update data quality scores: {e}")


def main():
    """Standalone validation script."""
    import sys
    sys.path.append(str(Path(__file__).parent.parent))
    
    from utils.database import HTSDatabase
    
    # Run validation
    db = HTSDatabase()
    conn = db.connect()
    
    validator = ValidationEngine(conn)
    results = validator.validate_all()
    
    # Generate and display report
    report = validator.generate_validation_report(results)
    print(report)
    
    # Save results
    results_file = validator.save_validation_results(results)
    print(f"\nDetailed results saved to: {results_file}")
    
    # Update quality scores
    validator.update_data_quality_scores(results)
    
    db.close()
    
    # Exit with appropriate code
    if results['overall_status'] == 'failed':
        sys.exit(1)
    elif results['overall_status'] == 'passed_with_warnings':
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()