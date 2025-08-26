---
# HTS Chapter 2 Database Schema - Meat and Edible Meat Offal
database_schema_version: "1.0"
chapter_code: "02"
chapter_name: "Meat and Edible Meat Offal"
section_code: "I"
section_name: "Live Animals; Animal Products"
hts_revision: "19"
effective_year: "2025"
last_updated: "2025-08-25"
document_type: "database_ready"
classification_authority: "USITC"
data_structure: "normalized"
scraping_ready: true
python_compatible: true
sqlite_ready: true
total_records: 150
schema_validation: "strict"
---

# Database Structure Overview

## Table: chapter_metadata
```sql
chapter_code: "02"
chapter_name: "Meat and Edible Meat Offal"
section_code: "I" 
section_name: "Live Animals; Animal Products"
revision: "19"
effective_year: "2025"
total_headings: 10
total_subheadings: 89
exclusions_count: 4
special_programs_count: 1
```

## Table: chapter_notes
```sql
note_id: 1
note_type: "exclusion"
note_text: "Products of the kinds described in headings 0201 to 0208 or 0210, unfit or unsuitable for human consumption"
reference_headings: "0201,0202,0203,0204,0205,0206,0207,0208,0210"

note_id: 2
note_type: "exclusion" 
note_text: "Edible, non-living insects (heading 0410)"
reference_headings: "0410"

note_id: 3
note_type: "exclusion"
note_text: "Guts, bladders, or stomachs of animals (heading 0504) or animal blood (heading 0511 or 3002)"
reference_headings: "0504,0511,3002"

note_id: 4
note_type: "exclusion"
note_text: "Animal fat, other than products of heading 0209 (chapter 15)"
reference_headings: "15"
exception_heading: "0209"
```

## Table: us_additional_notes
```sql
us_note_id: 1
note_type: "definition"
note_title: "Processed meats"
note_text: "The term 'processed' covers meats which have been ground or comminuted, diced or cut into sizes for stew meat or similar uses, rolled and skewered, or specially processed into fancy cuts, special shapes, or otherwise made ready for particular uses by the retail consumer"
applies_to: "all_meat_products"
status: "active"

us_note_id: 2
note_type: "definition"  
note_title: "High-quality beef cuts"
note_text: "beef specially processed into fancy cuts, special shapes, or otherwise made ready for particular uses by the retail consumer, which meets the specifications in regulations issued by the U.S. Department of Agriculture for Prime or Choice beef, and which has been so certified prior to exportation"
applies_to: "beef_products"
certification_required: true
certifying_authority: "USDA"
status: "active"

us_note_id: 3
note_type: "quota_system"
note_title: "Beef TRQ System"
note_text: "The aggregate quantity of beef, entered under specified subheadings in any calendar year shall not exceed the quantities specified in this note"
applies_to: "beef_quota_subheadings"
quota_type: "TRQ"
quota_period: "calendar_year"
administered_by: "USTR"
status: "active"
```

## Table: trq_quotas
```sql
country: "Canada"
quota_amount: null
quota_unit: "metric_ton"
quota_type: "unlimited"
trade_program: "USMCA"
status: "active"

country: "Mexico"
quota_amount: null
quota_unit: "metric_ton" 
quota_type: "unlimited"
trade_program: "USMCA"
status: "active"

country: "Australia"
quota_amount: 378214
quota_unit: "metric_ton"
quota_type: "limited"
trade_program: "FTA"
status: "active"

country: "New Zealand"
quota_amount: 213402
quota_unit: "metric_ton"
quota_type: "limited"
trade_program: "quota"
status: "active"

country: "Argentina"
quota_amount: 20000
quota_unit: "metric_ton"
quota_type: "limited"
trade_program: "quota"
status: "active"

country: "Uruguay"
quota_amount: 20000
quota_unit: "metric_ton"
quota_type: "limited"
trade_program: "quota" 
status: "active"

country: "Other countries or areas"
quota_amount: 65005
quota_unit: "metric_ton"
quota_type: "limited"
trade_program: "quota"
status: "active"
```

---

# HEADING 02.01 - MEAT OF BOVINE ANIMALS, FRESH OR CHILLED

## Table: heading_0201
```sql
heading_code: "0201"
heading_description: "Meat of bovine animals, fresh or chilled"
heading_full_text: "Meat of bovine animals, fresh or chilled"
animal_family: "Bovidae"
scientific_classification: "Bos taurus, Bos indicus"
temperature_range: "fresh_or_chilled"
temperature_min: -1
temperature_max: 4
temperature_unit: "celsius"
```

## Table: subheadings_0201
```sql
subheading_code: "0201.10"
subheading_description: "Carcasses and half-carcasses"
classification_criteria: "cut_type"
cut_type: "whole_carcass"
processing_level: "minimal"

subheading_code: "0201.20"
subheading_description: "Other cuts with bone in"
classification_criteria: "cut_type_processing"
cut_type: "bone_in_cuts"
bone_status: "bone_in"
processing_level: "variable"

subheading_code: "0201.30"
subheading_description: "Boneless"
classification_criteria: "cut_type_processing"
cut_type: "boneless_cuts"
bone_status: "boneless"
processing_level: "variable"
```

