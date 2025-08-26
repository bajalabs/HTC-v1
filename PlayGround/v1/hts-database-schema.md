# Harmonized Tariff System (HTS) Database Schema
Version 1.0 | Multi-Country Support

## Overview
This schema defines a hierarchical database structure for storing harmonized tariff codes with support for multiple countries and their specific extensions.

## Core Tables (International - HS6)

### 1. sections
Highest level grouping (21 sections in total)
```
- section_id: INTEGER PRIMARY KEY
- section_number: VARCHAR(10) -- Roman numerals (I, II, III, etc.)
- title_en: TEXT NOT NULL
- title_es: TEXT -- Spanish translation
- title_local: TEXT -- Local language translation
- description: TEXT
- notes: TEXT
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
```

### 2. chapters
2-digit classification level (Chapters 01-99)
```
- chapter_id: INTEGER PRIMARY KEY
- section_id: INTEGER FOREIGN KEY -> sections.section_id
- chapter_code: VARCHAR(2) NOT NULL UNIQUE -- "01" to "99"
- title_en: TEXT NOT NULL
- title_es: TEXT
- title_local: TEXT
- description: TEXT
- notes: TEXT
- general_notes: TEXT -- Chapter-specific general rules
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
```

### 3. headings
4-digit classification level
```
- heading_id: INTEGER PRIMARY KEY
- chapter_id: INTEGER FOREIGN KEY -> chapters.chapter_id
- heading_code: VARCHAR(4) NOT NULL UNIQUE -- "0101" to "9999"
- title_en: TEXT NOT NULL
- title_es: TEXT
- title_local: TEXT
- description: TEXT
- notes: TEXT
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
```

### 4. subheadings
6-digit classification level (internationally harmonized)
```
- subheading_id: INTEGER PRIMARY KEY
- heading_id: INTEGER FOREIGN KEY -> headings.heading_id
- subheading_code: VARCHAR(6) NOT NULL UNIQUE -- "010101" to "999999"
- title_en: TEXT NOT NULL
- title_es: TEXT
- title_local: TEXT
- description: TEXT
- unit_of_quantity: VARCHAR(20) -- kg, units, pairs, etc.
- notes: TEXT
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
```

## Country-Specific Tables

### 5. countries
Country registry for multi-country support
```
- country_id: INTEGER PRIMARY KEY
- country_code: VARCHAR(2) NOT NULL UNIQUE -- ISO 3166-1 alpha-2
- country_name: VARCHAR(100) NOT NULL
- classification_system: VARCHAR(50) -- "HTS", "NCM", "TARIC", etc.
- max_digits: INTEGER -- 8, 10, or 12
- effective_date: DATE
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
```

### 6. tariff_8digit
8-digit country-specific codes
```
- tariff8_id: INTEGER PRIMARY KEY
- country_id: INTEGER FOREIGN KEY -> countries.country_id
- subheading_id: INTEGER FOREIGN KEY -> subheadings.subheading_id
- tariff8_code: VARCHAR(8) NOT NULL
- title_en: TEXT NOT NULL
- title_local: TEXT
- description: TEXT
- duty_rate_general: DECIMAL(5,2) -- Percentage
- duty_rate_mfn: DECIMAL(5,2) -- Most Favored Nation rate
- duty_rate_preferential: DECIMAL(5,2)
- unit_of_quantity: VARCHAR(20)
- restrictions: TEXT -- Import/export restrictions
- notes: TEXT
- effective_from: DATE
- effective_to: DATE
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
- UNIQUE KEY (country_id, tariff8_code)
```

