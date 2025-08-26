# Local-First Harmonized Tariff System Database Schema
Version 2.0 | AI-Driven Population Strategy

## Overview
A simplified, local-first database design focusing on the internationally standardized HS6 structure (Sections → Chapters → Headings → Subheadings) that can be populated via AI agents. Country-specific extensions will be added in Phase 2.

## Database Statistics (HS 2022)
- **Sections**: 21 (I-XXI)
- **Chapters**: 97 (01-97, with 77 reserved)
- **Headings**: ~1,228 (4-digit codes)
- **Subheadings**: ~5,612 (6-digit codes)

## Phase 1: Core International Tables (AI-Populated)

### 1. sections
The 21 major sections of the HS classification
```sql
CREATE TABLE sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_number TEXT NOT NULL UNIQUE,  -- "I", "II", ... "XXI"
    section_range TEXT NOT NULL,          -- "01-05", "06-14", etc.
    title_en TEXT NOT NULL,
    title_short TEXT,                     -- Abbreviated title for UI
    description TEXT,
    chapter_count INTEGER,                -- Number of chapters in section
    ai_generated BOOLEAN DEFAULT 1,       -- Track AI-generated content
    confidence_score REAL DEFAULT 1.0,    -- AI confidence in data
    source_reference TEXT,                -- Source used for generation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CSV format: section_number,section_range,title_en,title_short,description,chapter_count
```

### 2. chapters  
The 97 chapters (01-97, excluding 77)
```sql
CREATE TABLE chapters (
    chapter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_id INTEGER NOT NULL,
    chapter_code TEXT NOT NULL UNIQUE,    -- "01", "02", ... "97"
    title_en TEXT NOT NULL,
    title_short TEXT,                     -- Abbreviated title
    description TEXT,
    heading_count INTEGER,                -- Number of headings in chapter
    general_notes TEXT,                   -- Chapter-specific rules
    ai_generated BOOLEAN DEFAULT 1,
    confidence_score REAL DEFAULT 1.0,
    source_reference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (section_id) REFERENCES sections(section_id)
);

-- CSV format: chapter_code,section_number,title_en,title_short,description,heading_count
```

### 3. headings
The ~1,228 4-digit headings
```sql
CREATE TABLE headings (
    heading_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INTEGER NOT NULL,
    heading_code TEXT NOT NULL UNIQUE,    -- "0101", "0102", ... "9706"
    title_en TEXT NOT NULL,
    title_short TEXT,
    description TEXT,
    subheading_count INTEGER,             -- Number of subheadings
    is_residual BOOLEAN DEFAULT 0,       -- True for "Other" categories
    ai_generated BOOLEAN DEFAULT 1,
    confidence_score REAL DEFAULT 1.0,
    source_reference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id)
);

-- CSV format: heading_code,chapter_code,title_en,title_short,description,subheading_count,is_residual
```

### 4. subheadings
The ~5,612 6-digit subheadings (internationally harmonized)
```sql
CREATE TABLE subheadings (
    subheading_id INTEGER PRIMARY KEY AUTOINCREMENT,
    heading_id INTEGER NOT NULL,
    subheading_code TEXT NOT NULL UNIQUE,  -- "010121", "010129", etc.
    title_en TEXT NOT NULL,
    title_short TEXT,
    description TEXT,
    unit_of_quantity TEXT,                 -- "kg", "u", "m²", etc.
    is_leaf_node BOOLEAN DEFAULT 0,        -- True if no further subdivision
    is_residual BOOLEAN DEFAULT 0,         -- True for "Other" categories
    ai_generated BOOLEAN DEFAULT 1,
    confidence_score REAL DEFAULT 1.0,
    source_reference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (heading_id) REFERENCES headings(heading_id)
);

-- CSV format: subheading_code,heading_code,title_en,title_short,description,unit_of_quantity,is_leaf_node,is_residual
```

## Phase 1.5: AI Enhancement Tables

