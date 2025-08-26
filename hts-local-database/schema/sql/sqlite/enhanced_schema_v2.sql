-- Enhanced HTS Database Schema v2.0
-- Comprehensive system with products, notes, cross-references, and enhanced relationships
-- Built on existing v1 foundation with backward compatibility

-- Enable foreign keys and performance optimizations
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA cache_size = -64000;
PRAGMA temp_store = memory;

-- =====================================
-- CORE CLASSIFICATION TABLES (Enhanced)
-- =====================================

-- Enhanced sections table (keeping existing structure, adding fields)
ALTER TABLE sections ADD COLUMN revision_year INTEGER DEFAULT 2022;
ALTER TABLE sections ADD COLUMN effective_date DATE;
ALTER TABLE sections ADD COLUMN status TEXT DEFAULT 'active' CHECK (status IN ('active', 'deprecated', 'reserved'));
ALTER TABLE sections ADD COLUMN sort_order INTEGER;
ALTER TABLE sections ADD COLUMN icon_url TEXT;
ALTER TABLE sections ADD COLUMN color_code TEXT; -- For UI themes

-- Enhanced chapters table
ALTER TABLE chapters ADD COLUMN revision_year INTEGER DEFAULT 2022;
ALTER TABLE chapters ADD COLUMN effective_date DATE;
ALTER TABLE chapters ADD COLUMN status TEXT DEFAULT 'active' CHECK (status IN ('active', 'deprecated', 'reserved'));
ALTER TABLE chapters ADD COLUMN statistical_suffix VARCHAR(4);
ALTER TABLE chapters ADD COLUMN trade_volume_rank INTEGER;
ALTER TABLE chapters ADD COLUMN complexity_score INTEGER DEFAULT 1 CHECK (complexity_score BETWEEN 1 AND 5);

-- Enhanced headings table
ALTER TABLE headings ADD COLUMN revision_year INTEGER DEFAULT 2022;
ALTER TABLE headings ADD COLUMN effective_date DATE;
ALTER TABLE headings ADD COLUMN status TEXT DEFAULT 'active' CHECK (status IN ('active', 'deprecated', 'reserved'));
ALTER TABLE headings ADD COLUMN statistical_suffix VARCHAR(4);
ALTER TABLE headings ADD COLUMN trade_frequency_score REAL DEFAULT 0.0;
ALTER TABLE headings ADD COLUMN classification_difficulty INTEGER DEFAULT 1 CHECK (classification_difficulty BETWEEN 1 AND 5);

-- Enhanced subheadings table
ALTER TABLE subheadings ADD COLUMN revision_year INTEGER DEFAULT 2022;
ALTER TABLE subheadings ADD COLUMN effective_date DATE;
ALTER TABLE subheadings ADD COLUMN status TEXT DEFAULT 'active' CHECK (status IN ('active', 'deprecated', 'reserved'));
ALTER TABLE subheadings ADD COLUMN statistical_suffix VARCHAR(4);
ALTER TABLE subheadings ADD COLUMN measurement_unit TEXT;
ALTER TABLE subheadings ADD COLUMN supplementary_unit TEXT;
ALTER TABLE subheadings ADD COLUMN conversion_factor REAL;

-- =====================================
-- PRODUCT CLASSIFICATION SYSTEM
-- =====================================

