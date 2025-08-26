# Claude Code Prompt for HTS Database Development

## Project Overview
I need you to help me build a comprehensive Harmonized Tariff System (HTS) database management system that supports multiple countries and output formats. The system should handle the hierarchical nature of tariff codes from sections down to country-specific 12-digit codes.

## Project Structure
Create the following directory structure:
```
hts-database/
├── schema/
│   ├── markdown/
│   │   └── hts-schema.md
│   ├── sql/
│   │   ├── sqlite/
│   │   │   └── create_tables.sql
│   │   └── postgres/
│   │       └── create_tables.sql
├── data/
│   ├── raw/
│   │   └── mexico/
│   │       └── [source files]
│   ├── processed/
│   │   ├── csv/
│   │   ├── excel/
│   │   └── json/
├── scripts/
│   ├── parsers/
│   │   ├── parse_mexican_tariff.py
│   │   └── base_parser.py
│   ├── generators/
│   │   ├── generate_csv.py
│   │   ├── generate_excel.py
│   │   ├── generate_sqlite.py
│   │   └── generate_postgres.py
│   ├── validators/
│   │   └── validate_hierarchy.py
│   └── utils/
│       ├── code_formatter.py
│       └── data_cleaner.py
├── config/
│   └── database_config.yaml
├── tests/
│   ├── test_parsers.py
│   ├── test_validators.py
│   └── test_generators.py
├── docs/
│   ├── API.md
│   └── USAGE.md
├── requirements.txt
├── Makefile
└── README.md
```

## Development Tasks