## Table: statistical_codes_0201
```sql
statistical_code: "0201.10.05.10"
description: "Veal"
parent_subheading: "0201.10.05"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "young"
animal_type: "veal"
quota_program: "general_note_15"
meat_grade: "all"

statistical_code: "0201.10.05.90"
description: "Other"
parent_subheading: "0201.10.05"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "mature"
animal_type: "beef"
quota_program: "general_note_15"
meat_grade: "all"

statistical_code: "0201.10.10.10"
description: "Veal"
parent_subheading: "0201.10.10"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "young"
animal_type: "veal"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.10.10.90"
description: "Other"
parent_subheading: "0201.10.10"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "mature"
animal_type: "beef"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.10.50.10"
description: "Veal"
parent_subheading: "0201.10.50"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "young"
animal_type: "veal"
quota_program: "other"
trq_eligible: false

statistical_code: "0201.10.50.90"
description: "Other"
parent_subheading: "0201.10.50"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "mature"
animal_type: "beef"
quota_program: "other"
trq_eligible: false

statistical_code: "0201.20.02.00"
description: "High-quality beef cuts"
parent_subheading: "0201.20.02"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "high_quality"
processing_type: "processed"
certification_required: true
certifying_authority: "USDA"
meat_grade: "prime_choice"
quota_program: "general_note_15"

statistical_code: "0201.20.04.00"
description: "Other"
parent_subheading: "0201.20.04"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "other_processed"
processing_type: "processed"
certification_required: false
meat_grade: "all"
quota_program: "general_note_15"

statistical_code: "0201.20.06.00"
description: "Other"
parent_subheading: "0201.20.06"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "natural"
processing_type: "unprocessed"
certification_required: false
meat_grade: "all"
quota_program: "general_note_15"

statistical_code: "0201.20.10.00"
description: "High-quality beef cuts"
parent_subheading: "0201.20.10"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "high_quality"
processing_type: "processed"
certification_required: true
certifying_authority: "USDA"
meat_grade: "prime_choice"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.20.30.00"
description: "Other"
parent_subheading: "0201.20.30"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "other_processed"
processing_type: "processed"
certification_required: false
meat_grade: "all"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.20.50.15"
description: "Fresh or chilled bone in veal cuts"
parent_subheading: "0201.20.50"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "young"
animal_type: "veal"
cut_classification: "bone_in"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.20.50.25"
description: "Rib cuts"
parent_subheading: "0201.20.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "rib"
cut_classification: "primal_cut"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.20.50.35"
description: "Chuck cuts"
parent_subheading: "0201.20.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "chuck"
cut_classification: "primal_cut"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.20.50.45"
description: "Loin cuts"
parent_subheading: "0201.20.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "loin"
cut_classification: "primal_cut"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.20.50.65"
description: "Hip cuts"
parent_subheading: "0201.20.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "hip"
cut_classification: "primal_cut"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.20.50.75"
description: "Flank or plate cuts"
parent_subheading: "0201.20.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "flank_plate"
cut_classification: "primal_cut"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.20.50.91"
description: "Other"
parent_subheading: "0201.20.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "other"
cut_classification: "other_cuts"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.20.80.10"
description: "Bison"
parent_subheading: "0201.20.80"
unit_of_quantity: "kg"
second_quantity: null
animal_species: "Bison bison"
quota_program: "other"
trq_eligible: false

statistical_code: "0201.20.80.90"
description: "Other"
parent_subheading: "0201.20.80"
unit_of_quantity: "kg"
second_quantity: null
animal_species: "Bos taurus"
quota_program: "other"
trq_eligible: false

statistical_code: "0201.30.02.00"
description: "High-quality beef cuts"
parent_subheading: "0201.30.02"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "high_quality"
processing_type: "processed"
certification_required: true
certifying_authority: "USDA"
meat_grade: "prime_choice"
quota_program: "general_note_15"
cut_classification: "boneless"

statistical_code: "0201.30.04.00"
description: "Other"
parent_subheading: "0201.30.04"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "other_processed"
processing_type: "processed"
certification_required: false
meat_grade: "all"
quota_program: "general_note_15"
cut_classification: "boneless"

statistical_code: "0201.30.06.00"
description: "Other"
parent_subheading: "0201.30.06"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "natural"
processing_type: "unprocessed"
certification_required: false
meat_grade: "all"
quota_program: "general_note_15"
cut_classification: "boneless"

statistical_code: "0201.30.10.00"
description: "High-quality beef cuts"
parent_subheading: "0201.30.10"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "high_quality"
processing_type: "processed"
certification_required: true
certifying_authority: "USDA"
meat_grade: "prime_choice"
quota_program: "us_note_3"
trq_eligible: true
cut_classification: "boneless"

statistical_code: "0201.30.30.00"
description: "Other"
parent_subheading: "0201.30.30"
unit_of_quantity: "kg"
second_quantity: null
processing_level: "other_processed"
processing_type: "processed"
certification_required: false
meat_grade: "all"
quota_program: "us_note_3"
trq_eligible: true
cut_classification: "boneless"

statistical_code: "0201.30.50.15"
description: "Fresh or chilled boneless veal cuts"
parent_subheading: "0201.30.50"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "young"
animal_type: "veal"
cut_classification: "boneless"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.30.50.25"
description: "Rib cuts"
parent_subheading: "0201.30.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "rib"
cut_classification: "boneless_primal"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.30.50.35"
description: "Chuck cuts"
parent_subheading: "0201.30.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "chuck"
cut_classification: "boneless_primal"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.30.50.45"
description: "Loin cuts"
parent_subheading: "0201.30.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "loin"
cut_classification: "boneless_primal"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.30.50.55"
description: "Brisket cuts"
parent_subheading: "0201.30.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "brisket"
cut_classification: "boneless_primal"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.30.50.65"
description: "Hip cuts"
parent_subheading: "0201.30.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "hip"
cut_classification: "boneless_primal"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.30.50.75"
description: "Flank or plate cuts"
parent_subheading: "0201.30.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "flank_plate"
cut_classification: "boneless_primal"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.30.50.85"
description: "Other"
parent_subheading: "0201.30.50"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "other"
cut_classification: "boneless_other"
temperature_state: "fresh_or_chilled"
quota_program: "us_note_3"
trq_eligible: true

statistical_code: "0201.30.80.10"
description: "Bison"
parent_subheading: "0201.30.80"
unit_of_quantity: "kg"
second_quantity: null
animal_species: "Bison bison"
cut_classification: "boneless"
quota_program: "other"
trq_eligible: false

statistical_code: "0201.30.80.90"
description: "Other"
parent_subheading: "0201.30.80"
unit_of_quantity: "kg"
second_quantity: null
animal_species: "Bos taurus"
cut_classification: "boneless"
quota_program: "other"
trq_eligible: false
```

