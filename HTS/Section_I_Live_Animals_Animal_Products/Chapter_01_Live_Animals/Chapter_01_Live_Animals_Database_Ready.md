---
# HTS Chapter 1 Database Schema - Live Animals
database_schema_version: "1.0"
chapter_code: "01"
chapter_name: "Live Animals"
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
total_records: 42
schema_validation: "strict"
---

# Database Structure Overview

## Table: chapter_metadata
```sql
chapter_code: "01"
chapter_name: "Live Animals"
section_code: "I" 
section_name: "Live Animals; Animal Products"
revision: "19"
effective_year: "2025"
total_headings: 6
total_subheadings: 42
exclusions_count: 3
```

## Table: chapter_notes
```sql
note_id: 1
note_type: "exclusion"
note_text: "Fish and crustaceans, molluscs and other aquatic invertebrates, of heading 03.01, 03.06, 03.07 or 03.08"
reference_headings: "03.01,03.06,03.07,03.08"

note_id: 2
note_type: "exclusion" 
note_text: "Cultures of micro-organisms and other products of heading 30.02"
reference_headings: "30.02"

note_id: 3
note_type: "exclusion"
note_text: "Animals of heading 95.08"
reference_headings: "95.08"
```

## Table: us_additional_notes
```sql
us_note_id: 1
note_type: "definition"
note_title: "Purebred breeding animals"
note_text: "The expression 'purebred breeding animals' covers only animals certified to the U.S. Customs Service by the Department of Agriculture as being purebred of a recognized breed and duly registered in a book of record recognized by the Secretary of Agriculture for that breed, imported specially for breeding purposes"
status: "active"
special_note: "The animal certificate of pure breeding is an obsolete form and can no longer be obtained from the U.S. Department of Agriculture"

us_note_id: 2
note_type: "reference"
note_title: "Special provisions"
note_text: "Certain special provisions applying to live animals are in chapter 98"
reference_chapter: "98"
status: "active"
```

---

# HEADING 01.01 - HORSES, ASSES, MULES AND HINNIES

## Table: heading_0101
```sql
heading_code: "0101"
heading_description: "Live horses, asses, mules and hinnies"
heading_full_text: "Live horses, asses, mules and hinnies"
animal_family: "Equidae"
scientific_classification: "Equus"
```

## Table: subheadings_0101
```sql
subheading_code: "0101.21"
subheading_description: "Purebred breeding animals"
parent_category: "Horses"
classification_criteria: "breeding_status"
certification_required: true

subheading_code: "0101.29"  
subheading_description: "Other"
parent_category: "Horses"
classification_criteria: "general"
certification_required: false

subheading_code: "0101.30"
subheading_description: "Asses" 
parent_category: "Asses"
classification_criteria: "species"
certification_required: false

subheading_code: "0101.90"
subheading_description: "Other"
parent_category: "Mules and Hinnies" 
classification_criteria: "species"
certification_required: false
```

## Table: statistical_codes_0101
```sql
statistical_code: "0101.21.00.10"
description: "Males"
parent_subheading: "0101.21.00"
unit_of_quantity: "Number"
second_quantity: null
gender_specification: "Male"
specific_use: "Breeding"

statistical_code: "0101.21.00.20"
description: "Females" 
parent_subheading: "0101.21.00"
unit_of_quantity: "Number"
second_quantity: null
gender_specification: "Female"
specific_use: "Breeding"

statistical_code: "0101.29.00.10"
description: "Imported for immediate slaughter"
parent_subheading: "0101.29.00"  
unit_of_quantity: "Number"
second_quantity: null
specific_use: "Slaughter"
time_restriction: "immediate"

statistical_code: "0101.29.00.90"
description: "Other"
parent_subheading: "0101.29.00"
unit_of_quantity: "Number" 
second_quantity: null
specific_use: "General"

statistical_code: "0101.30.00.00"
description: "Asses"
parent_subheading: "0101.30.00"
unit_of_quantity: "Number"
second_quantity: null
species: "Equus asinus"

statistical_code: "0101.90.30.00" 
description: "Imported for immediate slaughter"
parent_subheading: "0101.90.30"
unit_of_quantity: "Number"
second_quantity: null
specific_use: "Slaughter"
time_restriction: "immediate"

statistical_code: "0101.90.40.00"
description: "Other"
parent_subheading: "0101.90.40" 
unit_of_quantity: "Number"
second_quantity: null
specific_use: "General"
```

