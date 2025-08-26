-- Harmonized Tariff System Database Schema (SQLite)
-- Local-First AI-Driven Population Strategy
-- Version 2.0

-- Enable foreign keys
PRAGMA foreign_keys = ON;

-- =====================================
-- Phase 1: Core International Tables
-- =====================================

-- 1. Sections (21 total)
CREATE TABLE sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_number TEXT NOT NULL UNIQUE,     -- "I", "II", ... "XXI"
    section_range TEXT NOT NULL,             -- "01-05", "06-14", etc.
    title_en TEXT NOT NULL,
    title_short TEXT,                        -- Abbreviated title for UI
    description TEXT,
    chapter_count INTEGER,                   -- Number of chapters in section
    ai_generated BOOLEAN DEFAULT 1,          -- Track AI-generated content
    confidence_score REAL DEFAULT 1.0,       -- AI confidence in data
    source_reference TEXT,                   -- Source used for generation
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Chapters (97 total, 01-97 excluding 77)
CREATE TABLE chapters (
    chapter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_id INTEGER NOT NULL,
    chapter_code TEXT NOT NULL UNIQUE,       -- "01", "02", ... "97"
    title_en TEXT NOT NULL,
    title_short TEXT,                        -- Abbreviated title
    description TEXT,
    heading_count INTEGER,                   -- Number of headings in chapter
    general_notes TEXT,                      -- Chapter-specific rules
    ai_generated BOOLEAN DEFAULT 1,
    confidence_score REAL DEFAULT 1.0,
    source_reference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (section_id) REFERENCES sections(section_id)
);

-- 3. Headings (~1,228 total)
CREATE TABLE headings (
    heading_id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INTEGER NOT NULL,
    heading_code TEXT NOT NULL UNIQUE,       -- "0101", "0102", ... "9706"
    title_en TEXT NOT NULL,
    title_short TEXT,
    description TEXT,
    subheading_count INTEGER,                -- Number of subheadings
    is_residual BOOLEAN DEFAULT 0,          -- True for "Other" categories
    ai_generated BOOLEAN DEFAULT 1,
    confidence_score REAL DEFAULT 1.0,
    source_reference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id)
);

-- 4. Subheadings (~5,612 total)
CREATE TABLE subheadings (
    subheading_id INTEGER PRIMARY KEY AUTOINCREMENT,
    heading_id INTEGER NOT NULL,
    subheading_code TEXT NOT NULL UNIQUE,    -- "010121", "010129", etc.
    title_en TEXT NOT NULL,
    title_short TEXT,
    description TEXT,
    unit_of_quantity TEXT,                   -- "kg", "u", "m²", etc.
    is_leaf_node BOOLEAN DEFAULT 0,         -- True if no further subdivision
    is_residual BOOLEAN DEFAULT 0,          -- True for "Other" categories
    ai_generated BOOLEAN DEFAULT 1,
    confidence_score REAL DEFAULT 1.0,
    source_reference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (heading_id) REFERENCES headings(heading_id)
);

-- =====================================
-- Phase 1.5: AI Enhancement Tables
-- =====================================