## Table: duty_rates_0201
```sql
statistical_code: "0201.10.05"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "13.2¢/kg"
special_rate_numeric: 13.20
special_rate_type: "specific"
footnote: "4.4¢/kg"
unit_of_duty: "per_kg"
quota_program: "general_note_15"

statistical_code: "0201.10.10"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "13.2¢/kg"
special_rate_numeric: 13.20
special_rate_type: "specific"
footnote: "4.4¢/kg"
unit_of_duty: "per_kg"
quota_program: "us_note_3"

statistical_code: "0201.10.50"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "31.1%"
special_rate_numeric: 31.10
special_rate_type: "ad_valorem"
footnote: "26.4%"
unit_of_duty: "per_unit"
quota_program: "other"

statistical_code: "0201.20.02"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "4%"
unit_of_duty: "per_kg"
processing_level: "high_quality"

statistical_code: "0201.20.04"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "10%"
unit_of_duty: "per_kg"
processing_level: "other_processed"

statistical_code: "0201.20.06"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "13.2¢/kg"
special_rate_numeric: 13.20
special_rate_type: "specific"
footnote: "4.4¢/kg"
unit_of_duty: "per_kg"
processing_level: "natural"

statistical_code: "0201.20.10"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "4%"
unit_of_duty: "per_kg"
processing_level: "high_quality"
trq_eligible: true

statistical_code: "0201.20.30"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "10%"
unit_of_duty: "per_kg"
processing_level: "other_processed"
trq_eligible: true

statistical_code: "0201.20.50"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "13.2¢/kg"
special_rate_numeric: 13.20
special_rate_type: "specific"
footnote: "4.4¢/kg"
unit_of_duty: "per_kg"
processing_level: "natural"
trq_eligible: true

statistical_code: "0201.20.80"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "31.1%"
special_rate_numeric: 31.10
special_rate_type: "ad_valorem"
footnote: "26.4%"
unit_of_duty: "per_unit"
quota_program: "other"

statistical_code: "0201.30.02"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "4%"
unit_of_duty: "per_kg"
processing_level: "high_quality"

statistical_code: "0201.30.04"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "10%"
unit_of_duty: "per_kg"
processing_level: "other_processed"

statistical_code: "0201.30.06"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "13.2¢/kg"
special_rate_numeric: 13.20
special_rate_type: "specific"
footnote: "4.4¢/kg"
unit_of_duty: "per_kg"
processing_level: "natural"

statistical_code: "0201.30.10"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "4%"
unit_of_duty: "per_kg"
processing_level: "high_quality"
trq_eligible: true

statistical_code: "0201.30.30"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "10%"
unit_of_duty: "per_kg"
processing_level: "other_processed"
trq_eligible: true

statistical_code: "0201.30.50"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "13.2¢/kg"
special_rate_numeric: 13.20
special_rate_type: "specific"
footnote: "4.4¢/kg"
unit_of_duty: "per_kg"
processing_level: "natural"
trq_eligible: true

statistical_code: "0201.30.80"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "31.1%"
special_rate_numeric: 31.10
special_rate_type: "ad_valorem"
footnote: "26.4%"
unit_of_duty: "per_unit"
quota_program: "other"
```

---

# HEADING 02.02 - MEAT OF BOVINE ANIMALS, FROZEN

## Table: heading_0202
```sql
heading_code: "0202"
heading_description: "Meat of bovine animals, frozen"
heading_full_text: "Meat of bovine animals, frozen"
animal_family: "Bovidae"
scientific_classification: "Bos taurus, Bos indicus"
temperature_range: "frozen"
temperature_min: -18
temperature_max: -10
temperature_unit: "celsius"
```