-- Product categories for better organization
CREATE TABLE product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_code VARCHAR(10) NOT NULL UNIQUE,
    category_name TEXT NOT NULL,
    parent_category_id INTEGER REFERENCES product_categories(category_id),
    description TEXT,
    icon_url TEXT,
    sort_order INTEGER,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Actual products mapped to HTS codes
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    common_name TEXT,
    scientific_name TEXT,
    brand_names TEXT, -- JSON array of brand names
    subheading_id INTEGER NOT NULL REFERENCES subheadings(subheading_id),
    category_id INTEGER REFERENCES product_categories(category_id),
    description TEXT,
    technical_specs TEXT, -- JSON object with technical specifications  
    typical_uses TEXT, -- JSON array of common uses
    origin_countries TEXT, -- JSON array of typical origin countries
    seasonal_availability TEXT, -- JSON object with seasonal info
    shelf_life_days INTEGER,
    storage_requirements TEXT,
    hazard_classifications TEXT, -- JSON array of hazard codes
    certification_requirements TEXT, -- JSON array of required certifications
    packaging_types TEXT, -- JSON array of common packaging
    unit_weight_kg REAL,
    unit_dimensions TEXT, -- JSON object {length, width, height, unit}
    is_controlled BOOLEAN DEFAULT 0, -- Requires special permits/licenses
    is_prohibited BOOLEAN DEFAULT 0, -- Prohibited for import/export
    confidence_score REAL DEFAULT 1.0,
    data_sources TEXT, -- JSON array of data sources
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product images and media
CREATE TABLE product_media (
    media_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    media_type TEXT NOT NULL CHECK (media_type IN ('image', 'video', 'document', 'diagram')),
    file_url TEXT NOT NULL,
    file_name TEXT,
    file_size_bytes INTEGER,
    mime_type TEXT,
    caption TEXT,
    alt_text TEXT,
    is_primary BOOLEAN DEFAULT 0,
    sort_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product variations (size, color, grade, etc.)
CREATE TABLE product_variations (
    variation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    variation_type TEXT NOT NULL, -- 'size', 'color', 'grade', 'quality', etc.
    variation_value TEXT NOT NULL,
    additional_description TEXT,
    price_premium_pct REAL DEFAULT 0.0,
    availability_score REAL DEFAULT 1.0,
    subheading_override INTEGER REFERENCES subheadings(subheading_id), -- Different classification if needed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- COMPREHENSIVE NOTES SYSTEM  
-- =====================================

-- Legal and explanatory notes at all levels
CREATE TABLE classification_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    reference_type TEXT NOT NULL CHECK (reference_type IN ('section', 'chapter', 'heading', 'subheading', 'product')),
    reference_id INTEGER NOT NULL, -- ID of the referenced record
    note_type TEXT NOT NULL CHECK (note_type IN ('general', 'explanatory', 'legal', 'exclusion', 'inclusion', 'example', 'warning', 'classification_rule')),
    note_sequence INTEGER DEFAULT 1, -- For ordering notes
    title TEXT,
    note_text TEXT NOT NULL,
    note_text_html TEXT, -- Rich text version
    legal_reference TEXT, -- Source of legal authority
    country_specific TEXT, -- ISO country code if country-specific
    language_code TEXT DEFAULT 'en',
    effective_date DATE,
    expiry_date DATE,
    is_binding BOOLEAN DEFAULT 0, -- Is this legally binding?
    priority_level INTEGER DEFAULT 1 CHECK (priority_level BETWEEN 1 AND 5),
    created_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Examples and case studies for better understanding
CREATE TABLE classification_examples (
    example_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subheading_id INTEGER NOT NULL REFERENCES subheadings(subheading_id),
    product_id INTEGER REFERENCES products(product_id),
    example_type TEXT CHECK (example_type IN ('positive', 'negative', 'border_case', 'ruling')),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    ruling_details TEXT,
    ruling_authority TEXT,
    ruling_date DATE,
    ruling_reference TEXT,
    country_code TEXT,
    is_precedent BOOLEAN DEFAULT 0,
    confidence_level REAL DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Frequently asked questions
CREATE TABLE classification_faq (
    faq_id INTEGER PRIMARY KEY AUTOINCREMENT,
    reference_type TEXT NOT NULL CHECK (reference_type IN ('section', 'chapter', 'heading', 'subheading', 'product')),
    reference_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    answer_html TEXT,
    category TEXT, -- 'classification', 'documentation', 'rates', etc.
    view_count INTEGER DEFAULT 0,
    helpfulness_score REAL DEFAULT 0.0,
    language_code TEXT DEFAULT 'en',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- CROSS-REFERENCE AND MAPPING SYSTEM
-- =====================================

-- Alternative names and synonyms
CREATE TABLE alternative_names (
    alt_name_id INTEGER PRIMARY KEY AUTOINCREMENT,
    reference_type TEXT NOT NULL CHECK (reference_type IN ('section', 'chapter', 'heading', 'subheading', 'product')),
    reference_id INTEGER NOT NULL,
    alternative_name TEXT NOT NULL,
    name_type TEXT CHECK (name_type IN ('synonym', 'trade_name', 'scientific', 'common', 'abbreviation', 'acronym', 'obsolete')),
    language_code TEXT DEFAULT 'en',
    region_specific TEXT, -- Geographic region where this name is used
    usage_frequency REAL DEFAULT 1.0, -- How commonly this name is used (0.0-1.0)
    is_preferred BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cross-references between classifications
CREATE TABLE cross_references (
    xref_id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_type TEXT NOT NULL CHECK (from_type IN ('section', 'chapter', 'heading', 'subheading')),
    from_id INTEGER NOT NULL,
    to_type TEXT NOT NULL CHECK (to_type IN ('section', 'chapter', 'heading', 'subheading')),
    to_id INTEGER NOT NULL,
    relationship_type TEXT CHECK (relationship_type IN ('related', 'similar', 'alternative', 'superseded_by', 'supersedes', 'includes', 'excludes', 'see_also')),
    relationship_strength REAL DEFAULT 1.0 CHECK (relationship_strength BETWEEN 0.0 AND 1.0),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Mapping to other classification systems (NAICS, SIC, UN CPC, etc.)
CREATE TABLE external_mappings (
    mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hts_type TEXT NOT NULL CHECK (hts_type IN ('section', 'chapter', 'heading', 'subheading')),
    hts_id INTEGER NOT NULL,
    external_system TEXT NOT NULL, -- 'NAICS', 'SIC', 'UN_CPC', 'ISIC', etc.
    external_code TEXT NOT NULL,
    external_description TEXT,
    mapping_accuracy REAL DEFAULT 1.0 CHECK (mapping_accuracy BETWEEN 0.0 AND 1.0),
    mapping_type TEXT CHECK (mapping_type IN ('exact', 'approximate', 'partial', 'broader', 'narrower')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- TRADE AND DUTY INFORMATION
-- =====================================

-- Enhanced countries table with more details
INSERT OR IGNORE INTO countries (country_code, country_name, classification_system, max_digits, is_active) VALUES
('US', 'United States', 'HTS-US', 10, 1),
('CA', 'Canada', 'HS-Canada', 10, 1),
('MX', 'Mexico', 'TIGIE', 8, 1),
('CN', 'China', 'HS-China', 10, 1),
('DE', 'Germany', 'TARIC', 11, 1),
('FR', 'France', 'TARIC', 11, 1),
('GB', 'United Kingdom', 'UK-TARIC', 10, 1),
('JP', 'Japan', 'Japan-HS', 9, 1),
('AU', 'Australia', 'HTSCA', 10, 1),
('BR', 'Brazil', 'NCM', 8, 1);

-- Trade agreements and preferential arrangements
CREATE TABLE trade_agreements (
    agreement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agreement_code TEXT NOT NULL UNIQUE,
    agreement_name TEXT NOT NULL,
    agreement_type TEXT CHECK (agreement_type IN ('FTA', 'customs_union', 'preferential', 'GSP', 'regional', 'bilateral', 'multilateral')),
    member_countries TEXT NOT NULL, -- JSON array of ISO country codes
    effective_date DATE,
    expiry_date DATE,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'expired', 'proposed')),
    description TEXT,
    website_url TEXT,
    legal_text_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Duty rates and trade preferences  
CREATE TABLE duty_rates (
    rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL REFERENCES countries(country_id),
    classification_type TEXT NOT NULL CHECK (classification_type IN ('subheading', 'national_8', 'national_10', 'national_12')),
    classification_id INTEGER NOT NULL, -- Reference to appropriate table
    classification_code TEXT NOT NULL, -- The actual code for quick lookup
    rate_type TEXT NOT NULL CHECK (rate_type IN ('MFN', 'general', 'preferential', 'GSP', 'anti_dumping', 'countervailing')),
    agreement_id INTEGER REFERENCES trade_agreements(agreement_id),
    ad_valorem_rate REAL, -- Percentage rate
    specific_rate TEXT, -- e.g., "$0.05/kg"  
    compound_rate TEXT, -- e.g., "5% + $0.10/kg"
    rate_description TEXT,
    minimum_rate REAL,
    maximum_rate REAL,
    quota_quantity REAL,
    quota_unit TEXT,
    quota_period TEXT, -- 'annual', 'quarterly', 'monthly'
    effective_date DATE NOT NULL,
    expiry_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Import/export restrictions and requirements
CREATE TABLE trade_restrictions (
    restriction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL REFERENCES countries(country_id),
    classification_type TEXT NOT NULL CHECK (classification_type IN ('section', 'chapter', 'heading', 'subheading', 'product')),
    classification_id INTEGER NOT NULL,
    restriction_type TEXT NOT NULL CHECK (restriction_type IN ('prohibition', 'license', 'permit', 'quota', 'certification', 'inspection', 'tariff_quota')),
    restriction_category TEXT CHECK (restriction_category IN ('health', 'safety', 'environmental', 'security', 'economic', 'cultural', 'religious')),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    legal_authority TEXT,
    required_documents TEXT, -- JSON array of required documents
    application_process TEXT,
    processing_time_days INTEGER,
    fees TEXT, -- JSON object with fee structure
    validity_period_days INTEGER,
    seasonal_restrictions TEXT, -- JSON object with seasonal info
    quantity_limits TEXT, -- JSON object with quantity restrictions
    country_of_origin_rules TEXT,
    end_use_restrictions TEXT,
    agency_contact TEXT, -- JSON object with contact info
    website_url TEXT,
    effective_date DATE,
    expiry_date DATE,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- ENHANCED SEARCH AND INDEXING
-- =====================================

-- Full-text search index (enhanced)
DROP TABLE IF EXISTS search_index;
CREATE VIRTUAL TABLE search_index USING fts5(
    record_type,
    record_id,
    code,
    title_en,
    description,
    keywords,
    alternative_names,
    notes_text,
    product_names,
    examples_text,
    content='',
    contentless_delete=1
);

-- Search suggestions and auto-complete
CREATE TABLE search_suggestions (
    suggestion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    suggestion_text TEXT NOT NULL UNIQUE,
    suggestion_type TEXT CHECK (suggestion_type IN ('product', 'classification', 'keyword', 'phrase')),
    search_count INTEGER DEFAULT 0,
    result_count INTEGER DEFAULT 0,
    success_rate REAL DEFAULT 0.0,
    language_code TEXT DEFAULT 'en',
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User search history and analytics
CREATE TABLE search_history (
    search_id INTEGER PRIMARY KEY AUTOINCREMENT,
    search_query TEXT NOT NULL,
    search_filters TEXT, -- JSON object with applied filters
    result_count INTEGER,
    selected_result_type TEXT,
    selected_result_id INTEGER,
    search_duration_ms INTEGER,
    user_session_id TEXT,
    ip_address TEXT,
    user_agent TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- DATA QUALITY AND VALIDATION
-- =====================================

-- Data quality scores and validation results
CREATE TABLE data_quality_scores (
    score_id INTEGER PRIMARY KEY AUTOINCREMENT,
    record_type TEXT NOT NULL CHECK (record_type IN ('section', 'chapter', 'heading', 'subheading', 'product')),
    record_id INTEGER NOT NULL,
    completeness_score REAL DEFAULT 0.0 CHECK (completeness_score BETWEEN 0.0 AND 1.0),
    accuracy_score REAL DEFAULT 0.0 CHECK (accuracy_score BETWEEN 0.0 AND 1.0),
    consistency_score REAL DEFAULT 0.0 CHECK (consistency_score BETWEEN 0.0 AND 1.0),
    freshness_score REAL DEFAULT 0.0 CHECK (freshness_score BETWEEN 0.0 AND 1.0),
    overall_score REAL DEFAULT 0.0 CHECK (overall_score BETWEEN 0.0 AND 1.0),
    validation_errors TEXT, -- JSON array of validation errors
    last_validated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    validation_method TEXT,
    validated_by TEXT
);

-- Change log for audit trail
CREATE TABLE change_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT NOT NULL,
    record_id INTEGER NOT NULL,
    operation TEXT NOT NULL CHECK (operation IN ('INSERT', 'UPDATE', 'DELETE')),
    old_values TEXT, -- JSON object with old values
    new_values TEXT, -- JSON object with new values
    changed_fields TEXT, -- JSON array of changed field names
    change_reason TEXT,
    changed_by TEXT,
    ip_address TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- COMPREHENSIVE INDEXES
-- =====================================

-- Primary lookup indexes
CREATE INDEX idx_products_subheading ON products(subheading_id);
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_name ON products(product_name);
CREATE INDEX idx_products_common_name ON products(common_name);
CREATE INDEX idx_products_scientific_name ON products(scientific_name);
CREATE INDEX idx_products_active ON products(is_prohibited, is_controlled);

-- Notes and examples indexes
CREATE INDEX idx_classification_notes_ref ON classification_notes(reference_type, reference_id);
CREATE INDEX idx_classification_notes_type ON classification_notes(note_type);
CREATE INDEX idx_classification_examples_subheading ON classification_examples(subheading_id);
CREATE INDEX idx_classification_examples_product ON classification_examples(product_id);
CREATE INDEX idx_faq_reference ON classification_faq(reference_type, reference_id);

-- Cross-reference indexes
CREATE INDEX idx_alternative_names_ref ON alternative_names(reference_type, reference_id);
CREATE INDEX idx_alternative_names_text ON alternative_names(alternative_name);
CREATE INDEX idx_cross_references_from ON cross_references(from_type, from_id);
CREATE INDEX idx_cross_references_to ON cross_references(to_type, to_id);
CREATE INDEX idx_external_mappings_hts ON external_mappings(hts_type, hts_id);
CREATE INDEX idx_external_mappings_external ON external_mappings(external_system, external_code);

-- Trade information indexes
CREATE INDEX idx_duty_rates_country ON duty_rates(country_id);
CREATE INDEX idx_duty_rates_classification ON duty_rates(classification_type, classification_id);
CREATE INDEX idx_duty_rates_code ON duty_rates(classification_code);
CREATE INDEX idx_duty_rates_effective ON duty_rates(effective_date, expiry_date);
CREATE INDEX idx_restrictions_country ON trade_restrictions(country_id);
CREATE INDEX idx_restrictions_classification ON trade_restrictions(classification_type, classification_id);

-- Search and analytics indexes
CREATE INDEX idx_search_suggestions_text ON search_suggestions(suggestion_text);
CREATE INDEX idx_search_history_query ON search_history(search_query);
CREATE INDEX idx_search_history_timestamp ON search_history(timestamp);

-- Data quality indexes
CREATE INDEX idx_quality_scores_record ON data_quality_scores(record_type, record_id);
CREATE INDEX idx_quality_scores_overall ON data_quality_scores(overall_score);
CREATE INDEX idx_change_log_table_record ON change_log(table_name, record_id);
CREATE INDEX idx_change_log_timestamp ON change_log(timestamp);

-- =====================================
-- ENHANCED VIEWS
-- =====================================

-- Complete product view with full classification hierarchy
CREATE VIEW v_products_complete AS
SELECT 
    p.product_id,
    p.product_name,
    p.common_name,
    p.scientific_name,
    p.description as product_description,
    -- Classification hierarchy
    s.section_number,
    s.title_en as section_title,
    c.chapter_code,
    c.title_en as chapter_title,
    h.heading_code,
    h.title_en as heading_title,
    sh.subheading_code,
    sh.title_en as subheading_title,
    -- Product details
    pc.category_name,
    p.typical_uses,
    p.origin_countries,
    p.is_controlled,
    p.is_prohibited,
    p.confidence_score,
    -- Counts
    (SELECT COUNT(*) FROM product_media pm WHERE pm.product_id = p.product_id) as media_count,
    (SELECT COUNT(*) FROM product_variations pv WHERE pv.product_id = p.product_id) as variation_count,
    (SELECT COUNT(*) FROM classification_notes cn WHERE cn.reference_type = 'product' AND cn.reference_id = p.product_id) as note_count
FROM products p
JOIN subheadings sh ON p.subheading_id = sh.subheading_id
JOIN headings h ON sh.heading_id = h.heading_id
JOIN chapters c ON h.chapter_id = c.chapter_id
JOIN sections s ON c.section_id = s.section_id
LEFT JOIN product_categories pc ON p.category_id = pc.category_id
WHERE p.product_name IS NOT NULL;

-- Classification with notes and examples
CREATE VIEW v_classification_enriched AS
SELECT 
    'subheading' as classification_type,
    sh.subheading_id as classification_id,
    sh.subheading_code as code,
    sh.title_en as title,
    sh.description,
    s.section_number,
    s.title_en as section_title,
    c.chapter_code,
    c.title_en as chapter_title,
    h.heading_code,
    h.title_en as heading_title,
    -- Counts
    (SELECT COUNT(*) FROM products p WHERE p.subheading_id = sh.subheading_id) as product_count,
    (SELECT COUNT(*) FROM classification_notes cn WHERE cn.reference_type = 'subheading' AND cn.reference_id = sh.subheading_id) as note_count,
    (SELECT COUNT(*) FROM classification_examples ce WHERE ce.subheading_id = sh.subheading_id) as example_count,
    (SELECT COUNT(*) FROM alternative_names an WHERE an.reference_type = 'subheading' AND an.reference_id = sh.subheading_id) as alt_name_count
FROM subheadings sh
JOIN headings h ON sh.heading_id = h.heading_id
JOIN chapters c ON h.chapter_id = c.chapter_id
JOIN sections s ON c.section_id = s.section_id;

-- Trade information summary
CREATE VIEW v_trade_summary AS
SELECT 
    c.country_code,
    c.country_name,
    COUNT(DISTINCT dr.rate_id) as duty_rate_count,
    COUNT(DISTINCT tr.restriction_id) as restriction_count,
    COUNT(DISTINCT ta.agreement_id) as agreement_count,
    AVG(dr.ad_valorem_rate) as avg_duty_rate,
    MAX(dr.effective_date) as latest_rate_update
FROM countries c
LEFT JOIN duty_rates dr ON c.country_id = dr.country_id
LEFT JOIN trade_restrictions tr ON c.country_id = tr.country_id
LEFT JOIN trade_agreements ta ON json_extract(ta.member_countries, '$[*]') LIKE '%' || c.country_code || '%'
WHERE c.is_active = 1
GROUP BY c.country_id, c.country_code, c.country_name;

-- Data quality dashboard
CREATE VIEW v_data_quality_dashboard AS
SELECT 
    record_type,
    COUNT(*) as total_records,
    AVG(overall_score) as avg_quality_score,
    COUNT(CASE WHEN overall_score >= 0.9 THEN 1 END) as high_quality_count,
    COUNT(CASE WHEN overall_score < 0.7 THEN 1 END) as low_quality_count,
    MAX(last_validated) as latest_validation
FROM data_quality_scores
GROUP BY record_type;

-- =====================================
-- TRIGGERS FOR DATA INTEGRITY
-- =====================================

-- Update timestamps on modifications
CREATE TRIGGER tr_products_updated_at
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = NEW.product_id;
END;

CREATE TRIGGER tr_classification_notes_updated_at
AFTER UPDATE ON classification_notes
BEGIN
    UPDATE classification_notes SET updated_at = CURRENT_TIMESTAMP WHERE note_id = NEW.note_id;
END;

-- Maintain search index
CREATE TRIGGER tr_search_index_products_insert
AFTER INSERT ON products
BEGIN
    INSERT INTO search_index (record_type, record_id, code, title_en, description, product_names)
    SELECT 'product', NEW.product_id, 
           (SELECT sh.subheading_code FROM subheadings sh WHERE sh.subheading_id = NEW.subheading_id),
           NEW.product_name, NEW.description, NEW.product_name || ' ' || COALESCE(NEW.common_name, '');
END;

CREATE TRIGGER tr_search_index_products_update
AFTER UPDATE ON products
BEGIN
    UPDATE search_index 
    SET title_en = NEW.product_name,
        description = NEW.description,
        product_names = NEW.product_name || ' ' || COALESCE(NEW.common_name, '')
    WHERE record_type = 'product' AND record_id = NEW.product_id;
END;

CREATE TRIGGER tr_search_index_products_delete
AFTER DELETE ON products
BEGIN
    DELETE FROM search_index WHERE record_type = 'product' AND record_id = OLD.product_id;
END;

-- Log changes for audit trail
CREATE TRIGGER tr_products_change_log
AFTER UPDATE ON products
BEGIN
    INSERT INTO change_log (table_name, record_id, operation, old_values, new_values, timestamp)
    VALUES ('products', NEW.product_id, 'UPDATE', 
            json_object('product_name', OLD.product_name, 'description', OLD.description),
            json_object('product_name', NEW.product_name, 'description', NEW.description),
            CURRENT_TIMESTAMP);
END;