### Task 1: Schema Implementation
1. Convert the markdown schema (I'll provide it) into:
   - SQLite DDL with proper constraints and indexes
   - PostgreSQL DDL with appropriate data types and performance optimizations
   - Python SQLAlchemy models for ORM support
   - JSON Schema for validation

2. Include in each implementation:
   - Foreign key constraints with proper CASCADE rules
   - Check constraints for data validation
   - Indexes for performance
   - Triggers for updated_at timestamps
   - Views for common queries

### Task 2: Parser Development
Create a flexible parser system in Python that can:

```python
class TariffParser:
    """
    Base parser class for different country formats
    Should handle:
    - Excel files (multiple sheets)
    - CSV files
    - JSON imports
    - PDF extraction (if needed)
    """
    
    def parse_hierarchy(self, file_path):
        """Extract hierarchical structure from source"""
        pass
    
    def validate_codes(self, data):
        """Ensure code format compliance"""
        pass
    
    def extract_rates(self, data):
        """Extract duty rates and conditions"""
        pass
    
    def map_to_schema(self, raw_data):
        """Map source data to our standardized schema"""
        pass
```

For the Mexican classification specifically, handle:
- Spanish to English translations
- NCM (Nomenclatura Común del Mercosur) to HTS mapping
- Special characters and accents
- Multiple duty rate columns
- Notes and restrictions

### Task 3: Database Generators
Create generator scripts for each format:

1. **CSV Generator**
   - Separate CSV file for each table
   - UTF-8 encoding with BOM for Excel compatibility
   - Proper escaping of special characters
   - Include a manifest.json with metadata

2. **Excel Generator**
   - Multi-sheet workbook with one sheet per table
   - Formatted headers and data validation
   - Dropdown lists for foreign keys
   - Conditional formatting for duty rates
   - Summary dashboard sheet

3. **SQLite Generator**
   - Single portable database file
   - Include sample queries as views
   - Add full-text search support
   - Create useful indexes
   - Include metadata table

4. **PostgreSQL Generator**
   - SQL dump file with proper sequences
   - Partitioning strategy for large tables
   - Include materialized views for performance
   - Add GIN indexes for text search
   - Create read-only user scripts

### Task 4: Data Validation System
Implement comprehensive validation:

```python
class HierarchyValidator:
    def validate_code_format(self, code, level):
        """Check code format matches expected pattern"""
        
    def validate_parent_exists(self, child_code, parent_table):
        """Ensure hierarchical integrity"""
        
    def validate_duty_rates(self, rates):
        """Check rate constraints and relationships"""
        
    def validate_date_ranges(self, dates):
        """Ensure no overlapping periods"""
        
    def generate_report(self):
        """Create validation report with issues"""
```

### Task 5: Utility Functions
Create helpful utilities:

1. **Code Formatter**
   - Add/remove padding zeros
   - Convert between different code formats
   - Generate code ranges
   - Create hierarchical paths

2. **Search Engine**
   - Fuzzy matching for product descriptions
   - Multi-language search support
   - Synonym handling
   - Search by keywords or code patterns

3. **Diff Tool**
   - Compare tariff versions
   - Track rate changes over time
   - Generate change reports
   - Migration scripts between versions

### Task 6: API Layer (Optional)
If useful, create a simple REST API:

```python
# FastAPI example endpoints
GET /api/sections
GET /api/chapters/{chapter_code}
GET /api/search?q={query}&country={country_code}
GET /api/tariff/{code}?country={country_code}
GET /api/duty-rates/{code}?date={effective_date}
POST /api/validate
POST /api/import
```

### Task 7: Documentation
Generate comprehensive documentation:

1. **README.md** with:
   - Quick start guide
   - Installation instructions
   - Basic usage examples
   - Architecture overview

2. **API.md** with:
   - Endpoint documentation
   - Request/response examples
   - Authentication details
   - Rate limiting info

3. **USAGE.md** with:
   - Common query examples
   - Import/export workflows
   - Troubleshooting guide
   - Performance tips

## Implementation Guidelines

### Code Style
- Use Python 3.8+ with type hints
- Follow PEP 8 style guide
- Add comprehensive docstrings
- Include logging throughout
- Handle errors gracefully

### Performance Considerations
- Use bulk inserts for large datasets
- Implement connection pooling
- Add progress bars for long operations
- Cache frequently accessed data
- Use async/await where beneficial

### Testing Requirements
- Unit tests for all parsers
- Integration tests for database operations
- Validation tests with edge cases
- Performance benchmarks
- Mock data generators for testing

## Configuration File Example
Create a `database_config.yaml`:

```yaml
databases:
  sqlite:
    path: "data/hts_database.db"
    journal_mode: "WAL"
    cache_size: -64000
    
  postgres:
    host: "localhost"
    port: 5432
    database: "hts_db"
    user: "hts_user"
    password: "${HTS_DB_PASSWORD}"
    pool_size: 20
    
parsers:
  mexico:
    source_encoding: "latin-1"
    date_format: "%d/%m/%Y"
    decimal_separator: ","
    thousand_separator: "."
    
  usa:
    source_encoding: "utf-8"
    date_format: "%m/%d/%Y"
    decimal_separator: "."
    thousand_separator: ","

export:
  csv:
    delimiter: ","
    encoding: "utf-8-sig"
    include_headers: true
    
  excel:
    engine: "openpyxl"
    freeze_panes: "B2"
    auto_filter: true
```

## Makefile Commands
Create these helpful commands:

```makefile
setup:
    pip install -r requirements.txt
    
parse-mexico:
    python scripts/parsers/parse_mexican_tariff.py data/raw/mexico/

validate:
    python scripts/validators/validate_hierarchy.py
    
generate-all: generate-csv generate-excel generate-sqlite generate-postgres

generate-csv:
    python scripts/generators/generate_csv.py
    
test:
    pytest tests/ -v --cov=scripts
    
clean:
    rm -rf data/processed/*
    rm -f *.log
```

## Sample Data for Testing
Include sample data for development:

```python
# Sample section
{
    "section_number": "I",
    "title_en": "Live animals; animal products",
    "title_es": "Animales vivos y productos del reino animal"
}

# Sample chapter
{
    "chapter_code": "01",
    "title_en": "Live animals",
    "title_es": "Animales vivos"
}

# Sample 8-digit Mexican code
{
    "tariff8_code": "01012101",
    "title_en": "Horses, purebred breeding",
    "title_es": "Caballos reproductores de raza pura",
    "duty_rate_general": 0.0,
    "duty_rate_mfn": 0.0
}
```

## Error Handling Strategy
Implement robust error handling:

1. Log all errors with context
2. Provide helpful error messages
3. Allow partial imports with error reports
4. Create rollback mechanisms
5. Validate before committing changes

## Questions to Address

Before starting, please:
1. Confirm the Mexican tariff file format you have
2. Specify priority countries for implementation
3. Indicate preferred Python packages/libraries
4. Define update frequency requirements
5. Specify any API integration needs

Start by implementing the base parser for the Mexican classification file, then we'll expand to other functionalities. Focus on modularity and reusability so we can easily add support for other countries' formats.