### 7. tariff_10digit
10-digit country-specific codes
```
- tariff10_id: INTEGER PRIMARY KEY
- country_id: INTEGER FOREIGN KEY -> countries.country_id
- tariff8_id: INTEGER FOREIGN KEY -> tariff_8digit.tariff8_id
- tariff10_code: VARCHAR(10) NOT NULL
- title_en: TEXT NOT NULL
- title_local: TEXT
- description: TEXT
- duty_rate_general: DECIMAL(5,2)
- duty_rate_mfn: DECIMAL(5,2)
- duty_rate_preferential: DECIMAL(5,2)
- unit_of_quantity: VARCHAR(20)
- statistical_suffix: VARCHAR(4)
- restrictions: TEXT
- notes: TEXT
- effective_from: DATE
- effective_to: DATE
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
- UNIQUE KEY (country_id, tariff10_code)
```

### 8. tariff_12digit
12-digit country-specific codes (where applicable)
```
- tariff12_id: INTEGER PRIMARY KEY
- country_id: INTEGER FOREIGN KEY -> countries.country_id
- tariff10_id: INTEGER FOREIGN KEY -> tariff_10digit.tariff10_id
- tariff12_code: VARCHAR(12) NOT NULL
- title_en: TEXT NOT NULL
- title_local: TEXT
- description: TEXT
- duty_rate_general: DECIMAL(5,2)
- duty_rate_mfn: DECIMAL(5,2)
- duty_rate_preferential: DECIMAL(5,2)
- unit_of_quantity: VARCHAR(20)
- additional_codes: VARCHAR(20)
- restrictions: TEXT
- notes: TEXT
- effective_from: DATE
- effective_to: DATE
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
- UNIQUE KEY (country_id, tariff12_code)
```

## Supporting Tables

### 9. duty_rates_history
Track historical duty rate changes
```
- history_id: INTEGER PRIMARY KEY
- country_id: INTEGER FOREIGN KEY -> countries.country_id
- tariff_code: VARCHAR(12) NOT NULL
- tariff_level: VARCHAR(10) -- '8digit', '10digit', '12digit'
- duty_type: VARCHAR(20) -- 'general', 'mfn', 'preferential'
- old_rate: DECIMAL(5,2)
- new_rate: DECIMAL(5,2)
- change_date: DATE
- legal_reference: TEXT
- created_at: TIMESTAMP
```

### 10. trade_agreements
Preferential rates by trade agreement
```
- agreement_id: INTEGER PRIMARY KEY
- agreement_code: VARCHAR(20) NOT NULL UNIQUE -- "USMCA", "EU-UK", etc.
- agreement_name: VARCHAR(200) NOT NULL
- member_countries: TEXT -- JSON array of country codes
- effective_date: DATE
- expiry_date: DATE
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
```

### 11. preferential_rates
Specific rates per agreement and tariff code
```
- rate_id: INTEGER PRIMARY KEY
- agreement_id: INTEGER FOREIGN KEY -> trade_agreements.agreement_id
- country_id: INTEGER FOREIGN KEY -> countries.country_id
- tariff_code: VARCHAR(12) NOT NULL
- preferential_rate: DECIMAL(5,2)
- quota_quantity: DECIMAL(15,3)
- quota_unit: VARCHAR(20)
- conditions: TEXT
- effective_from: DATE
- effective_to: DATE
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
```

### 12. legal_notes
Chapter, heading, or subheading specific legal notes
```
- note_id: INTEGER PRIMARY KEY
- country_id: INTEGER FOREIGN KEY -> countries.country_id
- reference_type: VARCHAR(20) -- 'section', 'chapter', 'heading', 'subheading'
- reference_code: VARCHAR(12)
- note_type: VARCHAR(20) -- 'general', 'additional', 'exclusion'
- note_text: TEXT NOT NULL
- legal_reference: TEXT
- effective_from: DATE
- effective_to: DATE
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
```

### 13. search_keywords
Improve searchability with keyword associations
```
- keyword_id: INTEGER PRIMARY KEY
- tariff_code: VARCHAR(12) NOT NULL
- tariff_level: VARCHAR(10) -- 'heading', 'subheading', '8digit', etc.
- country_id: INTEGER FOREIGN KEY -> countries.country_id
- keyword: VARCHAR(100) NOT NULL
- language: VARCHAR(2) DEFAULT 'en'
- relevance_score: DECIMAL(3,2) -- 0.00 to 1.00
- created_at: TIMESTAMP
- INDEX idx_keyword (keyword)
- INDEX idx_tariff_code (tariff_code)
```