### 5. ai_extraction_log
Track AI agent extraction process
```sql
CREATE TABLE ai_extraction_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    extraction_batch TEXT NOT NULL,        -- Batch identifier
    table_name TEXT NOT NULL,              -- Which table was populated
    extraction_method TEXT,                -- "gpt4", "claude", "web_scrape", etc.
    records_extracted INTEGER,
    records_validated INTEGER,
    validation_errors INTEGER,
    extraction_prompt TEXT,                -- Prompt used for extraction
    raw_response TEXT,                     -- Store raw AI response
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 6. keywords_search
AI-generated keywords for better search
```sql
CREATE TABLE keywords_search (
    keyword_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code_level TEXT NOT NULL,              -- "section", "chapter", "heading", "subheading"
    code_value TEXT NOT NULL,              -- The actual code
    keyword TEXT NOT NULL,
    keyword_type TEXT,                     -- "primary", "synonym", "related"
    language TEXT DEFAULT 'en',
    relevance_score REAL DEFAULT 0.5,      -- 0.0 to 1.0
    ai_generated BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_keyword_search ON keywords_search(keyword);
CREATE INDEX idx_keyword_code ON keywords_search(code_value);

-- CSV format: code_level,code_value,keyword,keyword_type,language,relevance_score
```

### 7. validation_rules
AI-generated validation rules for data quality
```sql
CREATE TABLE validation_rules (
    rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_name TEXT NOT NULL,
    table_name TEXT NOT NULL,
    column_name TEXT,
    rule_type TEXT NOT NULL,              -- "format", "range", "reference", "logic"
    rule_expression TEXT NOT NULL,        -- SQL or regex expression
    error_message TEXT,
    severity TEXT DEFAULT 'warning',      -- "error", "warning", "info"
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Phase 2: Country Extensions (API-Populated)

### 8. countries
Registry for country-specific implementations
```sql
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_code TEXT NOT NULL UNIQUE,     -- ISO 3166-1 alpha-2
    country_name TEXT NOT NULL,
    classification_system TEXT,            -- "HTS", "CN", "TARIC", etc.
    api_endpoint TEXT,                     -- API URL for data fetching
    api_key_required BOOLEAN DEFAULT 0,
    max_digits INTEGER,                    -- 8, 10, or 12
    last_sync_date DATE,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 9. country_classifications
Country-specific 8+ digit codes (dynamically structured)
```sql
CREATE TABLE country_classifications (
    classification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL,
    parent_code TEXT NOT NULL,             -- 6-digit subheading code
    full_code TEXT NOT NULL,               -- 8, 10, or 12-digit code
    code_level INTEGER NOT NULL,           -- 8, 10, or 12
    title_en TEXT,
    title_local TEXT,
    duty_rate TEXT,                        -- Store as JSON for multiple rates
    unit_of_quantity TEXT,
    restrictions TEXT,                     -- JSON array of restrictions
    effective_from DATE,
    effective_to DATE,
    api_source TEXT,                       -- Track data source
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

CREATE UNIQUE INDEX idx_country_code ON country_classifications(country_id, full_code);
CREATE INDEX idx_parent_code ON country_classifications(parent_code);
```

## SQLite Specific Features

### Full-Text Search Setup
```sql
-- Create FTS5 virtual table for searching
CREATE VIRTUAL TABLE search_index USING fts5(
    code,
    title_en,
    description,
    keywords,
    content=subheadings,
    content_rowid=subheading_id
);

-- Populate search index
INSERT INTO search_index (code, title_en, description)
SELECT subheading_code, title_en, description FROM subheadings;
```

### Useful Views

```sql
-- Complete hierarchy view
CREATE VIEW v_complete_hierarchy AS
SELECT 
    s.section_number,
    s.title_en as section_title,
    c.chapter_code,
    c.title_en as chapter_title,
    h.heading_code,
    h.title_en as heading_title,
    sh.subheading_code,
    sh.title_en as subheading_title,
    sh.unit_of_quantity
FROM sections s
JOIN chapters c ON s.section_id = c.section_id
JOIN headings h ON c.chapter_id = h.chapter_id
JOIN subheadings sh ON h.heading_id = sh.heading_id
ORDER BY sh.subheading_code;

-- Statistics view
CREATE VIEW v_statistics AS
SELECT 
    (SELECT COUNT(*) FROM sections) as total_sections,
    (SELECT COUNT(*) FROM chapters) as total_chapters,
    (SELECT COUNT(*) FROM headings) as total_headings,
    (SELECT COUNT(*) FROM subheadings) as total_subheadings,
    (SELECT COUNT(DISTINCT country_id) FROM country_classifications) as total_countries;

-- AI confidence view
CREATE VIEW v_ai_confidence AS
SELECT 
    'sections' as table_name,
    AVG(confidence_score) as avg_confidence,
    MIN(confidence_score) as min_confidence,
    COUNT(*) as total_records
FROM sections
UNION ALL
SELECT 'chapters', AVG(confidence_score), MIN(confidence_score), COUNT(*) FROM chapters
UNION ALL
SELECT 'headings', AVG(confidence_score), MIN(confidence_score), COUNT(*) FROM headings
UNION ALL
SELECT 'subheadings', AVG(confidence_score), MIN(confidence_score), COUNT(*) FROM subheadings;
```

### Triggers for Data Integrity

```sql
-- Auto-update timestamps
CREATE TRIGGER update_sections_timestamp 
AFTER UPDATE ON sections
BEGIN
    UPDATE sections SET updated_at = CURRENT_TIMESTAMP WHERE section_id = NEW.section_id;
END;

-- Validate chapter codes
CREATE TRIGGER validate_chapter_code
BEFORE INSERT ON chapters
BEGIN
    SELECT CASE
        WHEN LENGTH(NEW.chapter_code) != 2 THEN
            RAISE(ABORT, 'Chapter code must be 2 digits')
        WHEN NEW.chapter_code = '77' THEN
            RAISE(ABORT, 'Chapter 77 is reserved')
    END;
END;

-- Validate heading codes match chapter
CREATE TRIGGER validate_heading_code
BEFORE INSERT ON headings
BEGIN
    SELECT CASE
        WHEN LENGTH(NEW.heading_code) != 4 THEN
            RAISE(ABORT, 'Heading code must be 4 digits')
        WHEN NOT EXISTS (
            SELECT 1 FROM chapters 
            WHERE chapter_code = SUBSTR(NEW.heading_code, 1, 2) 
            AND chapter_id = NEW.chapter_id
        ) THEN
            RAISE(ABORT, 'Heading code must match chapter code')
    END;
END;
```

## CSV File Structure

### Directory Layout
```
data/
├── csv/
│   ├── core/
│   │   ├── sections.csv
│   │   ├── chapters.csv
│   │   ├── headings.csv
│   │   └── subheadings.csv
│   ├── enhanced/
│   │   ├── keywords_search.csv
│   │   └── validation_rules.csv
│   ├── countries/
│   │   ├── countries.csv
│   │   └── {country_code}/
│   │       └── classifications.csv
│   └── manifest.json
```

### Manifest File Structure
```json
{
    "version": "2.0",
    "generated_date": "2024-01-01T00:00:00Z",
    "hs_version": "2022",
    "statistics": {
        "sections": 21,
        "chapters": 97,
        "headings": 1228,
        "subheadings": 5612
    },
    "ai_generation": {
        "model": "claude-3",
        "confidence_threshold": 0.95,
        "validation_passes": 3
    },
    "files": [
        {
            "name": "sections.csv",
            "rows": 21,
            "checksum": "md5_hash_here"
        }
    ]
}
```

## Data Quality Metrics

### Completeness Check
```sql
SELECT 
    'Missing Descriptions' as issue,
    COUNT(*) as count
FROM subheadings 
WHERE description IS NULL OR description = '';
```

### Hierarchy Validation
```sql
-- Find orphaned headings
SELECT h.heading_code 
FROM headings h
LEFT JOIN chapters c ON c.chapter_id = h.chapter_id
WHERE c.chapter_id IS NULL;

-- Find broken code patterns
SELECT subheading_code 
FROM subheadings
WHERE subheading_code NOT LIKE heading_code || '__';
```

## Migration Path

### From CSV to SQLite
```python
import pandas as pd
import sqlite3

def import_csv_to_sqlite(csv_path, db_path):
    conn = sqlite3.connect(db_path)
    
    # Import each core table
    for table in ['sections', 'chapters', 'headings', 'subheadings']:
        df = pd.read_csv(f"{csv_path}/core/{table}.csv")
        df.to_sql(table, conn, if_exists='append', index=False)
    
    conn.commit()
    conn.close()
```

### From SQLite to CSV
```python
def export_sqlite_to_csv(db_path, csv_path):
    conn = sqlite3.connect(db_path)
    
    for table in ['sections', 'chapters', 'headings', 'subheadings']:
        df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
        df.to_csv(f"{csv_path}/core/{table}.csv", index=False)
    
    conn.close()
```