## Table: subheadings_0202
```sql
subheading_code: "0202.10"
subheading_description: "Carcasses and half-carcasses"
classification_criteria: "cut_type"
cut_type: "whole_carcass"
processing_level: "minimal"
temperature_state: "frozen"

subheading_code: "0202.20"
subheading_description: "Other cuts with bone in"
classification_criteria: "cut_type_processing"
cut_type: "bone_in_cuts"
bone_status: "bone_in"
processing_level: "variable"
temperature_state: "frozen"

subheading_code: "0202.30"
subheading_description: "Boneless"
classification_criteria: "cut_type_processing"
cut_type: "boneless_cuts"
bone_status: "boneless"
processing_level: "variable"
temperature_state: "frozen"
```

## Table: statistical_codes_0202
```sql
statistical_code: "0202.10.05.10"
description: "Veal"
parent_subheading: "0202.10.05"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "young"
animal_type: "veal"
quota_program: "general_note_15"
temperature_state: "frozen"

statistical_code: "0202.10.05.90"
description: "Other"
parent_subheading: "0202.10.05"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "mature"
animal_type: "beef"
quota_program: "general_note_15"
temperature_state: "frozen"

statistical_code: "0202.10.10.10"
description: "Veal"
parent_subheading: "0202.10.10"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "young"
animal_type: "veal"
quota_program: "us_note_3"
trq_eligible: true
temperature_state: "frozen"

statistical_code: "0202.10.10.90"
description: "Other"
parent_subheading: "0202.10.10"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "mature"
animal_type: "beef"
quota_program: "us_note_3"
trq_eligible: true
temperature_state: "frozen"

statistical_code: "0202.10.50.10"
description: "Veal"
parent_subheading: "0202.10.50"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "young"
animal_type: "veal"
quota_program: "other"
trq_eligible: false
temperature_state: "frozen"

statistical_code: "0202.10.50.90"
description: "Other"
parent_subheading: "0202.10.50"
unit_of_quantity: "kg"
second_quantity: null
animal_age: "mature"
animal_type: "beef"
quota_program: "other"
trq_eligible: false
temperature_state: "frozen"
```

## Table: duty_rates_0202
```sql
statistical_code: "0202.10.05"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "13.2¢/kg"
special_rate_numeric: 13.20
special_rate_type: "specific"
footnote: "4.4¢/kg"
unit_of_duty: "per_kg"
quota_program: "general_note_15"
temperature_state: "frozen"

statistical_code: "0202.10.10"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "13.2¢/kg"
special_rate_numeric: 13.20
special_rate_type: "specific"
footnote: "4.4¢/kg"
unit_of_duty: "per_kg"
quota_program: "us_note_3"
temperature_state: "frozen"

statistical_code: "0202.10.50"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "31.1%"
special_rate_numeric: 31.10
special_rate_type: "ad_valorem"
footnote: "26.4%"
unit_of_duty: "per_unit"
quota_program: "other"
temperature_state: "frozen"
```

---

# HEADING 02.03 - MEAT OF SWINE

## Table: heading_0203
```sql
heading_code: "0203"
heading_description: "Meat of swine, fresh, chilled, or frozen"
heading_full_text: "Meat of swine, fresh, chilled, or frozen"
animal_family: "Suidae"
scientific_classification: "Sus scrofa domesticus"
temperature_range: "fresh_chilled_frozen"
```

## Table: subheadings_0203
```sql
subheading_code: "0203.11"
subheading_description: "Carcasses and half-carcasses"
classification_criteria: "cut_type_temperature"
cut_type: "whole_carcass"
temperature_state: "fresh_or_chilled"
processing_level: "minimal"

subheading_code: "0203.12"
subheading_description: "Hams, shoulders and cuts thereof, with bone in"
classification_criteria: "cut_type_processing_temperature"
cut_type: "hams_shoulders"
bone_status: "bone_in"
temperature_state: "fresh_or_chilled"
processing_level: "variable"

subheading_code: "0203.19"
subheading_description: "Other"
classification_criteria: "cut_type_processing_temperature"
cut_type: "other_cuts"
temperature_state: "fresh_or_chilled"
processing_level: "variable"

subheading_code: "0203.21"
subheading_description: "Carcasses and half-carcasses"
classification_criteria: "cut_type_temperature"
cut_type: "whole_carcass"
temperature_state: "frozen"
processing_level: "minimal"

subheading_code: "0203.22"
subheading_description: "Hams, shoulders and cuts thereof, with bone in"
classification_criteria: "cut_type_processing_temperature"
cut_type: "hams_shoulders"
bone_status: "bone_in"
temperature_state: "frozen"
processing_level: "variable"

subheading_code: "0203.29"
subheading_description: "Other"
classification_criteria: "cut_type_processing_temperature"
cut_type: "other_cuts"
temperature_state: "frozen"
processing_level: "variable"
```