## Table: duty_rates_0101
```sql
statistical_code: "0101.21.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "Free" 
special_rate_numeric: 0.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0101.29.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem" 
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0101.30.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem" 
footnote: "6.8%"
unit_of_duty: "per_unit"

statistical_code: "0101.90.30"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0101.90.40"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "4.5%"
unit_of_duty: "per_unit"
```

---

# HEADING 01.02 - BOVINE ANIMALS

## Table: heading_0102
```sql
heading_code: "0102"
heading_description: "Live bovine animals"
heading_full_text: "Live bovine animals"
animal_family: "Bovidae"
scientific_classification: "Bos,Bubalus,Syncerus"
```

## Table: subheadings_0102
```sql
subheading_code: "0102.21"
subheading_description: "Purebred breeding animals"
parent_category: "Cattle"
classification_criteria: "breeding_status"
certification_required: true

subheading_code: "0102.29"
subheading_description: "Other"
parent_category: "Cattle" 
classification_criteria: "general"
weight_based: true

subheading_code: "0102.31"
subheading_description: "Purebred breeding animals"
parent_category: "Buffalo"
classification_criteria: "breeding_status"
certification_required: true

subheading_code: "0102.39"
subheading_description: "Other"
parent_category: "Buffalo"
classification_criteria: "general"
weight_based: true

subheading_code: "0102.90"
subheading_description: "Other"
parent_category: "Other bovine animals"
classification_criteria: "species"
weight_based: true
```