## Indexes for Performance

```sql
-- Core tables
CREATE INDEX idx_chapter_section ON chapters(section_id);
CREATE INDEX idx_heading_chapter ON headings(chapter_id);
CREATE INDEX idx_subheading_heading ON subheadings(heading_id);

-- Country-specific tables
CREATE INDEX idx_tariff8_country ON tariff_8digit(country_id);
CREATE INDEX idx_tariff8_subheading ON tariff_8digit(subheading_id);
CREATE INDEX idx_tariff8_code ON tariff_8digit(tariff8_code);
CREATE INDEX idx_tariff10_country ON tariff_10digit(country_id);
CREATE INDEX idx_tariff10_tariff8 ON tariff_10digit(tariff8_id);
CREATE INDEX idx_tariff12_country ON tariff_12digit(country_id);
CREATE INDEX idx_tariff12_tariff10 ON tariff_12digit(tariff10_id);

-- Supporting tables
CREATE INDEX idx_duty_history_country ON duty_rates_history(country_id);
CREATE INDEX idx_duty_history_code ON duty_rates_history(tariff_code);
CREATE INDEX idx_preferential_agreement ON preferential_rates(agreement_id);
CREATE INDEX idx_legal_notes_reference ON legal_notes(reference_type, reference_code);
```

## Views for Common Queries

### full_classification_view
Complete hierarchy for easy querying
```sql
CREATE VIEW full_classification_view AS
SELECT 
    s.section_number,
    s.title_en AS section_title,
    c.chapter_code,
    c.title_en AS chapter_title,
    h.heading_code,
    h.title_en AS heading_title,
    sh.subheading_code,
    sh.title_en AS subheading_title,
    t8.tariff8_code,
    t8.title_en AS tariff8_title,
    t8.duty_rate_general,
    t8.duty_rate_mfn,
    cn.country_code,
    cn.country_name
FROM sections s
JOIN chapters c ON s.section_id = c.section_id
JOIN headings h ON c.chapter_id = h.chapter_id
JOIN subheadings sh ON h.heading_id = sh.heading_id
LEFT JOIN tariff_8digit t8 ON sh.subheading_id = t8.subheading_id
LEFT JOIN countries cn ON t8.country_id = cn.country_id;
```

## Data Validation Rules

1. **Code Format Validation**
   - Chapter codes: 2 digits, padded with leading zero
   - Heading codes: 4 digits (first 2 must match chapter)
   - Subheading codes: 6 digits (first 4 must match heading)
   - 8-digit codes: first 6 must match subheading
   - 10-digit codes: first 8 must match 8-digit code
   - 12-digit codes: first 10 must match 10-digit code

2. **Hierarchical Integrity**
   - No orphaned codes (all must have valid parent)
   - Sections cannot be deleted if chapters exist
   - Cascading updates for code changes

3. **Date Validation**
   - effective_from must be before effective_to
   - No overlapping date ranges for same code

4. **Rate Validation**
   - Duty rates between 0 and 100 (percentage)
   - Preferential rates ≤ MFN rates ≤ General rates

## Migration Strategy

1. **Phase 1**: Load international HS6 data (sections → subheadings)
2. **Phase 2**: Load country-specific 8-digit extensions
3. **Phase 3**: Load 10 and 12-digit codes where applicable
4. **Phase 4**: Load supporting data (rates, agreements, notes)
5. **Phase 5**: Generate search keywords and optimize indexes

## Maintenance Considerations

- Version control for schema changes
- Audit trail for all modifications
- Annual updates for HS revisions (every 5 years major revision)
- Country-specific update schedules
- Backup strategy before bulk updates
- API versioning for dependent applications