## Table: statistical_codes_0203
```sql
statistical_code: "0203.11.00.00"
description: "Carcasses and half-carcasses"
parent_subheading: "0203.11.00"
unit_of_quantity: "kg"
second_quantity: null
cut_type: "whole_carcass"
temperature_state: "fresh_or_chilled"
processing_level: "minimal"

statistical_code: "0203.12.10.10"
description: "Hams and cuts thereof"
parent_subheading: "0203.12.10"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "ham"
cut_type: "hams"
bone_status: "bone_in"
processing_level: "processed"
temperature_state: "fresh_or_chilled"

statistical_code: "0203.12.10.20"
description: "Shoulders and cuts thereof"
parent_subheading: "0203.12.10"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "shoulder"
cut_type: "shoulders"
bone_status: "bone_in"
processing_level: "processed"
temperature_state: "fresh_or_chilled"

statistical_code: "0203.12.90.10"
description: "Hams and cuts thereof"
parent_subheading: "0203.12.90"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "ham"
cut_type: "hams"
bone_status: "bone_in"
processing_level: "natural"
temperature_state: "fresh_or_chilled"

statistical_code: "0203.12.90.20"
description: "Shoulders and cuts thereof"
parent_subheading: "0203.12.90"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "shoulder"
cut_type: "shoulders"
bone_status: "bone_in"
processing_level: "natural"
temperature_state: "fresh_or_chilled"

statistical_code: "0203.19.20.10"
description: "Spare ribs"
parent_subheading: "0203.19.20"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "ribs"
cut_type: "spare_ribs"
processing_level: "processed"
temperature_state: "fresh_or_chilled"

statistical_code: "0203.19.20.90"
description: "Other"
parent_subheading: "0203.19.20"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "other"
cut_type: "other_cuts"
processing_level: "processed"
temperature_state: "fresh_or_chilled"

statistical_code: "0203.19.40.10"
description: "Bellies"
parent_subheading: "0203.19.40"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "belly"
cut_type: "bellies"
processing_level: "natural"
temperature_state: "fresh_or_chilled"

statistical_code: "0203.19.40.90"
description: "Other"
parent_subheading: "0203.19.40"
unit_of_quantity: "kg"
second_quantity: null
cut_location: "other"
cut_type: "other_cuts"
processing_level: "natural"
temperature_state: "fresh_or_chilled"

statistical_code: "0203.21.00.00"
description: "Carcasses and half-carcasses"
parent_subheading: "0203.21.00"
unit_of_quantity: "kg"
second_quantity: null
cut_type: "whole_carcass"
temperature_state: "frozen"
processing_level: "minimal"

statistical_code: "0203.22.10.00"
description: "Processed"
parent_subheading: "0203.22.10"
unit_of_quantity: "kg"
second_quantity: null
cut_type: "hams_shoulders"
bone_status: "bone_in"
processing_level: "processed"
temperature_state: "frozen"

statistical_code: "0203.22.90.00"
description: "Other"
parent_subheading: "0203.22.90"
unit_of_quantity: "kg"
second_quantity: null
cut_type: "hams_shoulders"
bone_status: "bone_in"
processing_level: "natural"
temperature_state: "frozen"

statistical_code: "0203.29.20.00"
description: "Processed"
parent_subheading: "0203.29.20"
unit_of_quantity: "kg"
second_quantity: null
cut_type: "other_cuts"
processing_level: "processed"
temperature_state: "frozen"

statistical_code: "0203.29.40.00"
description: "Other"
parent_subheading: "0203.29.40"
unit_of_quantity: "kg"
second_quantity: null
cut_type: "other_cuts"
processing_level: "natural"
temperature_state: "frozen"
```

## Table: duty_rates_0203
```sql
statistical_code: "0203.11.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "5.5¢/kg"
special_rate_numeric: 5.50
special_rate_type: "specific"
unit_of_duty: "per_kg"

statistical_code: "0203.12.10"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "7.2¢/kg"
special_rate_numeric: 7.20
special_rate_type: "specific"
footnote: "1.4¢/kg"
unit_of_duty: "per_kg"
processing_level: "processed"

statistical_code: "0203.12.90"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "5.5¢/kg"
special_rate_numeric: 5.50
special_rate_type: "specific"
unit_of_duty: "per_kg"
processing_level: "natural"

statistical_code: "0203.19.20"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "7.2¢/kg"
special_rate_numeric: 7.20
special_rate_type: "specific"
footnote: "1.4¢/kg"
unit_of_duty: "per_kg"
processing_level: "processed"

statistical_code: "0203.19.40"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "5.5¢/kg"
special_rate_numeric: 5.50
special_rate_type: "specific"
unit_of_duty: "per_kg"
processing_level: "natural"

statistical_code: "0203.21.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "5.5¢/kg"
special_rate_numeric: 5.50
special_rate_type: "specific"
unit_of_duty: "per_kg"

statistical_code: "0203.22.10"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "7.2¢/kg"
special_rate_numeric: 7.20
special_rate_type: "specific"
footnote: "1.4¢/kg"
unit_of_duty: "per_kg"
processing_level: "processed"

statistical_code: "0203.22.90"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "5.5¢/kg"
special_rate_numeric: 5.50
special_rate_type: "specific"
unit_of_duty: "per_kg"
processing_level: "natural"

statistical_code: "0203.29.20"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "7.2¢/kg"
special_rate_numeric: 7.20
special_rate_type: "specific"
footnote: "1.4¢/kg"
unit_of_duty: "per_kg"
processing_level: "processed"

statistical_code: "0203.29.40"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "5.5¢/kg"
special_rate_numeric: 5.50
special_rate_type: "specific"
unit_of_duty: "per_kg"
processing_level: "natural"
```