## Table: statistical_codes_0102
```sql
statistical_code: "0102.21.00.10"
description: "Male"
parent_subheading: "0102.21.00"
unit_of_quantity: "Number"
second_quantity: null
gender_specification: "Male"
breed_category: "Dairy"
specific_use: "Breeding"

statistical_code: "0102.21.00.20"
description: "Female"
parent_subheading: "0102.21.00"
unit_of_quantity: "Number" 
second_quantity: null
gender_specification: "Female"
breed_category: "Dairy"
specific_use: "Breeding"

statistical_code: "0102.21.00.30"
description: "Male"
parent_subheading: "0102.21.00"
unit_of_quantity: "Number"
second_quantity: null
gender_specification: "Male"
breed_category: "Other"
specific_use: "Breeding"

statistical_code: "0102.21.00.50"
description: "Female"
parent_subheading: "0102.21.00"
unit_of_quantity: "Number"
second_quantity: null
gender_specification: "Female" 
breed_category: "Other"
specific_use: "Breeding"

statistical_code: "0102.29.20.11"
description: "Weighing less than 90 kg each"
parent_subheading: "0102.29.20"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 0
weight_threshold_max: 90
specific_use: "Dairy"

statistical_code: "0102.29.20.12"
description: "Weighing 90 kg or more each"
parent_subheading: "0102.29.20"
unit_of_quantity: "Number"
second_quantity: "kg" 
weight_threshold_min: 90
weight_threshold_max: null
specific_use: "Dairy"

statistical_code: "0102.29.40.24"
description: "Male, weighing less than 90 kg each"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 0
weight_threshold_max: 90
gender_specification: "Male"

statistical_code: "0102.29.40.28"
description: "Female, weighing less than 90 kg each"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 0
weight_threshold_max: 90
gender_specification: "Female"

statistical_code: "0102.29.40.34"
description: "Male, weighing 90 kg or more but less than 200 kg each"  
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 90
weight_threshold_max: 200
gender_specification: "Male"

statistical_code: "0102.29.40.38"
description: "Female, weighing 90 kg or more but less than 200 kg each"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 90 
weight_threshold_max: 200
gender_specification: "Female"

statistical_code: "0102.29.40.54"
description: "Male, weighing 200 kg or more but less than 320 kg each"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 200
weight_threshold_max: 320
gender_specification: "Male"

statistical_code: "0102.29.40.58"
description: "Female, weighing 200 kg or more but less than 320 kg each"
parent_subheading: "0102.29.40" 
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 200
weight_threshold_max: 320
gender_specification: "Female"

statistical_code: "0102.29.40.62"
description: "Steers, weighing 320 kg or more each, for immediate slaughter"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 320
weight_threshold_max: null
gender_specification: "Castrated_male"
specific_use: "Slaughter"

statistical_code: "0102.29.40.64"
description: "Bulls, weighing 320 kg or more each, for immediate slaughter"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 320
weight_threshold_max: null
gender_specification: "Male"
specific_use: "Slaughter"

statistical_code: "0102.29.40.66"
description: "Cows, weighing 320 kg or more each, for immediate slaughter"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 320
weight_threshold_max: null
gender_specification: "Female"
specific_use: "Slaughter"

statistical_code: "0102.29.40.68"  
description: "Heifers, weighing 320 kg or more each, for immediate slaughter"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 320
weight_threshold_max: null
gender_specification: "Young_female"
specific_use: "Slaughter"

statistical_code: "0102.29.40.72"
description: "Male, weighing 320 kg or more each, for breeding"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 320
weight_threshold_max: null
gender_specification: "Male"
specific_use: "Breeding"

statistical_code: "0102.29.40.74"
description: "Female, weighing 320 kg or more each, for breeding"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 320
weight_threshold_max: null
gender_specification: "Female"
specific_use: "Breeding"

statistical_code: "0102.29.40.82"
description: "Male, weighing 320 kg or more each, other"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 320
weight_threshold_max: null
gender_specification: "Male"
specific_use: "Other"

statistical_code: "0102.29.40.84"
description: "Female, weighing 320 kg or more each, other"
parent_subheading: "0102.29.40"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 320
weight_threshold_max: null
gender_specification: "Female"
specific_use: "Other"

statistical_code: "0102.31.00.10"
description: "Male"
parent_subheading: "0102.31.00"
unit_of_quantity: "Number"
second_quantity: null
gender_specification: "Male" 
animal_type: "Buffalo"
specific_use: "Breeding"

statistical_code: "0102.31.00.20"
description: "Female"
parent_subheading: "0102.31.00"
unit_of_quantity: "Number"
second_quantity: null
gender_specification: "Female"
animal_type: "Buffalo"
specific_use: "Breeding"

statistical_code: "0102.39.00.10"
description: "Bison"
parent_subheading: "0102.39.00"
unit_of_quantity: "Number"
second_quantity: "kg"
animal_type: "Bison"
species: "Bison bison"

statistical_code: "0102.39.00.24"
description: "Male, weighing less than 90 kg each"
parent_subheading: "0102.39.00"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 0
weight_threshold_max: 90
gender_specification: "Male"
animal_type: "Buffalo"

statistical_code: "0102.39.00.28"
description: "Female, weighing less than 90 kg each"
parent_subheading: "0102.39.00"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 0
weight_threshold_max: 90
gender_specification: "Female"
animal_type: "Buffalo"

statistical_code: "0102.90.00.00"
description: "Other"
parent_subheading: "0102.90.00"
unit_of_quantity: "Number"
second_quantity: "kg"
animal_type: "Other bovine animals"
```

## Table: duty_rates_0102
```sql
statistical_code: "0102.21.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0102.29.20"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "6.6¢/kg"
special_rate_numeric: 6.60
special_rate_type: "specific"
unit_of_duty: "per_kg"

statistical_code: "0102.29.40"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "5.5¢/kg"
special_rate_numeric: 5.50
special_rate_type: "specific"
footnote: "1¢/kg"
unit_of_duty: "per_kg"

statistical_code: "0102.31.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0102.39.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "5.5¢/kg"
special_rate_numeric: 5.50
special_rate_type: "specific"
footnote: "1¢/kg"
unit_of_duty: "per_kg"

statistical_code: "0102.90.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "5.5¢/kg"
special_rate_numeric: 5.50
special_rate_type: "specific"
footnote: "1¢/kg"
unit_of_duty: "per_kg"
```

