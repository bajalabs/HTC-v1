---
# HTS Chapter [XX] Database Schema - [CHAPTER_NAME]
database_schema_version: "1.0"
chapter_code: "[XX]"
chapter_name: "[CHAPTER_NAME]"
section_code: "[SECTION_ROMAN]"
section_name: "[SECTION_NAME]"
hts_revision: "[REVISION_NUMBER]"
effective_year: "[YYYY]"
last_updated: "[YYYY-MM-DD]"
document_type: "database_ready"
classification_authority: "USITC"
data_structure: "normalized"
scraping_ready: true
python_compatible: true
sqlite_ready: true
total_records: [NUMBER]
schema_validation: "strict"
---

# Database Structure Overview

## Table: chapter_metadata
```sql
chapter_code: "[XX]"
chapter_name: "[CHAPTER_NAME]"
section_code: "[SECTION_ROMAN]" 
section_name: "[SECTION_NAME]"
revision: "[REVISION_NUMBER]"
effective_year: "[YYYY]"
total_headings: [NUMBER]
total_subheadings: [NUMBER]
exclusions_count: [NUMBER]
```

## Table: chapter_notes
```sql
note_id: 1
note_type: "[NOTE_TYPE]"
note_text: "[NOTE_TEXT]"
reference_headings: "[REFERENCE_HEADINGS]"

note_id: 2
note_type: "[NOTE_TYPE]" 
note_text: "[NOTE_TEXT]"
reference_headings: "[REFERENCE_HEADINGS]"

note_id: 3
note_type: "[NOTE_TYPE]"
note_text: "[NOTE_TEXT]"
reference_headings: "[REFERENCE_HEADINGS]"
```

## Table: us_additional_notes
```sql
us_note_id: 1
note_type: "[NOTE_TYPE]"
note_title: "[NOTE_TITLE]"
note_text: "[NOTE_TEXT]"
status: "active"
special_note: "[SPECIAL_NOTE]"

us_note_id: 2
note_type: "[NOTE_TYPE]"
note_title: "[NOTE_TITLE]"
note_text: "[NOTE_TEXT]"
reference_chapter: "[REFERENCE]"
status: "active"
```

---

# HEADING [XX].01 - [HEADING_1_NAME]

## Table: heading_[XX]01
```sql
heading_code: "[XX]01"
heading_description: "[HEADING_DESCRIPTION]"
heading_full_text: "[FULL_TEXT]"
[CLASSIFICATION_FIELD]: "[CLASSIFICATION_VALUE]"
[SCIENTIFIC_FIELD]: "[SCIENTIFIC_VALUE]"
```

## Table: subheadings_[XX]01
```sql
subheading_code: "[XX]01.21"
subheading_description: "[SUBHEADING_DESCRIPTION]"
parent_category: "[PARENT_CATEGORY]"
classification_criteria: "[CRITERIA]"
certification_required: [true/false]

subheading_code: "[XX]01.29"  
subheading_description: "[SUBHEADING_DESCRIPTION]"
parent_category: "[PARENT_CATEGORY]"
classification_criteria: "[CRITERIA]"
certification_required: [true/false]

subheading_code: "[XX]01.30"
subheading_description: "[SUBHEADING_DESCRIPTION]" 
parent_category: "[PARENT_CATEGORY]"
classification_criteria: "[CRITERIA]"
certification_required: [true/false]

subheading_code: "[XX]01.90"
subheading_description: "[SUBHEADING_DESCRIPTION]"
parent_category: "[PARENT_CATEGORY]" 
classification_criteria: "[CRITERIA]"
certification_required: [true/false]
```