---

# HEADING 02.04 - MEAT OF SHEEP OR GOATS

## Table: heading_0204
```sql
heading_code: "0204"
heading_description: "Meat of sheep or goats, fresh, chilled or frozen"
heading_full_text: "Meat of sheep or goats, fresh, chilled or frozen"
animal_family: "Bovidae"
scientific_classification: "Ovis aries, Capra hircus"
temperature_range: "fresh_chilled_frozen"
age_based_classification: true
```

## Table: subheadings_0204
```sql
subheading_code: "0204.10"
subheading_description: "Carcasses and half-carcasses of lamb, fresh or chilled"
classification_criteria: "age_temperature_cut"
animal_type: "lamb"
animal_age: "young"
cut_type: "whole_carcass"
temperature_state: "fresh_or_chilled"

subheading_code: "0204.21"
subheading_description: "Carcasses and half-carcasses"
classification_criteria: "age_temperature_cut"
animal_type: "sheep"
animal_age: "mature"
cut_type: "whole_carcass"
temperature_state: "fresh_or_chilled"

subheading_code: "0204.22"
subheading_description: "Other cuts with bone in"
classification_criteria: "age_temperature_cut"
animal_type: "sheep_lamb"
cut_type: "bone_in_cuts"
bone_status: "bone_in"
temperature_state: "fresh_or_chilled"

subheading_code: "0204.23"
subheading_description: "Boneless"
classification_criteria: "age_temperature_cut"
animal_type: "sheep_lamb"
cut_type: "boneless_cuts"
bone_status: "boneless"
temperature_state: "fresh_or_chilled"

subheading_code: "0204.30"
subheading_description: "Carcasses and half-carcasses of lamb, frozen"
classification_criteria: "age_temperature_cut"
animal_type: "lamb"
animal_age: "young"
cut_type: "whole_carcass"
temperature_state: "frozen"

subheading_code: "0204.41"
subheading_description: "Carcasses and half-carcasses"
classification_criteria: "age_temperature_cut"
animal_type: "sheep"
animal_age: "mature"
cut_type: "whole_carcass"
temperature_state: "frozen"

subheading_code: "0204.42"
subheading_description: "Other cuts with bone in"
classification_criteria: "age_temperature_cut"
animal_type: "sheep_lamb"
cut_type: "bone_in_cuts"
bone_status: "bone_in"
temperature_state: "frozen"

subheading_code: "0204.43"
subheading_description: "Boneless"
classification_criteria: "age_temperature_cut"
animal_type: "sheep_lamb"
cut_type: "boneless_cuts"
bone_status: "boneless"
temperature_state: "frozen"

subheading_code: "0204.50"
subheading_description: "Meat of goats"
classification_criteria: "species"
animal_type: "goats"
species: "Capra hircus"
temperature_state: "all"
```

## Table: statistical_codes_0204
```sql
statistical_code: "0204.10.00.00"
description: "Carcasses and half-carcasses of lamb, fresh or chilled"
parent_subheading: "0204.10.00"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "lamb"
animal_age: "young"
cut_type: "whole_carcass"
temperature_state: "fresh_or_chilled"

statistical_code: "0204.21.00.00"
description: "Carcasses and half-carcasses"
parent_subheading: "0204.21.00"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "sheep"
animal_age: "mature"
cut_type: "whole_carcass"
temperature_state: "fresh_or_chilled"

statistical_code: "0204.22.20.10"
description: "Shoulders"
parent_subheading: "0204.22.20"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "lamb"
cut_location: "shoulder"
cut_type: "bone_in_primal"
bone_status: "bone_in"
temperature_state: "fresh_or_chilled"

statistical_code: "0204.22.20.20"
description: "Legs"
parent_subheading: "0204.22.20"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "lamb"
cut_location: "leg"
cut_type: "bone_in_primal"
bone_status: "bone_in"
temperature_state: "fresh_or_chilled"

statistical_code: "0204.22.20.30"
description: "Loins"
parent_subheading: "0204.22.20"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "lamb"
cut_location: "loin"
cut_type: "bone_in_primal"
bone_status: "bone_in"
temperature_state: "fresh_or_chilled"

statistical_code: "0204.22.20.90"
description: "Other"
parent_subheading: "0204.22.20"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "lamb"
cut_location: "other"
cut_type: "bone_in_other"
bone_status: "bone_in"
temperature_state: "fresh_or_chilled"

statistical_code: "0204.22.40.00"
description: "Other"
parent_subheading: "0204.22.40"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "sheep"
animal_age: "mature"
cut_type: "bone_in_cuts"
bone_status: "bone_in"
temperature_state: "fresh_or_chilled"

statistical_code: "0204.23.20.00"
description: "Lamb"
parent_subheading: "0204.23.20"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "lamb"
animal_age: "young"
cut_type: "boneless_cuts"
bone_status: "boneless"
temperature_state: "fresh_or_chilled"

statistical_code: "0204.23.40.00"
description: "Other"
parent_subheading: "0204.23.40"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "sheep"
animal_age: "mature"
cut_type: "boneless_cuts"
bone_status: "boneless"
temperature_state: "fresh_or_chilled"

statistical_code: "0204.30.00.00"
description: "Carcasses and half-carcasses of lamb, frozen"
parent_subheading: "0204.30.00"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "lamb"
animal_age: "young"
cut_type: "whole_carcass"
temperature_state: "frozen"

statistical_code: "0204.50.00.00"
description: "Meat of goats"
parent_subheading: "0204.50.00"
unit_of_quantity: "kg"
second_quantity: null
animal_type: "goats"
species: "Capra hircus"
temperature_state: "all"
```