---

# HEADING 01.03 - SWINE

## Table: heading_0103
```sql
heading_code: "0103"
heading_description: "Live swine"
heading_full_text: "Live swine"
animal_family: "Suidae"
scientific_classification: "Sus scrofa"
weight_threshold: 50
weight_unit: "kg"
```

## Table: subheadings_0103
```sql
subheading_code: "0103.10"
subheading_description: "Purebred breeding animals"
classification_criteria: "breeding_status"
certification_required: true
weight_based: false

subheading_code: "0103.91" 
subheading_description: "Weighing less than 50 kg"
classification_criteria: "weight"
weight_threshold_max: 50
weight_unit: "kg"
certification_required: false

subheading_code: "0103.92"
subheading_description: "Weighing 50 kg or more"
classification_criteria: "weight"
weight_threshold_min: 50
weight_unit: "kg"
certification_required: false
```

## Table: statistical_codes_0103
```sql
statistical_code: "0103.10.00.00"
description: "Purebred breeding animals"
parent_subheading: "0103.10.00"
unit_of_quantity: "Number"
second_quantity: null
specific_use: "Breeding"
certification_required: true

statistical_code: "0103.91.00.10"
description: "Weighing less than 7 kg each"
parent_subheading: "0103.91.00"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 0
weight_threshold_max: 7
life_stage: "Piglet"

statistical_code: "0103.91.00.20"
description: "Weighing 7 kg or more but less than 23 kg each"
parent_subheading: "0103.91.00"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 7
weight_threshold_max: 23
life_stage: "Weaner"

statistical_code: "0103.91.00.30"
description: "Weighing 23 kg or more but less than 50 kg each"
parent_subheading: "0103.91.00"
unit_of_quantity: "Number"
second_quantity: "kg" 
weight_threshold_min: 23
weight_threshold_max: 50
life_stage: "Feeder"

statistical_code: "0103.92.00.10"
description: "Imported for immediate slaughter"
parent_subheading: "0103.92.00"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 50
weight_threshold_max: null
specific_use: "Slaughter"
time_restriction: "immediate"

statistical_code: "0103.92.00.20"
description: "Breeding animals other than purebred breeding animals"
parent_subheading: "0103.92.00"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 50
weight_threshold_max: null
specific_use: "Breeding"
certification_required: false

statistical_code: "0103.92.00.91"
description: "Other"
parent_subheading: "0103.92.00"
unit_of_quantity: "Number"
second_quantity: "kg"
weight_threshold_min: 50
weight_threshold_max: null
specific_use: "General"
```

## Table: duty_rates_0103
```sql
statistical_code: "0103.10.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0103.91.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "4.4¢/kg"
special_rate_numeric: 4.40
special_rate_type: "specific"
unit_of_duty: "per_kg"

statistical_code: "0103.92.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "4.4¢/kg"
special_rate_numeric: 4.40
special_rate_type: "specific"
unit_of_duty: "per_kg"
```

---

# HEADING 01.04 - SHEEP AND GOATS

## Table: heading_0104
```sql
heading_code: "0104"
heading_description: "Live sheep and goats" 
heading_full_text: "Live sheep and goats"
animal_family: "Bovidae"
scientific_classification: "Ovis,Capra"
```

## Table: subheadings_0104
```sql
subheading_code: "0104.10"
subheading_description: "Sheep"
classification_criteria: "species"
species: "Ovis aries"
animal_type: "Sheep"

subheading_code: "0104.20"
subheading_description: "Goats"
classification_criteria: "species"
species: "Capra hircus"
animal_type: "Goats"
```

## Table: statistical_codes_0104
```sql
statistical_code: "0104.10.00.00"
description: "Sheep"
parent_subheading: "0104.10.00"
unit_of_quantity: "Number"
second_quantity: "kg"
species: "Ovis aries"
animal_type: "Sheep"

statistical_code: "0104.20.00.00"
description: "Goats"
parent_subheading: "0104.20.00"
unit_of_quantity: "Number"
second_quantity: null
species: "Capra hircus"
animal_type: "Goats"
```