## Table: statistical_codes_[XX]01
```sql
statistical_code: "[XX]01.21.00.10"
description: "[DESCRIPTION]"
parent_subheading: "[XX]01.21.00"
unit_of_quantity: "[UNIT]"
second_quantity: [null/"[UNIT]"]
[FIELD_1]: "[VALUE_1]"
[FIELD_2]: "[VALUE_2]"

statistical_code: "[XX]01.21.00.20"
description: "[DESCRIPTION]" 
parent_subheading: "[XX]01.21.00"
unit_of_quantity: "[UNIT]"
second_quantity: [null/"[UNIT]"]
[FIELD_1]: "[VALUE_1]"
[FIELD_2]: "[VALUE_2]"

statistical_code: "[XX]01.29.00.10"
description: "[DESCRIPTION]"
parent_subheading: "[XX]01.29.00"  
unit_of_quantity: "[UNIT]"
second_quantity: [null/"[UNIT]"]
[FIELD_1]: "[VALUE_1]"
[FIELD_2]: "[VALUE_2]"

statistical_code: "[XX]01.29.00.90"
description: "[DESCRIPTION]"
parent_subheading: "[XX]01.29.00"
unit_of_quantity: "[UNIT]" 
second_quantity: [null/"[UNIT]"]
[FIELD_1]: "[VALUE_1]"
[FIELD_2]: "[VALUE_2]"

statistical_code: "[XX]01.30.00.00"
description: "[DESCRIPTION]"
parent_subheading: "[XX]01.30.00"
unit_of_quantity: "[UNIT]"
second_quantity: [null/"[UNIT]"]
[FIELD_1]: "[VALUE_1]"

statistical_code: "[XX]01.90.30.00" 
description: "[DESCRIPTION]"
parent_subheading: "[XX]01.90.30"
unit_of_quantity: "[UNIT]"
second_quantity: [null/"[UNIT]"]
[FIELD_1]: "[VALUE_1]"
[FIELD_2]: "[VALUE_2]"

statistical_code: "[XX]01.90.40.00"
description: "[DESCRIPTION]"
parent_subheading: "[XX]01.90.40" 
unit_of_quantity: "[UNIT]"
second_quantity: [null/"[UNIT]"]
[FIELD_1]: "[VALUE_1]"
[FIELD_2]: "[VALUE_2]"
```

## Table: duty_rates_[XX]01
```sql
statistical_code: "[XX]01.21.00"
general_rate: "[RATE]"
general_rate_numeric: [NUMBER]
general_rate_type: "[RATE_TYPE]"
special_rate: "[RATE]" 
special_rate_numeric: [NUMBER]
special_rate_type: "[RATE_TYPE]"
unit_of_duty: "[UNIT_OF_DUTY]"

statistical_code: "[XX]01.29.00"
general_rate: "[RATE]"
general_rate_numeric: [NUMBER]
general_rate_type: "[RATE_TYPE]" 
special_rate: "[RATE]"
special_rate_numeric: [NUMBER]
special_rate_type: "[RATE_TYPE]"
unit_of_duty: "[UNIT_OF_DUTY]"

statistical_code: "[XX]01.30.00"
general_rate: "[RATE]"
general_rate_numeric: [NUMBER]
general_rate_type: "[RATE_TYPE]"
special_rate: "[RATE]"
special_rate_numeric: [NUMBER]
special_rate_type: "[RATE_TYPE]" 
footnote: "[FOOTNOTE_RATE]"
unit_of_duty: "[UNIT_OF_DUTY]"

statistical_code: "[XX]01.90.30"
general_rate: "[RATE]"
general_rate_numeric: [NUMBER]
general_rate_type: "[RATE_TYPE]"
special_rate: "[RATE]"
special_rate_numeric: [NUMBER]
special_rate_type: "[RATE_TYPE]"
unit_of_duty: "[UNIT_OF_DUTY]"

statistical_code: "[XX]01.90.40"
general_rate: "[RATE]"
general_rate_numeric: [NUMBER]
general_rate_type: "[RATE_TYPE]"
special_rate: "[RATE]"
special_rate_numeric: [NUMBER]
special_rate_type: "[RATE_TYPE]"
footnote: "[FOOTNOTE_RATE]"
unit_of_duty: "[UNIT_OF_DUTY]"
```

---

# HEADING [XX].02 - [HEADING_2_NAME]

## Table: heading_[XX]02
```sql
heading_code: "[XX]02"
heading_description: "[HEADING_DESCRIPTION]"
heading_full_text: "[FULL_TEXT]"
[CLASSIFICATION_FIELD]: "[CLASSIFICATION_VALUE]"
[SCIENTIFIC_FIELD]: "[SCIENTIFIC_VALUE]"
```