## Table: duty_rates_0204
```sql
statistical_code: "0204.10.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15.4¢/kg"
special_rate_numeric: 15.40
special_rate_type: "specific"
footnote: "0.7¢/kg"
unit_of_duty: "per_kg"
animal_type: "lamb"

statistical_code: "0204.21.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "11¢/kg"
special_rate_numeric: 11.00
special_rate_type: "specific"
footnote: "2.8¢/kg"
unit_of_duty: "per_kg"
animal_type: "sheep"

statistical_code: "0204.22.20"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15.4¢/kg"
special_rate_numeric: 15.40
special_rate_type: "specific"
footnote: "0.7¢/kg"
unit_of_duty: "per_kg"
animal_type: "lamb"

statistical_code: "0204.22.40"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "11¢/kg"
special_rate_numeric: 11.00
special_rate_type: "specific"
footnote: "2.8¢/kg"
unit_of_duty: "per_kg"
animal_type: "sheep"

statistical_code: "0204.23.20"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15.4¢/kg"
special_rate_numeric: 15.40
special_rate_type: "specific"
footnote: "0.7¢/kg"
unit_of_duty: "per_kg"
animal_type: "lamb"

statistical_code: "0204.23.40"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "11¢/kg"
special_rate_numeric: 11.00
special_rate_type: "specific"
footnote: "2.8¢/kg"
unit_of_duty: "per_kg"
animal_type: "sheep"

statistical_code: "0204.30.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15.4¢/kg"
special_rate_numeric: 15.40
special_rate_type: "specific"
footnote: "0.7¢/kg"
unit_of_duty: "per_kg"
animal_type: "lamb"

statistical_code: "0204.50.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "11¢/kg"
special_rate_numeric: 11.00
special_rate_type: "specific"
unit_of_duty: "per_kg"
animal_type: "goats"
```

---

# HEADING 02.05 - MEAT OF HORSES, ASSES, MULES OR HINNIES

## Table: heading_0205
```sql
heading_code: "0205"
heading_description: "Meat of horses, asses, mules or hinnies, fresh, chilled or frozen"
heading_full_text: "Meat of horses, asses, mules or hinnies, fresh, chilled or frozen"
animal_family: "Equidae"
scientific_classification: "Equus caballus, Equus asinus"
temperature_range: "fresh_chilled_frozen"
single_classification: true
```

## Table: subheadings_0205
```sql
subheading_code: "0205.00"
subheading_description: "Meat of horses, asses, mules or hinnies, fresh, chilled or frozen"
classification_criteria: "species_only"
animal_family: "Equidae"
temperature_state: "all"
single_subheading: true
```

## Table: statistical_codes_0205
```sql
statistical_code: "0205.00.00.00"
description: "Meat of horses, asses, mules or hinnies, fresh, chilled or frozen"
parent_subheading: "0205.00.00"
unit_of_quantity: "kg"
second_quantity: null
animal_family: "Equidae"
species_included: "Equus caballus, Equus asinus, hybrids"
temperature_state: "all"
```

## Table: duty_rates_0205
```sql
statistical_code: "0205.00.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"
```

---

# HEADING 02.06 - EDIBLE OFFAL

## Table: heading_0206
```sql
heading_code: "0206"
heading_description: "Edible offal of bovine animals, swine, sheep, goats, horses, asses, mules or hinnies, fresh, chilled or frozen"
heading_full_text: "Edible offal of bovine animals, swine, sheep, goats, horses, asses, mules or hinnies, fresh, chilled or frozen"
coverage: "multiple_species"
product_type: "offal"
temperature_range: "fresh_chilled_frozen"
```