## Table: duty_rates_0104
```sql
statistical_code: "0104.10.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "$3/head"
special_rate_numeric: 3.00
special_rate_type: "specific"
unit_of_duty: "per_head"

statistical_code: "0104.20.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "$3/head"
special_rate_numeric: 3.00
special_rate_type: "specific"
footnote: "68¢/head"
unit_of_duty: "per_head"
```

---

# HEADING 01.05 - POULTRY

## Table: heading_0105
```sql
heading_code: "0105"
heading_description: "Live poultry of the following kinds: Chickens, ducks, geese, turkeys and guinea fowls"
heading_full_text: "Live poultry, that is to say, fowls of the species Gallus domesticus, ducks, geese, turkeys and guinea fowls"
animal_family: "Multiple poultry families"
weight_threshold: 185
weight_unit: "g"
scientific_classification: "Gallus domesticus,Anatidae,Meleagrididae,Numididae"
```

## Table: subheadings_0105
```sql
subheading_code: "0105.11"
subheading_description: "Fowls of the species Gallus domesticus"
classification_criteria: "weight_and_species"
weight_threshold_max: 185
weight_unit: "g"
species: "Gallus domesticus"
animal_type: "Chickens"

subheading_code: "0105.12"
subheading_description: "Turkeys"
classification_criteria: "weight_and_species"
weight_threshold_max: 185
weight_unit: "g"
species: "Meleagris gallopavo"
animal_type: "Turkeys"

subheading_code: "0105.13"
subheading_description: "Ducks"
classification_criteria: "weight_and_species"
weight_threshold_max: 185
weight_unit: "g"
animal_type: "Ducks"

subheading_code: "0105.14"
subheading_description: "Geese"
classification_criteria: "weight_and_species"
weight_threshold_max: 185
weight_unit: "g"
animal_type: "Geese"

subheading_code: "0105.15"
subheading_description: "Guinea fowls"
classification_criteria: "weight_and_species"
weight_threshold_max: 185
weight_unit: "g"
species: "Numida meleagris"
animal_type: "Guinea fowls"

subheading_code: "0105.94"
subheading_description: "Fowls of the species Gallus domesticus"
classification_criteria: "weight_and_species"
weight_threshold_min: 185
weight_unit: "g"
species: "Gallus domesticus"
animal_type: "Chickens"

subheading_code: "0105.99"
subheading_description: "Other"
classification_criteria: "weight_and_species"
weight_threshold_min: 185
weight_unit: "g"
animal_type: "Other poultry"
```

## Table: statistical_codes_0105
```sql
statistical_code: "0105.11.00.10"
description: "Layer-type (egg-type)"
parent_subheading: "0105.11.00"
unit_of_quantity: "Number"
second_quantity: null
breeding_purpose: "Layer"
specific_use: "Breeding"
life_stage: "Day-old"

statistical_code: "0105.11.00.20"
description: "Broiler-type (meat-type)"
parent_subheading: "0105.11.00"
unit_of_quantity: "Number"
second_quantity: null
breeding_purpose: "Broiler"
specific_use: "Breeding"
life_stage: "Day-old"

statistical_code: "0105.11.00.40"
description: "Other"
parent_subheading: "0105.11.00"
unit_of_quantity: "Number"
second_quantity: null
specific_use: "General"
life_stage: "Day-old"

statistical_code: "0105.12.00.00"
description: "Turkeys"
parent_subheading: "0105.12.00"
unit_of_quantity: "Number"
second_quantity: null
animal_type: "Turkeys"
life_stage: "Poult"

statistical_code: "0105.13.00.00"
description: "Ducks"
parent_subheading: "0105.13.00"
unit_of_quantity: "Number"
second_quantity: null
animal_type: "Ducks"
life_stage: "Duckling"

statistical_code: "0105.14.00.00"
description: "Geese"
parent_subheading: "0105.14.00"
unit_of_quantity: "Number"
second_quantity: null
animal_type: "Geese"
life_stage: "Gosling"

statistical_code: "0105.15.00.00"
description: "Guinea fowls"
parent_subheading: "0105.15.00"
unit_of_quantity: "Number"
second_quantity: null
animal_type: "Guinea fowls"
life_stage: "Keet"

statistical_code: "0105.94.00.00"
description: "Chickens"
parent_subheading: "0105.94.00"
unit_of_quantity: "Number"
second_quantity: "kg"
animal_type: "Chickens"
life_stage: "Mature"

statistical_code: "0105.99.00.00"
description: "Other"
parent_subheading: "0105.99.00"
unit_of_quantity: "Number"
second_quantity: "kg"
animal_type: "Other poultry"
life_stage: "Mature"
```