## Table: subheadings_[XX]02
```sql
subheading_code: "[XX]02.21"
subheading_description: "[SUBHEADING_DESCRIPTION]"
parent_category: "[PARENT_CATEGORY]"
classification_criteria: "[CRITERIA]"
certification_required: [true/false]

subheading_code: "[XX]02.29"
subheading_description: "[SUBHEADING_DESCRIPTION]"
parent_category: "[PARENT_CATEGORY]" 
classification_criteria: "[CRITERIA]"
[SPECIAL_FIELD]: [true/false]

subheading_code: "[XX]02.31"
subheading_description: "[SUBHEADING_DESCRIPTION]"
parent_category: "[PARENT_CATEGORY]"
classification_criteria: "[CRITERIA]"
certification_required: [true/false]

subheading_code: "[XX]02.39"
subheading_description: "[SUBHEADING_DESCRIPTION]"
parent_category: "[PARENT_CATEGORY]"
classification_criteria: "[CRITERIA]"
[SPECIAL_FIELD]: [true/false]

subheading_code: "[XX]02.90"
subheading_description: "[SUBHEADING_DESCRIPTION]"
parent_category: "[PARENT_CATEGORY]"
classification_criteria: "[CRITERIA]"
[SPECIAL_FIELD]: [true/false]
```

## Table: statistical_codes_[XX]02
```sql
statistical_code: "[XX]02.21.00.10"
description: "[DESCRIPTION]"
parent_subheading: "[XX]02.21.00"
unit_of_quantity: "[UNIT]"
second_quantity: [null/"[UNIT]"]
[FIELD_1]: "[VALUE_1]"
[FIELD_2]: "[VALUE_2]"
[FIELD_3]: "[VALUE_3]"

statistical_code: "[XX]02.21.00.20"
description: "[DESCRIPTION]"
parent_subheading: "[XX]02.21.00"
unit_of_quantity: "[UNIT]" 
second_quantity: [null/"[UNIT]"]
[FIELD_1]: "[VALUE_1]"
[FIELD_2]: "[VALUE_2]"
[FIELD_3]: "[VALUE_3]"

[CONTINUE_PATTERN_FOR_ALL_STATISTICAL_CODES]
```

## Table: duty_rates_[XX]02
```sql
statistical_code: "[XX]02.21.00"
general_rate: "[RATE]"
general_rate_numeric: [NUMBER]
general_rate_type: "[RATE_TYPE]"
special_rate: "[RATE]"
special_rate_numeric: [NUMBER]
special_rate_type: "[RATE_TYPE]"
unit_of_duty: "[UNIT_OF_DUTY]"

statistical_code: "[XX]02.29.20"
general_rate: "[RATE]"
general_rate_numeric: [NUMBER]
general_rate_type: "[RATE_TYPE]"
special_rate: "[RATE]"
special_rate_numeric: [NUMBER]
special_rate_type: "[RATE_TYPE]"
unit_of_duty: "[UNIT_OF_DUTY]"

[CONTINUE_PATTERN_FOR_ALL_RATES]
```

---

[REPEAT_PATTERN_FOR_REMAINING_HEADINGS_XX.03_THROUGH_XX.06]

---

# NORMALIZED REFERENCE TABLES

## Table: trade_programs
```sql
program_code: "[CODE]"
program_name: "[PROGRAM_NAME]"
participating_countries: "[COUNTRIES]"
status: "active"

program_code: "[CODE]"
program_name: "[PROGRAM_NAME]"
participating_countries: "[COUNTRIES]"
status: "active"

[CONTINUE_FOR_ALL_PROGRAMS]
```

## Table: units_of_measure
```sql
unit_code: "[UNIT_CODE]"
unit_description: "[DESCRIPTION]"
unit_type: "[TYPE]"
base_unit: "[BASE]"

unit_code: "[UNIT_CODE]"
unit_description: "[DESCRIPTION]"
unit_type: "[TYPE]"
base_unit: "[BASE]"
conversion_to_base: [NUMBER]

[CONTINUE_FOR_ALL_UNITS]
```

## Table: duty_rate_types
```sql
rate_type: "[RATE_TYPE]"
description: "[DESCRIPTION]"
calculation_method: "[METHOD]"

rate_type: "[RATE_TYPE]"
description: "[DESCRIPTION]"
calculation_method: "[METHOD]"

[CONTINUE_FOR_ALL_RATE_TYPES]
```

---

# DATA VALIDATION RULES

## Required Fields Validation
```sql
-- All statistical codes must have:
statistical_code: NOT NULL, FORMAT: ####.##.##.##
description: NOT NULL, MIN_LENGTH: 5
parent_subheading: NOT NULL, FOREIGN_KEY: subheadings
unit_of_quantity: NOT NULL, FOREIGN_KEY: units_of_measure

-- All duty rates must have:
general_rate: NOT NULL
special_rate: NOT NULL
unit_of_duty: NOT NULL
```