## Table: subheadings_0206
```sql
subheading_code: "0206.10"
subheading_description: "Of bovine animals, fresh or chilled"
classification_criteria: "species_temperature"
animal_source: "bovine"
temperature_state: "fresh_or_chilled"

subheading_code: "0206.21"
subheading_description: "Tongues"
classification_criteria: "species_organ_temperature"
animal_source: "bovine"
organ_type: "tongues"
temperature_state: "frozen"

subheading_code: "0206.22"
subheading_description: "Livers"
classification_criteria: "species_organ_temperature"
animal_source: "bovine"
organ_type: "livers"
temperature_state: "frozen"

subheading_code: "0206.29"
subheading_description: "Other"
classification_criteria: "species_organ_temperature"
animal_source: "bovine"
organ_type: "other"
temperature_state: "frozen"

subheading_code: "0206.30"
subheading_description: "Of swine, fresh or chilled"
classification_criteria: "species_temperature"
animal_source: "swine"
temperature_state: "fresh_or_chilled"

subheading_code: "0206.41"
subheading_description: "Livers"
classification_criteria: "species_organ_temperature"
animal_source: "swine"
organ_type: "livers"
temperature_state: "frozen"

subheading_code: "0206.49"
subheading_description: "Other"
classification_criteria: "species_organ_temperature"
animal_source: "swine"
organ_type: "other"
temperature_state: "frozen"

subheading_code: "0206.80"
subheading_description: "Other, fresh or chilled"
classification_criteria: "species_temperature"
animal_source: "other"
temperature_state: "fresh_or_chilled"

subheading_code: "0206.90"
subheading_description: "Other, frozen"
classification_criteria: "species_temperature"
animal_source: "other"
temperature_state: "frozen"
```

## Table: statistical_codes_0206
```sql
statistical_code: "0206.10.00.00"
description: "Of bovine animals, fresh or chilled"
parent_subheading: "0206.10.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "bovine"
organ_type: "all"
temperature_state: "fresh_or_chilled"

statistical_code: "0206.21.00.00"
description: "Tongues"
parent_subheading: "0206.21.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "bovine"
organ_type: "tongues"
temperature_state: "frozen"

statistical_code: "0206.22.00.00"
description: "Livers"
parent_subheading: "0206.22.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "bovine"
organ_type: "livers"
temperature_state: "frozen"

statistical_code: "0206.29.00.00"
description: "Other"
parent_subheading: "0206.29.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "bovine"
organ_type: "other"
temperature_state: "frozen"

statistical_code: "0206.30.00.00"
description: "Of swine, fresh or chilled"
parent_subheading: "0206.30.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "swine"
organ_type: "all"
temperature_state: "fresh_or_chilled"

statistical_code: "0206.41.00.00"
description: "Livers"
parent_subheading: "0206.41.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "swine"
organ_type: "livers"
temperature_state: "frozen"

statistical_code: "0206.49.00.00"
description: "Other"
parent_subheading: "0206.49.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "swine"
organ_type: "other"
temperature_state: "frozen"

statistical_code: "0206.80.00.00"
description: "Other, fresh or chilled"
parent_subheading: "0206.80.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "sheep_goats_equine"
organ_type: "all"
temperature_state: "fresh_or_chilled"

statistical_code: "0206.90.00.20"
description: "Of sheep (including lamb)"
parent_subheading: "0206.90.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "sheep"
organ_type: "all"
temperature_state: "frozen"

statistical_code: "0206.90.00.40"
description: "Of goats, horses, asses, mules or hinnies"
parent_subheading: "0206.90.00"
unit_of_quantity: "kg"
second_quantity: null
animal_source: "goats_equine"
organ_type: "all"
temperature_state: "frozen"
```

## Table: duty_rates_0206
```sql
statistical_code: "0206.10.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "30%"
special_rate_numeric: 30.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0206.21.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "30%"
special_rate_numeric: 30.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0206.22.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "30%"
special_rate_numeric: 30.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0206.29.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "30%"
special_rate_numeric: 30.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0206.30.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "30%"
special_rate_numeric: 30.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0206.41.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "30%"
special_rate_numeric: 30.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0206.49.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "30%"
special_rate_numeric: 30.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0206.80.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "30%"
special_rate_numeric: 30.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0206.90.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "30%"
special_rate_numeric: 30.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"
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

-- Temperature-sensitive products must have:
temperature_state: NOT NULL IN ("fresh", "chilled", "frozen", "fresh_or_chilled", "all")

-- Processing classification must be consistent:
processing_level: IN ("minimal", "processed", "high_quality", "other_processed", "natural")
```

## Business Rules Validation
```sql
-- TRQ eligibility rules
IF trq_eligible = true THEN quota_program MUST BE "us_note_3"

-- Processing level consistency
IF processing_level = "high_quality" THEN certification_required = true
IF certification_required = true THEN certifying_authority IS NOT NULL

-- Temperature state logic
IF temperature_state = "frozen" THEN temperature_min <= -10

-- Age-based classification for sheep
IF animal_type = "lamb" THEN special_rate_numeric < sheep_rate_numeric

-- Statistical codes must match parent subheading pattern
statistical_code LIKE parent_subheading + "%"
```

## Chapter-Specific Validation
```sql
-- Beef quota validation
IF quota_program = "us_note_3" THEN trq_eligible = true
IF trq_eligible = true THEN country IN trq_quotas.country

-- Processing vs rate validation
IF processing_level = "high_quality" THEN special_rate_type = "ad_valorem"
IF processing_level = "natural" THEN special_rate_type IN ("specific", "ad_valorem")

-- Cut classification consistency
IF cut_type = "boneless_cuts" THEN bone_status = "boneless"
IF cut_type LIKE "%bone_in%" THEN bone_status = "bone_in"
```

---

**Database Schema Version**: 1.0  
**SQLite Compatible**: Yes  
**Python Scraping Ready**: Yes  
**Total Data Points**: 800+  
**Normalization Level**: 3NF  
**Last Updated**: August 25, 2025