## Table: duty_rates_0105
```sql
statistical_code: "0105.11.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "4¢ each"
special_rate_numeric: 4.00
special_rate_type: "specific"
footnote: "0.9¢ each"
unit_of_duty: "per_each"

statistical_code: "0105.12.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "4¢ each"
special_rate_numeric: 4.00
special_rate_type: "specific"
footnote: "0.9¢ each"
unit_of_duty: "per_each"

statistical_code: "0105.13.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "4¢ each"
special_rate_numeric: 4.00
special_rate_type: "specific"
footnote: "0.9¢ each"
unit_of_duty: "per_each"

statistical_code: "0105.14.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "4¢ each"
special_rate_numeric: 4.00
special_rate_type: "specific"
footnote: "0.9¢ each"
unit_of_duty: "per_each"

statistical_code: "0105.15.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "4¢ each"
special_rate_numeric: 4.00
special_rate_type: "specific"
footnote: "0.9¢ each"
unit_of_duty: "per_each"

statistical_code: "0105.94.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "17.6¢/kg"
special_rate_numeric: 17.60
special_rate_type: "specific"
footnote: "2¢/kg"
unit_of_duty: "per_kg"

statistical_code: "0105.99.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "17.6¢/kg"
special_rate_numeric: 17.60
special_rate_type: "specific"
footnote: "2¢/kg"
unit_of_duty: "per_kg"
```

---

# HEADING 01.06 - OTHER LIVE ANIMALS

## Table: heading_0106
```sql
heading_code: "0106"
heading_description: "Other live animals"
heading_full_text: "Other live animals"
classification_criteria: "taxonomic_groups"
coverage: "All live animals not elsewhere specified"
```

## Table: subheadings_0106
```sql
subheading_code: "0106.11"
subheading_description: "Primates"
classification_criteria: "taxonomic_order"
taxonomic_order: "Primates"
animal_group: "Mammals"

subheading_code: "0106.12"
subheading_description: "Whales, dolphins and porpoises (mammals of the order Cetacea); manatees and dugongs (mammals of the order Sirenia); seals, sea lions and walruses (mammals of the suborder Pinnipedia)"
classification_criteria: "taxonomic_order"
taxonomic_orders: "Cetacea,Sirenia,Pinnipedia"
animal_group: "Marine mammals"

subheading_code: "0106.13"
subheading_description: "Camels and other camelids (Camelidae)"
classification_criteria: "taxonomic_family"
taxonomic_family: "Camelidae"
animal_group: "Mammals"

subheading_code: "0106.14"
subheading_description: "Rabbits and hares"
classification_criteria: "taxonomic_family"
taxonomic_family: "Leporidae"
animal_group: "Mammals"

subheading_code: "0106.19"
subheading_description: "Other"
classification_criteria: "taxonomic_exclusion"
animal_group: "Other mammals"

subheading_code: "0106.20"
subheading_description: "Reptiles (including snakes and turtles)"
classification_criteria: "taxonomic_class"
taxonomic_class: "Reptilia"
animal_group: "Reptiles"

subheading_code: "0106.31"
subheading_description: "Birds of prey"
classification_criteria: "behavioral_ecological"
taxonomic_orders: "Falconiformes,Strigiformes"
animal_group: "Birds"

subheading_code: "0106.32"
subheading_description: "Psittaciformes (including parrots, parakeets, macaws and cockatoos)"
classification_criteria: "taxonomic_order"
taxonomic_order: "Psittaciformes"
animal_group: "Birds"

subheading_code: "0106.33"
subheading_description: "Ostriches; emus (Dromaius novaehollandiae)"
classification_criteria: "taxonomic_order"
taxonomic_order: "Struthioniformes"
animal_group: "Ratite birds"

subheading_code: "0106.39"
subheading_description: "Other"
classification_criteria: "taxonomic_exclusion"
animal_group: "Other birds"

subheading_code: "0106.41"
subheading_description: "Bees"
classification_criteria: "taxonomic_family"
taxonomic_family: "Apidae"
animal_group: "Insects"

subheading_code: "0106.49"
subheading_description: "Other"
classification_criteria: "taxonomic_exclusion"
animal_group: "Other insects"

subheading_code: "0106.90"
subheading_description: "Other"
classification_criteria: "taxonomic_exclusion"
animal_group: "Other animals"
```