## Business Rules Validation
```sql
-- [CHAPTER_SPECIFIC_RULE_1]
[CONDITION] THEN [REQUIREMENT]

-- [CHAPTER_SPECIFIC_RULE_2]  
[CONDITION] THEN [REQUIREMENT]

-- Statistical codes must match parent subheading pattern
statistical_code LIKE parent_subheading + "%"
```

## Data Type Constraints
```sql
-- Numeric fields
general_rate_numeric: DECIMAL(10,2)
special_rate_numeric: DECIMAL(10,2)
[NUMERIC_FIELD]: [DATA_TYPE]

-- Text fields
description: VARCHAR(500)
classification_criteria: VARCHAR(100)
[TEXT_FIELD]: VARCHAR([LENGTH])
```

---

**Database Schema Version**: 1.0  
**SQLite Compatible**: Yes  
**Python Scraping Ready**: Yes  
**Total Data Points**: [NUMBER]+  
**Normalization Level**: 3NF  
**Last Updated**: [YYYY-MM-DD]

---

## 📝 Database Template Usage Instructions

### 🔧 Replacement Variables

**Basic Schema Information:**
- `[XX]` = Chapter number (01, 02, etc.)
- `[CHAPTER_NAME]` = Full chapter name
- `[SECTION_ROMAN]` = Section in Roman numerals (I, II, etc.)
- `[SECTION_NAME]` = Full section name
- `[YYYY]` = Current year
- `[REVISION_NUMBER]` = Current HTS revision

**Database Fields:**
- `[HEADING_X_NAME]` = Name of each heading
- `[DESCRIPTION]` = Field descriptions
- `[UNIT]` = Units of measure
- `[RATE]` = Duty rates
- `[FIELD_X]` = Custom fields specific to chapter
- `[VALUE_X]` = Field values

**Classification Fields:**
- `[CLASSIFICATION_FIELD]` = Fields like animal_family, product_category, etc.
- `[SCIENTIFIC_FIELD]` = Scientific classification fields
- `[CRITERIA]` = Classification criteria

### 📊 Database Design Principles

**Normalization Requirements:**
- All tables in Third Normal Form (3NF)
- Foreign key relationships properly defined
- No redundant data storage
- Consistent naming conventions

**Field Naming Standards:**
- `table_name`: lowercase with underscores
- `field_name`: descriptive, lowercase with underscores  
- `statistical_code`: always full 10-digit format
- `rate_numeric`: always decimal values for calculations

**Data Type Standards:**
```sql
-- Standard field types
statistical_code: CHAR(10) -- Always 10 characters
description: VARCHAR(500) -- Variable length descriptions
unit_of_quantity: VARCHAR(20) -- Standard units
general_rate_numeric: DECIMAL(10,2) -- Numeric rates
parent_subheading: CHAR(8) -- Always 8 characters
classification_criteria: VARCHAR(100) -- Classification methods
```

### 🔧 Chapter-Specific Customizations

**Weight-Based Classifications:**
Add fields for weight thresholds:
```sql
weight_threshold_min: INTEGER
weight_threshold_max: INTEGER
weight_unit: VARCHAR(10)
```

**Breeding/Special Use Classifications:**
Add fields for special uses:
```sql
specific_use: VARCHAR(50) -- "Breeding", "Slaughter", "General"
certification_required: BOOLEAN
time_restriction: VARCHAR(50) -- "immediate", etc.
```

**Scientific Classifications:**
Add taxonomic fields:
```sql
taxonomic_family: VARCHAR(50)
taxonomic_order: VARCHAR(50)
taxonomic_class: VARCHAR(50)
species: VARCHAR(100)
```

### 📈 Python Integration Points

**Pandas DataFrame Compatible:**
- All table structures designed for easy pandas import
- Consistent data types for analysis
- Normalized foreign keys for joins

**SQLite Integration:**
- All SQL syntax SQLite compatible
- Foreign key constraints defined
- Index-ready field structures

**Scraping Compatibility:**
- Field names match likely HTML/PDF parsing
- Description fields accommodate full text
- Rate fields handle multiple formats

### ✅ Quality Assurance Checklist

Before finalizing database schema:
- [ ] All statistical codes follow ####.##.##.## format
- [ ] All parent-child relationships properly defined
- [ ] All duty rates have both text and numeric fields
- [ ] All required business rules documented
- [ ] All chapter-specific fields included
- [ ] All reference tables populated
- [ ] Data validation rules tested
- [ ] Foreign key constraints verified