-- 5. AI Extraction Log
CREATE TABLE ai_extraction_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    extraction_batch TEXT NOT NULL,         -- Batch identifier
    table_name TEXT NOT NULL,               -- Which table was populated
    extraction_method TEXT,                 -- "gpt4", "claude", "web_scrape", etc.
    records_extracted INTEGER,
    records_validated INTEGER,
    validation_errors INTEGER,
    extraction_prompt TEXT,                 -- Prompt used for extraction
    raw_response TEXT,                      -- Store raw AI response
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 6. Keywords for Search Enhancement
CREATE TABLE keywords_search (
    keyword_id INTEGER PRIMARY KEY AUTOINCREMENT,
    code_level TEXT NOT NULL,               -- "section", "chapter", "heading", "subheading"
    code_value TEXT NOT NULL,               -- The actual code
    keyword TEXT NOT NULL,
    keyword_type TEXT,                      -- "primary", "synonym", "related"
    language TEXT DEFAULT 'en',
    relevance_score REAL DEFAULT 0.5,       -- 0.0 to 1.0
    ai_generated BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. Validation Rules
CREATE TABLE validation_rules (
    rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_name TEXT NOT NULL,
    table_name TEXT NOT NULL,
    column_name TEXT,
    rule_type TEXT NOT NULL,                -- "format", "range", "reference", "logic"
    rule_expression TEXT NOT NULL,          -- SQL or regex expression
    error_message TEXT,
    severity TEXT DEFAULT 'warning',        -- "error", "warning", "info"
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- Phase 2: Country Extensions
-- =====================================

-- 8. Countries Registry
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_code TEXT NOT NULL UNIQUE,      -- ISO 3166-1 alpha-2
    country_name TEXT NOT NULL,
    classification_system TEXT,             -- "HTS", "CN", "TARIC", etc.
    api_endpoint TEXT,                      -- API URL for data fetching
    api_key_required BOOLEAN DEFAULT 0,
    max_digits INTEGER,                     -- 8, 10, or 12
    last_sync_date DATE,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 9. Country-specific Classifications
CREATE TABLE country_classifications (
    classification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL,
    parent_code TEXT NOT NULL,              -- 6-digit subheading code
    full_code TEXT NOT NULL,                -- 8, 10, or 12-digit code
    code_level INTEGER NOT NULL,            -- 8, 10, or 12
    title_en TEXT,
    title_local TEXT,
    duty_rate TEXT,                         -- Store as JSON for multiple rates
    unit_of_quantity TEXT,
    restrictions TEXT,                      -- JSON array of restrictions
    effective_from DATE,
    effective_to DATE,
    api_source TEXT,                        -- Track data source
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- =====================================
-- Indexes for Performance
-- =====================================

-- Core hierarchy indexes
CREATE INDEX idx_chapter_section ON chapters(section_id);
CREATE INDEX idx_heading_chapter ON headings(chapter_id);
CREATE INDEX idx_subheading_heading ON subheadings(heading_id);

-- Code lookup indexes
CREATE INDEX idx_chapter_code ON chapters(chapter_code);
CREATE INDEX idx_heading_code ON headings(heading_code);
CREATE INDEX idx_subheading_code ON subheadings(subheading_code);

-- Search indexes
CREATE INDEX idx_keyword_search ON keywords_search(keyword);
CREATE INDEX idx_keyword_code ON keywords_search(code_value);

-- Country extension indexes
CREATE UNIQUE INDEX idx_country_code ON country_classifications(country_id, full_code);
CREATE INDEX idx_parent_code ON country_classifications(parent_code);

-- =====================================
-- Full-Text Search Setup
-- =====================================

-- FTS5 virtual table for searching
CREATE VIRTUAL TABLE search_index USING fts5(
    code,
    title_en,
    description,
    keywords,
    content='',
    contentless_delete=1
);

-- =====================================
-- Useful Views
-- =====================================

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

-- =====================================
-- Triggers for Data Integrity
-- =====================================

-- Auto-update timestamps
CREATE TRIGGER update_sections_timestamp 
AFTER UPDATE ON sections
BEGIN
    UPDATE sections SET updated_at = CURRENT_TIMESTAMP WHERE section_id = NEW.section_id;
END;

CREATE TRIGGER update_chapters_timestamp 
AFTER UPDATE ON chapters
BEGIN
    UPDATE chapters SET updated_at = CURRENT_TIMESTAMP WHERE chapter_id = NEW.chapter_id;
END;

CREATE TRIGGER update_headings_timestamp 
AFTER UPDATE ON headings
BEGIN
    UPDATE headings SET updated_at = CURRENT_TIMESTAMP WHERE heading_id = NEW.heading_id;
END;

CREATE TRIGGER update_subheadings_timestamp 
AFTER UPDATE ON subheadings
BEGIN
    UPDATE subheadings SET updated_at = CURRENT_TIMESTAMP WHERE subheading_id = NEW.subheading_id;
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
        WHEN NEW.chapter_code NOT GLOB '[0-9][0-9]' THEN
            RAISE(ABORT, 'Chapter code must be numeric')
    END;
END;

-- Validate heading codes match chapter
CREATE TRIGGER validate_heading_code
BEFORE INSERT ON headings
BEGIN
    SELECT CASE
        WHEN LENGTH(NEW.heading_code) != 4 THEN
            RAISE(ABORT, 'Heading code must be 4 digits')
        WHEN NEW.heading_code NOT GLOB '[0-9][0-9][0-9][0-9]' THEN
            RAISE(ABORT, 'Heading code must be numeric')
        WHEN NOT EXISTS (
            SELECT 1 FROM chapters 
            WHERE chapter_code = SUBSTR(NEW.heading_code, 1, 2) 
            AND chapter_id = NEW.chapter_id
        ) THEN
            RAISE(ABORT, 'Heading code must match chapter code')
    END;
END;

-- Validate subheading codes match heading
CREATE TRIGGER validate_subheading_code
BEFORE INSERT ON subheadings
BEGIN
    SELECT CASE
        WHEN LENGTH(NEW.subheading_code) != 6 THEN
            RAISE(ABORT, 'Subheading code must be 6 digits')
        WHEN NEW.subheading_code NOT GLOB '[0-9][0-9][0-9][0-9][0-9][0-9]' THEN
            RAISE(ABORT, 'Subheading code must be numeric')
        WHEN NOT EXISTS (
            SELECT 1 FROM headings 
            WHERE heading_code = SUBSTR(NEW.subheading_code, 1, 4) 
            AND heading_id = NEW.heading_id
        ) THEN
            RAISE(ABORT, 'Subheading code must match heading code')
    END;
END;