## Table: statistical_codes_0106
```sql
statistical_code: "0106.11.00.00"
description: "Primates"
parent_subheading: "0106.11.00"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_order: "Primates"
animal_group: "Mammals"

statistical_code: "0106.12.01.00"
description: "Whales, dolphins and porpoises; manatees and dugongs; seals, sea lions and walruses"
parent_subheading: "0106.12.01"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_orders: "Cetacea,Sirenia,Pinnipedia"
animal_group: "Marine mammals"

statistical_code: "0106.13.00.00"
description: "Camels and other camelids (Camelidae)"
parent_subheading: "0106.13.00"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_family: "Camelidae"
animal_group: "Mammals"

statistical_code: "0106.14.00.00"
description: "Rabbits and hares"
parent_subheading: "0106.14.00"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_family: "Leporidae"
animal_group: "Mammals"

statistical_code: "0106.19.30.00"
description: "Foxes"
parent_subheading: "0106.19.30"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_family: "Canidae"
animal_group: "Mammals"

statistical_code: "0106.19.91.20"
description: "Dogs"
parent_subheading: "0106.19.91"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_family: "Canidae"
animal_group: "Mammals"

statistical_code: "0106.19.91.95"
description: "Other"
parent_subheading: "0106.19.91"
unit_of_quantity: "Number"
second_quantity: null
animal_group: "Other mammals"

statistical_code: "0106.20.00.00"
description: "Reptiles (including snakes and turtles)"
parent_subheading: "0106.20.00"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_class: "Reptilia"
animal_group: "Reptiles"

statistical_code: "0106.31.00.00"
description: "Birds of prey"
parent_subheading: "0106.31.00"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_orders: "Falconiformes,Strigiformes"
animal_group: "Birds"

statistical_code: "0106.32.00.00"
description: "Psittaciformes (including parrots, parakeets, macaws and cockatoos)"
parent_subheading: "0106.32.00"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_order: "Psittaciformes"
animal_group: "Birds"

statistical_code: "0106.33.00.00"
description: "Ostriches; emus (Dromaius novaehollandiae)"
parent_subheading: "0106.33.00"
unit_of_quantity: "Number"
second_quantity: null
taxonomic_order: "Struthioniformes"
animal_group: "Ratite birds"

statistical_code: "0106.39.01.00"
description: "Other"
parent_subheading: "0106.39.01"
unit_of_quantity: "Number"
second_quantity: null
animal_group: "Other birds"

statistical_code: "0106.41.00.00"
description: "Bees"
parent_subheading: "0106.41.00"
unit_of_quantity: "kg"
second_quantity: null
taxonomic_family: "Apidae"
animal_group: "Insects"

statistical_code: "0106.49.00.10"
description: "Leaf cutter bee larvae"
parent_subheading: "0106.49.00"
unit_of_quantity: "kg"
second_quantity: null
taxonomic_family: "Megachilidae"
animal_group: "Insects"

statistical_code: "0106.49.00.90"
description: "Other"
parent_subheading: "0106.49.00"
unit_of_quantity: "kg"
second_quantity: null
animal_group: "Other insects"

statistical_code: "0106.90.01.10"
description: "Worms"
parent_subheading: "0106.90.01"
unit_of_quantity: "kg"
second_quantity: null
taxonomic_phylum: "Annelida"
animal_group: "Invertebrates"

statistical_code: "0106.90.01.20"
description: "Bait (other than worms)"
parent_subheading: "0106.90.01"
unit_of_quantity: "kg"
second_quantity: null
animal_group: "Invertebrates"

statistical_code: "0106.90.01.80"
description: "Other"
parent_subheading: "0106.90.01"
unit_of_quantity: "kg"
second_quantity: null
animal_group: "Other animals"
```

## Table: duty_rates_0106
```sql
statistical_code: "0106.11.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0106.12.01"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0106.13.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0106.14.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0106.19.30"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
footnote: "4.8%"
unit_of_duty: "per_unit"

statistical_code: "0106.19.91"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0106.20.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_unit"

statistical_code: "0106.31.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "1.8%"
unit_of_duty: "per_unit"

statistical_code: "0106.32.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "1.8%"
unit_of_duty: "per_unit"

statistical_code: "0106.33.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "1.8%"
unit_of_duty: "per_unit"

statistical_code: "0106.39.01"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "20%"
special_rate_numeric: 20.00
special_rate_type: "ad_valorem"
footnote: "1.8%"
unit_of_duty: "per_unit"

statistical_code: "0106.41.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0106.49.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"

statistical_code: "0106.90.01"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "ad_valorem"
special_rate: "15%"
special_rate_numeric: 15.00
special_rate_type: "ad_valorem"
unit_of_duty: "per_kg"
```

---

# NORMALIZED REFERENCE TABLES

## Table: trade_programs
```sql
program_code: "A+"
program_name: "USMCA (North American Free Trade Agreement successor)"
participating_countries: "Canada,Mexico"
status: "active"

program_code: "AU"
program_name: "Australia Free Trade Agreement"
participating_countries: "Australia"
status: "active"

program_code: "BH"
program_name: "Bahrain Free Trade Agreement"
participating_countries: "Bahrain"
status: "active"

program_code: "CL"
program_name: "Chile Free Trade Agreement"
participating_countries: "Chile"
status: "active"

program_code: "CO"
program_name: "Colombia Trade Promotion Agreement"
participating_countries: "Colombia"
status: "active"
```

## Table: units_of_measure
```sql
unit_code: "Number"
unit_description: "Number of units/heads/individual animals"
unit_type: "count"
base_unit: "each"

unit_code: "kg"
unit_description: "Kilograms"
unit_type: "weight"
base_unit: "kilogram"

unit_code: "g"
unit_description: "Grams"
unit_type: "weight"
base_unit: "gram"
conversion_to_kg: 0.001
```

## Table: duty_rate_types
```sql
rate_type: "ad_valorem"
description: "Percentage of value"
calculation_method: "percentage"

rate_type: "specific"
description: "Fixed amount per unit"
calculation_method: "per_unit_amount"

rate_type: "compound"
description: "Combination of ad valorem and specific"
calculation_method: "combined"
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
-- Weight thresholds must be logical
weight_threshold_min < weight_threshold_max

-- Breeding animals must be certified if purebred
IF specific_use = "Breeding" AND "purebred" IN description 
THEN certification_required = true

-- Statistical codes must match parent subheading pattern
statistical_code LIKE parent_subheading + "%"
```

## Data Type Constraints
```sql
-- Numeric fields
general_rate_numeric: DECIMAL(10,2)
special_rate_numeric: DECIMAL(10,2)
weight_threshold_min: INTEGER
weight_threshold_max: INTEGER

-- Text fields
description: VARCHAR(500)
classification_criteria: VARCHAR(100)
animal_type: VARCHAR(50)
```

---

**Database Schema Version**: 1.0  
**SQLite Compatible**: Yes  
**Python Scraping Ready**: Yes  
**Total Data Points**: 500+  
**Normalization Level**: 3NF  
**Last Updated**: August 25, 2025