---
# HTS Chapter 03 Database Schema - Fish and Aquatic Invertebrates
database_schema_version: "1.0"
chapter_code: "03"
chapter_name: "Fish and Aquatic Invertebrates"
section_code: "I"
section_name: "Live Animals; Animal Products"
hts_revision: "19"
effective_year: "2025"
last_updated: "2025-08-26"
document_type: "database_ready"
classification_authority: "USITC"
data_structure: "normalized"
scraping_ready: true
python_compatible: true
sqlite_ready: true
total_records: 350
schema_validation: "strict"
---

# Database Structure Overview

## Table: chapter_metadata
```sql
chapter_code: "03"
chapter_name: "Fish and Aquatic Invertebrates"
section_code: "I" 
section_name: "Live Animals; Animal Products"
revision: "19"
effective_year: "2025"
total_headings: 9
total_subheadings: 180
exclusions_count: 6
environmental_requirements: true
turtle_safe_required: true
```

## Table: chapter_notes
```sql
note_id: 1
note_type: "exclusion"
note_text: "This Chapter does not cover: (a) Mammals of heading 01.06; (b) Meat of mammals of heading 01.06 (heading 02.08 or 02.10)"
reference_headings: "01.06, 02.08, 02.10"

note_id: 2
note_type: "exclusion" 
note_text: "Dead fish (including livers, roes and milt), crustaceans, molluscs and other aquatic invertebrates, unfit for human consumption by reason of either their species or their condition (Chapter 5)"
reference_headings: "Chapter 5"

note_id: 3
note_type: "exclusion"
note_text: "Flours, meals and pellets of fish, crustaceans, molluscs or other aquatic invertebrates, unfit for human consumption (heading 23.01)"
reference_headings: "23.01"

note_id: 4
note_type: "exclusion"
note_text: "Caviar and caviar substitutes prepared from fish eggs (heading 16.04)"
reference_headings: "16.04"

note_id: 5
note_type: "definition"
note_text: "For purposes of this Chapter 'pellets' means products agglomerated either by compression or by the addition of small quantities of binder"
reference_headings: "all"

note_id: 6
note_type: "exclusion"
note_text: "Headings 03.05, 03.06, 03.07 and 03.08 do not apply to flours, meals and pellets, fit for human consumption (heading 03.09)"
reference_headings: "03.05-03.09"
```

## Table: us_additional_notes
```sql
us_note_id: 1
note_type: "reference"
note_title: "Chapter 98 Products"
note_text: "Certain products of this Chapter are provided for in Chapter 98"
status: "active"
special_note: "Product-specific Chapter 98 references apply"

us_note_id: 2
note_type: "environmental"
note_title: "Turtle-Safe Shrimp Requirements"
note_text: "Shrimp imports from certain countries subject to section 609 of Public Law 101-162 regarding turtle-safe harvesting methods"
reference_chapter: "Environmental Protection"
status: "active"
environmental_compliance: true
```

---

# HEADING 03.01 - Live Fish

## Table: heading_0301
```sql
heading_code: "0301"
heading_description: "Live fish"
heading_full_text: "Live fish"
product_category: "live_aquatic"
ornamental_included: true
commercial_included: true
aquaculture_status: "all_types"
```

## Table: subheadings_0301
```sql
subheading_code: "0301.11"
subheading_description: "Ornamental fish: Freshwater"
parent_category: "ornamental"
classification_criteria: "freshwater_species"
aquarium_trade: true

subheading_code: "0301.19"
subheading_description: "Ornamental fish: Other"
parent_category: "ornamental"
classification_criteria: "marine_species"
aquarium_trade: true

subheading_code: "0301.91"
subheading_description: "Trout (Salmo trutta, Oncorhynchus spp., Salvelinus spp.)"
parent_category: "salmonidae"
classification_criteria: "genus_species"
scientific_classification: "Salmonidae"

subheading_code: "0301.92"
subheading_description: "Eels (Anguilla spp.)"
parent_category: "anguillidae"
classification_criteria: "genus_species" 
scientific_classification: "Anguillidae"

subheading_code: "0301.93"
subheading_description: "Carp (Cyprinus spp., Carassius spp., Ctenopharyngodon idellus, Hypophthalmichthys spp.)"
parent_category: "cyprinidae"
classification_criteria: "genus_species"
scientific_classification: "Cyprinidae"

subheading_code: "0301.94"
subheading_description: "Atlantic and Pacific bluefin tunas (Thunnus thynnus, Thunnus orientalis)"
parent_category: "scombridae"
classification_criteria: "specific_species"
scientific_classification: "Thunnus"

subheading_code: "0301.95"
subheading_description: "Southern bluefin tunas (Thunnus maccoyii)"
parent_category: "scombridae" 
classification_criteria: "specific_species"
scientific_classification: "Thunnus"

subheading_code: "0301.99"
subheading_description: "Other"
parent_category: "miscellaneous"
classification_criteria: "not_elsewhere_specified"
scientific_classification: "various"
```

## Table: statistical_codes_0301
```sql
statistical_code: "0301.11.00.10"
description: "Goldfish (Carassius auratus)"
parent_subheading: "0301.11.00"
unit_of_quantity: "No."
second_quantity: null
species: "Carassius auratus"
ornamental_type: "freshwater"

statistical_code: "0301.11.00.90"
description: "Other freshwater ornamental fish"
parent_subheading: "0301.11.00"
unit_of_quantity: "No."
second_quantity: null
species: "various"
ornamental_type: "freshwater"

statistical_code: "0301.19.00.10"
description: "Tropical marine fish"
parent_subheading: "0301.19.00"
unit_of_quantity: "No."
second_quantity: null
species: "various"
ornamental_type: "marine"

statistical_code: "0301.19.00.90"
description: "Other ornamental fish"
parent_subheading: "0301.19.00"
unit_of_quantity: "No."
second_quantity: null
species: "various"
ornamental_type: "other"

statistical_code: "0301.91.00.10"
description: "Rainbow trout (Oncorhynchus mykiss)"
parent_subheading: "0301.91.00"
unit_of_quantity: "No."
second_quantity: null
species: "Oncorhynchus mykiss"
commercial_use: "aquaculture"

statistical_code: "0301.91.00.90"
description: "Other trout"
parent_subheading: "0301.91.00"
unit_of_quantity: "No."
second_quantity: null
species: "Salmo/Oncorhynchus spp."
commercial_use: "aquaculture"

statistical_code: "0301.92.00.00"
description: "Eels (Anguilla spp.)"
parent_subheading: "0301.92.00"
unit_of_quantity: "No."
second_quantity: null
species: "Anguilla spp."
commercial_use: "aquaculture"

statistical_code: "0301.93.00.10"
description: "Grass carp (Ctenopharyngodon idellus)"
parent_subheading: "0301.93.00"
unit_of_quantity: "No."
second_quantity: null
species: "Ctenopharyngodon idellus"
commercial_use: "aquaculture"

statistical_code: "0301.93.00.90"
description: "Other carp"
parent_subheading: "0301.93.00"
unit_of_quantity: "No."
second_quantity: null
species: "Cyprinus/Carassius spp."
commercial_use: "aquaculture"

statistical_code: "0301.94.00.00"
description: "Atlantic and Pacific bluefin tunas"
parent_subheading: "0301.94.00"
unit_of_quantity: "No."
second_quantity: null
species: "Thunnus thynnus/orientalis"
commercial_use: "ranching"

statistical_code: "0301.95.00.00"
description: "Southern bluefin tunas"
parent_subheading: "0301.95.00"
unit_of_quantity: "No."
second_quantity: null
species: "Thunnus maccoyii"
commercial_use: "ranching"

statistical_code: "0301.99.00.10"
description: "Bass"
parent_subheading: "0301.99.00"
unit_of_quantity: "No."
second_quantity: null
species: "various"
commercial_use: "general"

statistical_code: "0301.99.00.90"
description: "Other live fish"
parent_subheading: "0301.99.00"
unit_of_quantity: "No."
second_quantity: null
species: "various"
commercial_use: "general"
```

## Table: duty_rates_0301
```sql
statistical_code: "0301.11.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "No."

statistical_code: "0301.19.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "No."

statistical_code: "0301.91.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "No."

statistical_code: "0301.92.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "No."

statistical_code: "0301.93.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "No."

statistical_code: "0301.94.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "No."

statistical_code: "0301.95.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "No."

statistical_code: "0301.99.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "No."
```

---

# HEADING 03.02 - Fish, Fresh or Chilled (excluding fillets and other fish meat)

## Table: heading_0302
```sql
heading_code: "0302"
heading_description: "Fish, fresh or chilled, excluding fish fillets and other fish meat of heading 03.04"
heading_full_text: "Fish, fresh or chilled, excluding fish fillets and other fish meat of heading 03.04"
temperature_state: "fresh_chilled"
processing_level: "whole_fish"
excludes_fillets: true
commercial_category: "primary"
```

## Table: subheadings_0302
```sql
subheading_code: "0302.11"
subheading_description: "Trout (Salmo trutta, Oncorhynchus spp., Salvelinus spp.)"
parent_category: "salmonidae"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.13"
subheading_description: "Pacific salmon (Oncorhynchus nerka, O. gorbuscha, O. keta, O. tschawytscha, O. kisutch, O. masou, O. rhodurus)"
parent_category: "salmonidae"
classification_criteria: "specific_pacific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.14"
subheading_description: "Atlantic salmon (Salmo salar) and Danube salmon (Hucho hucho)"
parent_category: "salmonidae"
classification_criteria: "specific_atlantic_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.19"
subheading_description: "Other"
parent_category: "salmonidae"
classification_criteria: "other_salmonidae"
temperature_state: "fresh_chilled"

subheading_code: "0302.21"
subheading_description: "Halibut (Reinhardtius hippoglossoides, Hippoglossus spp.) and Greenland turbot (Reinhardtius hippoglossoides)"
parent_category: "flat_fish"
classification_criteria: "halibut_turbot"
temperature_state: "fresh_chilled"

subheading_code: "0302.22"
subheading_description: "Plaice (Pleuronectes platessa)"
parent_category: "flat_fish"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.23"
subheading_description: "Sole (Solea spp.)"
parent_category: "flat_fish"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.24"
subheading_description: "Turbots (Psetta maxima)"
parent_category: "flat_fish"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.29"
subheading_description: "Other"
parent_category: "flat_fish"
classification_criteria: "other_flat_fish"
temperature_state: "fresh_chilled"

subheading_code: "0302.31"
subheading_description: "Albacore or longfinned tunas (Thunnus alalunga)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.32"
subheading_description: "Yellowfin tunas (Thunnus albacares)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.33"
subheading_description: "Skipjack or stripe-bellied bonito"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.34"
subheading_description: "Bigeye tunas (Thunnus obesus)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.35"
subheading_description: "Atlantic and Pacific bluefin tunas (Thunnus thynnus, Thunnus orientalis)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.36"
subheading_description: "Southern bluefin tunas (Thunnus maccoyii)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.39"
subheading_description: "Other"
parent_category: "tunas"
classification_criteria: "other_tunas"
temperature_state: "fresh_chilled"

subheading_code: "0302.41"
subheading_description: "Herrings (Clupea harengus, Clupea pallasii), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.42"
subheading_description: "Anchovies (Engraulis spp.), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.43"
subheading_description: "Sardines, sardinella, brisling or sprats, excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "small_pelagic"
temperature_state: "fresh_chilled"

subheading_code: "0302.44"
subheading_description: "Mackerel (Scomber spp.), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.45"
subheading_description: "Jack and horse mackerel (Trachurus spp.), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.46"
subheading_description: "Cobia (Rachycentron canadum), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.47"
subheading_description: "Swordfish (Xiphias gladius), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.49"
subheading_description: "Other, excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "other_pelagic"
temperature_state: "fresh_chilled"

subheading_code: "0302.51"
subheading_description: "Cod (Gadus morhua, Gadus ogac, Gadus macrocephalus), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.52"
subheading_description: "Haddock (Melanogrammus aeglefinus), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.53"
subheading_description: "Coalfish (Pollachius virens), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.54"
subheading_description: "Hake (Merluccius spp., Urophycis spp.), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.55"
subheading_description: "Alaska pollock (Theragra chalcogramma), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.56"
subheading_description: "Blue whitings (Micromesistius poutassou, Micromesistius australis), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.59"
subheading_description: "Other, excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "other_cod_family"
temperature_state: "fresh_chilled"

subheading_code: "0302.71"
subheading_description: "Tilapias (Oreochromis spp.), excluding livers, roes and milt"
parent_category: "freshwater_aquaculture"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.72"
subheading_description: "Catfish (Pangasius spp., Silurus spp., Clarias spp., Ictalurus spp.), excluding livers, roes and milt"
parent_category: "freshwater_aquaculture"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.73"
subheading_description: "Carp (Cyprinus spp., Carassius spp., Ctenopharyngodon idellus, Hypophthalmichthys spp.), excluding livers, roes and milt"
parent_category: "freshwater_aquaculture"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.74"
subheading_description: "Eels (Anguilla spp.), excluding livers, roes and milt"
parent_category: "freshwater_aquaculture"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.79"
subheading_description: "Other, excluding livers, roes and milt"
parent_category: "freshwater_aquaculture"
classification_criteria: "other_freshwater"
temperature_state: "fresh_chilled"

subheading_code: "0302.81"
subheading_description: "Sharks, excluding livers, roes and milt"
parent_category: "cartilaginous"
classification_criteria: "shark_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.82"
subheading_description: "Rays and skates (Rajidae), excluding livers, roes and milt"
parent_category: "cartilaginous"
classification_criteria: "ray_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.83"
subheading_description: "Toothfish (Dissostichus spp.), excluding livers, roes and milt"
parent_category: "deep_water"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.84"
subheading_description: "Seabass (Dicentrarchus spp.), excluding livers, roes and milt"
parent_category: "marine_finfish"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.85"
subheading_description: "Seabream (Sparidae), excluding livers, roes and milt"
parent_category: "marine_finfish"
classification_criteria: "family_species"
temperature_state: "fresh_chilled"

subheading_code: "0302.89"
subheading_description: "Other fish, excluding livers, roes and milt"
parent_category: "other_fish"
classification_criteria: "not_elsewhere_specified"
temperature_state: "fresh_chilled"

subheading_code: "0302.91"
subheading_description: "Livers, roes and milt"
parent_category: "fish_offal"
classification_criteria: "edible_offal"
temperature_state: "fresh_chilled"

subheading_code: "0302.92"
subheading_description: "Shark fins"
parent_category: "fish_offal"
classification_criteria: "specific_parts"
temperature_state: "fresh_chilled"

subheading_code: "0302.99"
subheading_description: "Other edible fish offal"
parent_category: "fish_offal"
classification_criteria: "other_edible_parts"
temperature_state: "fresh_chilled"
```

## Table: statistical_codes_0302
```sql
statistical_code: "0302.11.00.10"
description: "Trout, farmed"
parent_subheading: "0302.11.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Salmo/Oncorhynchus spp."
production_method: "aquaculture"
temperature_state: "fresh_chilled"

statistical_code: "0302.11.00.90"
description: "Trout, other"
parent_subheading: "0302.11.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Salmo/Oncorhynchus spp."
production_method: "wild_caught"
temperature_state: "fresh_chilled"

statistical_code: "0302.13.00.01"
description: "Chinook (King) salmon"
parent_subheading: "0302.13.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus tshawytscha"
production_method: "all"
temperature_state: "fresh_chilled"

statistical_code: "0302.13.00.02"
description: "Sockeye salmon"
parent_subheading: "0302.13.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus nerka"
production_method: "all"
temperature_state: "fresh_chilled"

statistical_code: "0302.13.00.03"
description: "Coho salmon"
parent_subheading: "0302.13.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus kisutch"
production_method: "all"
temperature_state: "fresh_chilled"

statistical_code: "0302.13.00.04"
description: "Pink salmon"
parent_subheading: "0302.13.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus gorbuscha"
production_method: "all"
temperature_state: "fresh_chilled"

statistical_code: "0302.13.00.05"
description: "Chum salmon"
parent_subheading: "0302.13.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus keta"
production_method: "all"
temperature_state: "fresh_chilled"

statistical_code: "0302.13.00.06"
description: "Atlantic salmon (farm-raised in the Pacific Ocean)"
parent_subheading: "0302.13.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Salmo salar"
production_method: "aquaculture"
temperature_state: "fresh_chilled"

statistical_code: "0302.14.00.10"
description: "Atlantic salmon"
parent_subheading: "0302.14.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Salmo salar"
production_method: "all"
temperature_state: "fresh_chilled"

statistical_code: "0302.14.00.90"
description: "Danube salmon"
parent_subheading: "0302.14.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Hucho hucho"
production_method: "all"
temperature_state: "fresh_chilled"

statistical_code: "0302.21.00.00"
description: "Halibut and Greenland turbot"
parent_subheading: "0302.21.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Reinhardtius/Hippoglossus spp."
production_method: "wild_caught"
temperature_state: "fresh_chilled"

statistical_code: "0302.31.00.00"
description: "Albacore tunas"
parent_subheading: "0302.31.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Thunnus alalunga"
production_method: "wild_caught"
temperature_state: "fresh_chilled"

statistical_code: "0302.41.00.10"
description: "Herrings, not in bulk or in immediate packagings weighing 6.8 kg or more each"
parent_subheading: "0302.41.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Clupea spp."
packaging_type: "retail"
temperature_state: "fresh_chilled"

statistical_code: "0302.41.00.20"
description: "Herrings, in bulk or in immediate packagings weighing 6.8 kg or more each"
parent_subheading: "0302.41.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Clupea spp."
packaging_type: "bulk"
temperature_state: "fresh_chilled"

statistical_code: "0302.51.00.10"
description: "Cod, not in bulk or in immediate packagings weighing 6.8 kg or more each"
parent_subheading: "0302.51.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Gadus spp."
packaging_type: "retail"
temperature_state: "fresh_chilled"

statistical_code: "0302.51.00.20"
description: "Cod, in bulk or in immediate packagings weighing 6.8 kg or more each"
parent_subheading: "0302.51.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Gadus spp."
packaging_type: "bulk"
temperature_state: "fresh_chilled"

statistical_code: "0302.91.00.10"
description: "Sturgeon roe"
parent_subheading: "0302.91.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Acipenser spp."
product_type: "caviar_precursor"
temperature_state: "fresh_chilled"

statistical_code: "0302.91.00.20"
description: "Other fish roe"
parent_subheading: "0302.91.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
product_type: "roe"
temperature_state: "fresh_chilled"

statistical_code: "0302.91.00.30"
description: "Fish livers"
parent_subheading: "0302.91.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
product_type: "liver"
temperature_state: "fresh_chilled"

statistical_code: "0302.91.00.40"
description: "Fish milt"
parent_subheading: "0302.91.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
product_type: "milt"
temperature_state: "fresh_chilled"
```

## Table: duty_rates_0302
```sql
statistical_code: "0302.11.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0302.13.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0302.14.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0302.21.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0302.31.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0302.41.00"
general_rate: "4.4¢/kg (retail) 25% (bulk)"
general_rate_numeric: 4.40
general_rate_type: "specific_or_ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
packaging_differential: true

statistical_code: "0302.51.00"
general_rate: "2.2¢/kg (retail) 25% (bulk)"
general_rate_numeric: 2.20
general_rate_type: "specific_or_ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
packaging_differential: true

statistical_code: "0302.91.00"
general_rate: "15% (sturgeon) 2.2¢/kg (other)"
general_rate_numeric: 15.00
general_rate_type: "ad_valorem_or_specific"
special_rate: "Free-7.5%"
special_rate_numeric: 7.50
special_rate_type: "preferential_rate"
unit_of_duty: "kg"
product_differential: true
```

---

# HEADING 03.03 - Fish, Frozen (excluding fillets and other fish meat)

## Table: heading_0303
```sql
heading_code: "0303"
heading_description: "Fish, frozen, excluding fish fillets and other fish meat of heading 03.04"
heading_full_text: "Fish, frozen, excluding fish fillets and other fish meat of heading 03.04"
temperature_state: "frozen"
processing_level: "whole_fish"
excludes_fillets: true
commercial_category: "primary"
```

## Table: subheadings_0303
```sql
subheading_code: "0303.11"
subheading_description: "Sockeye salmon (red salmon) (Oncorhynchus nerka)"
parent_category: "salmonidae"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.12"
subheading_description: "Other Pacific salmon"
parent_category: "salmonidae"
classification_criteria: "other_pacific_species"
temperature_state: "frozen"

subheading_code: "0303.13"
subheading_description: "Atlantic salmon (Salmo salar) and Danube salmon (Hucho hucho)"
parent_category: "salmonidae"
classification_criteria: "specific_atlantic_species"
temperature_state: "frozen"

subheading_code: "0303.14"
subheading_description: "Trout (Salmo trutta, Oncorhynchus spp., Salvelinus spp.)"
parent_category: "salmonidae"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.19"
subheading_description: "Other"
parent_category: "salmonidae"
classification_criteria: "other_salmonidae"
temperature_state: "frozen"

subheading_code: "0303.23"
subheading_description: "Sole (Solea spp.)"
parent_category: "flat_fish"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.24"
subheading_description: "Turbots (Psetta maxima)"
parent_category: "flat_fish"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.29"
subheading_description: "Other"
parent_category: "flat_fish"
classification_criteria: "other_flat_fish"
temperature_state: "frozen"

subheading_code: "0303.31"
subheading_description: "Albacore or longfinned tunas (Thunnus alalunga)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.32"
subheading_description: "Yellowfin tunas (Thunnus albacares)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.33"
subheading_description: "Skipjack or stripe-bellied bonito"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.34"
subheading_description: "Bigeye tunas (Thunnus obesus)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.35"
subheading_description: "Atlantic and Pacific bluefin tunas (Thunnus thynnus, Thunnus orientalis)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.36"
subheading_description: "Southern bluefin tunas (Thunnus maccoyii)"
parent_category: "tunas"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.39"
subheading_description: "Other"
parent_category: "tunas"
classification_criteria: "other_tunas"
temperature_state: "frozen"

subheading_code: "0303.41"
subheading_description: "Herrings (Clupea harengus, Clupea pallasii), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.42"
subheading_description: "Anchovies (Engraulis spp.), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.43"
subheading_description: "Sardines, sardinella, brisling or sprats, excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "small_pelagic"
temperature_state: "frozen"

subheading_code: "0303.44"
subheading_description: "Mackerel (Scomber spp.), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.45"
subheading_description: "Jack and horse mackerel (Trachurus spp.), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.46"
subheading_description: "Cobia (Rachycentron canadum), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.47"
subheading_description: "Swordfish (Xiphias gladius), excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.49"
subheading_description: "Other, excluding livers, roes and milt"
parent_category: "pelagic"
classification_criteria: "other_pelagic"
temperature_state: "frozen"

subheading_code: "0303.63"
subheading_description: "Cod (Gadus morhua, Gadus ogac, Gadus macrocephalus), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.64"
subheading_description: "Haddock (Melanogrammus aeglefinus), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.65"
subheading_description: "Coalfish (Pollachius virens), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.66"
subheading_description: "Hake (Merluccius spp., Urophycis spp.), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.67"
subheading_description: "Alaska pollock (Theragra chalcogramma), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "specific_species"
temperature_state: "frozen"

subheading_code: "0303.68"
subheading_description: "Blue whitings (Micromesistius poutassou, Micromesistius australis), excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.69"
subheading_description: "Other, excluding livers, roes and milt"
parent_category: "cod_family"
classification_criteria: "other_cod_family"
temperature_state: "frozen"

subheading_code: "0303.81"
subheading_description: "Sharks, excluding livers, roes and milt"
parent_category: "cartilaginous"
classification_criteria: "shark_species"
temperature_state: "frozen"

subheading_code: "0303.82"
subheading_description: "Rays and skates (Rajidae), excluding livers, roes and milt"
parent_category: "cartilaginous"
classification_criteria: "ray_species"
temperature_state: "frozen"

subheading_code: "0303.83"
subheading_description: "Toothfish (Dissostichus spp.), excluding livers, roes and milt"
parent_category: "deep_water"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.84"
subheading_description: "Seabass (Dicentrarchus spp.), excluding livers, roes and milt"
parent_category: "marine_finfish"
classification_criteria: "genus_species"
temperature_state: "frozen"

subheading_code: "0303.89"
subheading_description: "Other fish, excluding livers, roes and milt"
parent_category: "other_fish"
classification_criteria: "not_elsewhere_specified"
temperature_state: "frozen"

subheading_code: "0303.91"
subheading_description: "Livers, roes and milt"
parent_category: "fish_offal"
classification_criteria: "edible_offal"
temperature_state: "frozen"

subheading_code: "0303.92"
subheading_description: "Shark fins"
parent_category: "fish_offal"
classification_criteria: "specific_parts"
temperature_state: "frozen"

subheading_code: "0303.99"
subheading_description: "Other edible fish offal"
parent_category: "fish_offal"
classification_criteria: "other_edible_parts"
temperature_state: "frozen"
```

## Table: statistical_codes_0303
```sql
statistical_code: "0303.11.00.00"
description: "Sockeye salmon (red salmon)"
parent_subheading: "0303.11.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus nerka"
production_method: "wild_caught"
temperature_state: "frozen"

statistical_code: "0303.12.00.10"
description: "Chinook (King) salmon"
parent_subheading: "0303.12.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus tshawytscha"
production_method: "wild_caught"
temperature_state: "frozen"

statistical_code: "0303.12.00.20"
description: "Coho salmon"
parent_subheading: "0303.12.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus kisutch"
production_method: "wild_caught"
temperature_state: "frozen"

statistical_code: "0303.12.00.30"
description: "Pink salmon"
parent_subheading: "0303.12.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus gorbuscha"
production_method: "wild_caught"
temperature_state: "frozen"

statistical_code: "0303.12.00.40"
description: "Chum salmon"
parent_subheading: "0303.12.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus keta"
production_method: "wild_caught"
temperature_state: "frozen"

statistical_code: "0303.13.00.10"
description: "Atlantic salmon"
parent_subheading: "0303.13.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Salmo salar"
production_method: "all"
temperature_state: "frozen"

statistical_code: "0303.63.00.00"
description: "Cod"
parent_subheading: "0303.63.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Gadus spp."
production_method: "wild_caught"
temperature_state: "frozen"

statistical_code: "0303.67.00.00"
description: "Alaska pollock"
parent_subheading: "0303.67.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Theragra chalcogramma"
production_method: "wild_caught"
temperature_state: "frozen"
```

## Table: duty_rates_0303
```sql
statistical_code: "0303.11.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0303.63.00"
general_rate: "2.2¢/kg"
general_rate_numeric: 2.20
general_rate_type: "specific"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0303.67.00"
general_rate: "4.4¢/kg"
general_rate_numeric: 4.40
general_rate_type: "specific"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
```

---

# HEADING 03.04 - Fish Fillets and Other Fish Meat

## Table: heading_0304
```sql
heading_code: "0304"
heading_description: "Fish fillets and other fish meat (whether or not minced), fresh, chilled or frozen"
heading_full_text: "Fish fillets and other fish meat (whether or not minced), fresh, chilled or frozen"
temperature_state: "fresh_chilled_frozen"
processing_level: "filleted"
includes_minced: true
commercial_category: "processed"
```

## Table: subheadings_0304
```sql
subheading_code: "0304.31"
subheading_description: "Fresh or chilled: Tilapias (Oreochromis spp.)"
parent_category: "freshwater_fillets"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.32"
subheading_description: "Fresh or chilled: Catfish (Pangasius spp., Silurus spp., Clarias spp., Ictalurus spp.)"
parent_category: "freshwater_fillets"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.33"
subheading_description: "Fresh or chilled: Nile perch (Lates niloticus)"
parent_category: "freshwater_fillets"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.39"
subheading_description: "Fresh or chilled: Other"
parent_category: "freshwater_fillets"
classification_criteria: "other_freshwater"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.41"
subheading_description: "Fresh or chilled: Pacific salmon, Atlantic salmon and Danube salmon"
parent_category: "marine_fillets"
classification_criteria: "salmon_species"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.42"
subheading_description: "Fresh or chilled: Trout (Salmo trutta, Oncorhynchus spp., Salvelinus spp.)"
parent_category: "marine_fillets"
classification_criteria: "trout_species"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.43"
subheading_description: "Fresh or chilled: Flat fish (Pleuronectidae, Bothidae, Cynoglossidae, Soleidae, Scophthalmidae and Citharidae)"
parent_category: "marine_fillets"
classification_criteria: "flat_fish_families"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.44"
subheading_description: "Fresh or chilled: Fish of the families Bregmacerotidae, Euclichthyidae, Gadidae, Macrouridae, Melanonidae, Merlucciidae, Moridae and Muraenolepididae"
parent_category: "marine_fillets"
classification_criteria: "cod_family_complex"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.45"
subheading_description: "Fresh or chilled: Swordfish (Xiphias gladius)"
parent_category: "marine_fillets"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.46"
subheading_description: "Fresh or chilled: Toothfish (Dissostichus spp.)"
parent_category: "marine_fillets"
classification_criteria: "genus_species"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.47"
subheading_description: "Fresh or chilled: Tunas (of the genus Thunnus), skipjack or stripe-bellied bonito"
parent_category: "marine_fillets"
classification_criteria: "tuna_species"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.49"
subheading_description: "Fresh or chilled: Other"
parent_category: "marine_fillets"
classification_criteria: "other_marine"
temperature_state: "fresh_chilled"
processing_level: "filleted"

subheading_code: "0304.51"
subheading_description: "Fresh or chilled, other fish meat: Tilapias, catfish, carp, eels, Nile perch and snakeheads"
parent_category: "freshwater_meat"
classification_criteria: "specified_species"
temperature_state: "fresh_chilled"
processing_level: "other_meat"

subheading_code: "0304.52"
subheading_description: "Fresh or chilled, other fish meat: Salmonidae"
parent_category: "marine_meat"
classification_criteria: "salmon_family"
temperature_state: "fresh_chilled"
processing_level: "other_meat"

subheading_code: "0304.53"
subheading_description: "Fresh or chilled, other fish meat: Fish of families Bregmacerotidae through Muraenolepididae"
parent_category: "marine_meat"
classification_criteria: "cod_complex"
temperature_state: "fresh_chilled"
processing_level: "other_meat"

subheading_code: "0304.54"
subheading_description: "Fresh or chilled, other fish meat: Swordfish"
parent_category: "marine_meat"
classification_criteria: "specific_species"
temperature_state: "fresh_chilled"
processing_level: "other_meat"

subheading_code: "0304.55"
subheading_description: "Fresh or chilled, other fish meat: Tunas, skipjack and stripe-bellied bonito"
parent_category: "marine_meat"
classification_criteria: "tuna_species"
temperature_state: "fresh_chilled"
processing_level: "other_meat"

subheading_code: "0304.56"
subheading_description: "Fresh or chilled, other fish meat: Sharks"
parent_category: "marine_meat"
classification_criteria: "cartilaginous"
temperature_state: "fresh_chilled"
processing_level: "other_meat"

subheading_code: "0304.57"
subheading_description: "Fresh or chilled, other fish meat: Rays and skates"
parent_category: "marine_meat"
classification_criteria: "cartilaginous"
temperature_state: "fresh_chilled"
processing_level: "other_meat"

subheading_code: "0304.59"
subheading_description: "Fresh or chilled, other fish meat: Other"
parent_category: "marine_meat"
classification_criteria: "other_species"
temperature_state: "fresh_chilled"
processing_level: "other_meat"

subheading_code: "0304.61"
subheading_description: "Frozen: Tilapias, catfish, carp, eels, Nile perch and snakeheads"
parent_category: "freshwater_fillets"
classification_criteria: "specified_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.62"
subheading_description: "Frozen: Salmonidae"
parent_category: "marine_fillets"
classification_criteria: "salmon_family"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.63"
subheading_description: "Frozen: Tunas (genus Thunnus), skipjack or stripe-bellied bonito"
parent_category: "marine_fillets"
classification_criteria: "tuna_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.71"
subheading_description: "Frozen: Cod (Gadus morhua, Gadus ogac, Gadus macrocephalus)"
parent_category: "cod_fillets"
classification_criteria: "cod_genus"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.72"
subheading_description: "Frozen: Haddock (Melanogrammus aeglefinus)"
parent_category: "cod_fillets"
classification_criteria: "specific_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.73"
subheading_description: "Frozen: Coalfish (Pollachius virens)"
parent_category: "cod_fillets"
classification_criteria: "specific_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.74"
subheading_description: "Frozen: Hake (Merluccius spp., Urophycis spp.)"
parent_category: "cod_fillets"
classification_criteria: "hake_genera"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.75"
subheading_description: "Frozen: Alaska pollock (Theragra chalcogramma)"
parent_category: "cod_fillets"
classification_criteria: "specific_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.79"
subheading_description: "Frozen: Other fish of families Bregmacerotidae through Muraenolepididae"
parent_category: "cod_fillets"
classification_criteria: "other_cod_complex"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.81"
subheading_description: "Frozen: Pacific salmon, Atlantic salmon and Danube salmon"
parent_category: "marine_fillets"
classification_criteria: "salmon_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.82"
subheading_description: "Frozen: Trout (Salmo trutta, Oncorhynchus spp., Salvelinus spp.)"
parent_category: "marine_fillets"
classification_criteria: "trout_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.83"
subheading_description: "Frozen: Flat fish"
parent_category: "marine_fillets"
classification_criteria: "flat_fish"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.84"
subheading_description: "Frozen: Swordfish (Xiphias gladius)"
parent_category: "marine_fillets"
classification_criteria: "specific_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.85"
subheading_description: "Frozen: Toothfish (Dissostichus spp.)"
parent_category: "marine_fillets"
classification_criteria: "genus_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.86"
subheading_description: "Frozen: Herrings (Clupea harengus, Clupea pallasii)"
parent_category: "pelagic_fillets"
classification_criteria: "herring_species"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.87"
subheading_description: "Frozen: Tunas (genus Thunnus), skipjack or stripe-bellied bonito (Euthynnus pelamis) and other fish of family Scombridae"
parent_category: "pelagic_fillets"
classification_criteria: "tuna_mackerel"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.89"
subheading_description: "Frozen: Other"
parent_category: "marine_fillets"
classification_criteria: "other_marine"
temperature_state: "frozen"
processing_level: "filleted"

subheading_code: "0304.91"
subheading_description: "Frozen, other fish meat: Swordfish"
parent_category: "marine_meat"
classification_criteria: "specific_species"
temperature_state: "frozen"
processing_level: "other_meat"

subheading_code: "0304.92"
subheading_description: "Frozen, other fish meat: Toothfish"
parent_category: "marine_meat"
classification_criteria: "genus_species"
temperature_state: "frozen"
processing_level: "other_meat"

subheading_code: "0304.93"
subheading_description: "Frozen, other fish meat: Tilapias, catfish, carp, eels, Nile perch and snakeheads"
parent_category: "freshwater_meat"
classification_criteria: "specified_species"
temperature_state: "frozen"
processing_level: "other_meat"

subheading_code: "0304.94"
subheading_description: "Frozen, other fish meat: Alaska pollock"
parent_category: "cod_meat"
classification_criteria: "specific_species"
temperature_state: "frozen"
processing_level: "other_meat"

subheading_code: "0304.95"
subheading_description: "Frozen, other fish meat: Fish of families Bregmacerotidae through Muraenolepididae, other than Alaska pollock"
parent_category: "cod_meat"
classification_criteria: "other_cod_complex"
temperature_state: "frozen"
processing_level: "other_meat"

subheading_code: "0304.99"
subheading_description: "Frozen, other fish meat: Other"
parent_category: "marine_meat"
classification_criteria: "other_species"
temperature_state: "frozen"
processing_level: "other_meat"
```

## Table: statistical_codes_0304
```sql
statistical_code: "0304.32.00.10"
description: "Pangasius fillets, fresh or chilled"
parent_subheading: "0304.32.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Pangasius spp."
temperature_state: "fresh_chilled"
processing_level: "filleted"

statistical_code: "0304.41.00.10"
description: "Pacific salmon fillets, fresh or chilled"
parent_subheading: "0304.41.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Oncorhynchus spp."
temperature_state: "fresh_chilled"
processing_level: "filleted"

statistical_code: "0304.71.00.00"
description: "Cod fillets, frozen"
parent_subheading: "0304.71.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Gadus spp."
temperature_state: "frozen"
processing_level: "filleted"

statistical_code: "0304.75.00.10"
description: "Alaska pollock fillets, frozen, in bulk or in immediate packagings weighing 6.8 kg or more each"
parent_subheading: "0304.75.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Theragra chalcogramma"
temperature_state: "frozen"
processing_level: "filleted"
packaging_type: "bulk"

statistical_code: "0304.75.00.20"
description: "Alaska pollock fillets, frozen, not in bulk or in immediate packagings weighing 6.8 kg or more each"
parent_subheading: "0304.75.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Theragra chalcogramma"
temperature_state: "frozen"
processing_level: "filleted"
packaging_type: "retail"
```

## Table: duty_rates_0304
```sql
statistical_code: "0304.41.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0304.71.00"
general_rate: "5.5¢/kg"
general_rate_numeric: 5.50
general_rate_type: "specific"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0304.75.00"
general_rate: "2.8¢/kg (bulk) 6% (retail)"
general_rate_numeric: 2.80
general_rate_type: "specific_or_ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
packaging_differential: true

statistical_code: "0304.89.00"
general_rate: "5.5¢/kg"
general_rate_numeric: 5.50
general_rate_type: "specific"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
```

---

# HEADING 03.05 - Fish, Dried, Salted or in Brine; Smoked Fish

## Table: heading_0305
```sql
heading_code: "0305"
heading_description: "Fish, dried, salted or in brine; smoked fish, whether or not cooked before or during the smoking process"
heading_full_text: "Fish, dried, salted or in brine; smoked fish, whether or not cooked before or during the smoking process"
temperature_state: "processed"
processing_level: "preserved"
preservation_methods: "dried_salted_brined_smoked"
commercial_category: "value_added"
```

## Table: subheadings_0305
```sql
subheading_code: "0305.20"
subheading_description: "Livers, roes and milt of fish, dried, smoked, salted or in brine"
parent_category: "fish_offal"
classification_criteria: "edible_offal"
processing_level: "preserved"

subheading_code: "0305.31"
subheading_description: "Fish fillets, dried, salted or in brine, but not smoked: Tilapias, catfish, carp, eels, Nile perch and snakeheads"
parent_category: "preserved_fillets"
classification_criteria: "specified_freshwater"
processing_level: "preserved_not_smoked"

subheading_code: "0305.32"
subheading_description: "Fish fillets, dried, salted or in brine, but not smoked: Fish of families Bregmacerotidae through Muraenolepididae"
parent_category: "preserved_fillets"
classification_criteria: "cod_complex"
processing_level: "preserved_not_smoked"

subheading_code: "0305.39"
subheading_description: "Fish fillets, dried, salted or in brine, but not smoked: Other"
parent_category: "preserved_fillets"
classification_criteria: "other_species"
processing_level: "preserved_not_smoked"

subheading_code: "0305.41"
subheading_description: "Smoked fish, including fillets: Pacific salmon, Atlantic salmon and Danube salmon"
parent_category: "smoked_fish"
classification_criteria: "salmon_species"
processing_level: "smoked"

subheading_code: "0305.42"
subheading_description: "Smoked fish, including fillets: Herrings"
parent_category: "smoked_fish"
classification_criteria: "herring_species"
processing_level: "smoked"

subheading_code: "0305.43"
subheading_description: "Smoked fish, including fillets: Trout"
parent_category: "smoked_fish"
classification_criteria: "trout_species"
processing_level: "smoked"

subheading_code: "0305.44"
subheading_description: "Smoked fish, including fillets: Tilapias, catfish, carp, eels, Nile perch and snakeheads"
parent_category: "smoked_fish"
classification_criteria: "specified_freshwater"
processing_level: "smoked"

subheading_code: "0305.49"
subheading_description: "Smoked fish, including fillets: Other"
parent_category: "smoked_fish"
classification_criteria: "other_species"
processing_level: "smoked"

subheading_code: "0305.51"
subheading_description: "Fish, dried, whether or not salted but not smoked: Cod"
parent_category: "dried_fish"
classification_criteria: "cod_species"
processing_level: "dried_not_smoked"

subheading_code: "0305.59"
subheading_description: "Fish, dried, whether or not salted but not smoked: Other"
parent_category: "dried_fish"
classification_criteria: "other_species"
processing_level: "dried_not_smoked"

subheading_code: "0305.61"
subheading_description: "Fish, salted but not dried or smoked and fish in brine: Herrings"
parent_category: "salted_fish"
classification_criteria: "herring_species"
processing_level: "salted_not_dried_smoked"

subheading_code: "0305.62"
subheading_description: "Fish, salted but not dried or smoked and fish in brine: Cod"
parent_category: "salted_fish"
classification_criteria: "cod_species"
processing_level: "salted_not_dried_smoked"

subheading_code: "0305.63"
subheading_description: "Fish, salted but not dried or smoked and fish in brine: Anchovies"
parent_category: "salted_fish"
classification_criteria: "anchovy_species"
processing_level: "salted_not_dried_smoked"

subheading_code: "0305.69"
subheading_description: "Fish, salted but not dried or smoked and fish in brine: Other"
parent_category: "salted_fish"
classification_criteria: "other_species"
processing_level: "salted_not_dried_smoked"

subheading_code: "0305.71"
subheading_description: "Fish fins, heads, tails, maws and other edible fish offal: Shark fins"
parent_category: "fish_parts"
classification_criteria: "shark_fins"
processing_level: "preserved"

subheading_code: "0305.72"
subheading_description: "Fish fins, heads, tails, maws and other edible fish offal: Fish heads, tails and maws"
parent_category: "fish_parts"
classification_criteria: "heads_tails_maws"
processing_level: "preserved"

subheading_code: "0305.79"
subheading_description: "Fish fins, heads, tails, maws and other edible fish offal: Other"
parent_category: "fish_parts"
classification_criteria: "other_edible_parts"
processing_level: "preserved"
```

## Table: statistical_codes_0305
```sql
statistical_code: "0305.20.20.10"
description: "Sturgeon roe, dried, smoked, salted or in brine"
parent_subheading: "0305.20.20"
unit_of_quantity: "kg"
second_quantity: null
species: "Acipenser spp."
product_type: "caviar"
processing_level: "preserved"

statistical_code: "0305.20.20.20"
description: "Other fish roe, dried, smoked, salted or in brine"
parent_subheading: "0305.20.20"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
product_type: "roe"
processing_level: "preserved"

statistical_code: "0305.20.40.00"
description: "Fish livers and milt, dried, smoked, salted or in brine"
parent_subheading: "0305.20.40"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
product_type: "liver_milt"
processing_level: "preserved"

statistical_code: "0305.41.00.00"
description: "Pacific salmon, Atlantic salmon and Danube salmon, smoked"
parent_subheading: "0305.41.00"
unit_of_quantity: "kg"
second_quantity: null
species: "salmon_species"
product_type: "smoked_fish"
processing_level: "smoked"

statistical_code: "0305.59.20.00"
description: "Cod, dried"
parent_subheading: "0305.59.20"
unit_of_quantity: "kg"
second_quantity: null
species: "Gadus spp."
product_type: "dried_fish"
processing_level: "dried"

statistical_code: "0305.62.00.00"
description: "Cod, salted but not dried or smoked and cod in brine"
parent_subheading: "0305.62.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Gadus spp."
product_type: "salted_fish"
processing_level: "salted"
```

## Table: duty_rates_0305
```sql
statistical_code: "0305.20.20"
general_rate: "15% (sturgeon) 30% (other)"
general_rate_numeric: 15.00
general_rate_type: "ad_valorem"
special_rate: "Free-7.5%"
special_rate_numeric: 7.50
special_rate_type: "preferential_rate"
unit_of_duty: "kg"
product_differential: true

statistical_code: "0305.20.40"
general_rate: "6.6¢/kg"
general_rate_numeric: 6.60
general_rate_type: "specific"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0305.41.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0305.59.20"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0305.62.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
```

---

# HEADING 03.06 - Crustaceans

## Table: heading_0306
```sql
heading_code: "0306"
heading_description: "Crustaceans, whether in shell or not, live, fresh, chilled, frozen, dried, salted or in brine; smoked crustaceans; crustaceans, cooked by steaming or by boiling in water"
heading_full_text: "Crustaceans, whether in shell or not, live, fresh, chilled, frozen, dried, salted or in brine; smoked crustaceans, whether or not in shell; crustaceans, in shell, cooked by steaming or by boiling in water, whether or not chilled, frozen, dried, salted or in brine"
temperature_state: "all_states"
processing_level: "all_levels"
shell_condition: "in_shell_or_not"
commercial_category: "crustacean"
environmental_requirements: true
```

## Table: subheadings_0306
```sql
subheading_code: "0306.11"
subheading_description: "Frozen: Rock lobster and other sea crawfish (Palinurus spp., Panulirus spp., Jasus spp.)"
parent_category: "lobsters"
classification_criteria: "genus_species"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0306.12"
subheading_description: "Frozen: Lobsters (Homarus spp.)"
parent_category: "lobsters"
classification_criteria: "genus_species"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0306.14"
subheading_description: "Frozen: Crabs"
parent_category: "crabs"
classification_criteria: "crab_species"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0306.15"
subheading_description: "Frozen: Norway lobsters (Nephrops norvegicus)"
parent_category: "lobsters"
classification_criteria: "specific_species"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0306.16"
subheading_description: "Frozen: Cold-water shrimps and prawns (Pandalus spp., Crangon crangon)"
parent_category: "shrimps_prawns"
classification_criteria: "cold_water_species"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0306.17"
subheading_description: "Frozen: Other shrimps and prawns"
parent_category: "shrimps_prawns"
classification_criteria: "other_species"
temperature_state: "frozen"
shell_condition: "various"
size_classification: true

subheading_code: "0306.19"
subheading_description: "Frozen: Other, including flours, meals and pellets of crustaceans, fit for human consumption"
parent_category: "other_crustaceans"
classification_criteria: "not_elsewhere_specified"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0306.31"
subheading_description: "Live, fresh or chilled: Rock lobster and other sea crawfish"
parent_category: "lobsters"
classification_criteria: "genus_species"
temperature_state: "live_fresh_chilled"
shell_condition: "various"

subheading_code: "0306.32"
subheading_description: "Live, fresh or chilled: Lobsters (Homarus spp.)"
parent_category: "lobsters"
classification_criteria: "genus_species"
temperature_state: "live_fresh_chilled"
shell_condition: "various"

subheading_code: "0306.33"
subheading_description: "Live, fresh or chilled: Crabs"
parent_category: "crabs"
classification_criteria: "crab_species"
temperature_state: "live_fresh_chilled"
shell_condition: "various"

subheading_code: "0306.34"
subheading_description: "Live, fresh or chilled: Norway lobsters (Nephrops norvegicus)"
parent_category: "lobsters"
classification_criteria: "specific_species"
temperature_state: "live_fresh_chilled"
shell_condition: "various"

subheading_code: "0306.35"
subheading_description: "Live, fresh or chilled: Cold-water shrimps and prawns"
parent_category: "shrimps_prawns"
classification_criteria: "cold_water_species"
temperature_state: "live_fresh_chilled"
shell_condition: "various"

subheading_code: "0306.36"
subheading_description: "Live, fresh or chilled: Other shrimps and prawns"
parent_category: "shrimps_prawns"
classification_criteria: "other_species"
temperature_state: "live_fresh_chilled"
shell_condition: "various"

subheading_code: "0306.39"
subheading_description: "Live, fresh or chilled: Other"
parent_category: "other_crustaceans"
classification_criteria: "not_elsewhere_specified"
temperature_state: "live_fresh_chilled"
shell_condition: "various"

subheading_code: "0306.91"
subheading_description: "Other: Rock lobster and other sea crawfish"
parent_category: "lobsters"
classification_criteria: "genus_species"
temperature_state: "dried_salted_smoked_cooked"
shell_condition: "various"

subheading_code: "0306.92"
subheading_description: "Other: Lobsters (Homarus spp.)"
parent_category: "lobsters"
classification_criteria: "genus_species"
temperature_state: "dried_salted_smoked_cooked"
shell_condition: "various"

subheading_code: "0306.93"
subheading_description: "Other: Crabs"
parent_category: "crabs"
classification_criteria: "crab_species"
temperature_state: "dried_salted_smoked_cooked"
shell_condition: "various"

subheading_code: "0306.94"
subheading_description: "Other: Norway lobsters (Nephrops norvegicus)"
parent_category: "lobsters"
classification_criteria: "specific_species"
temperature_state: "dried_salted_smoked_cooked"
shell_condition: "various"

subheading_code: "0306.95"
subheading_description: "Other: Shrimps and prawns"
parent_category: "shrimps_prawns"
classification_criteria: "all_species"
temperature_state: "dried_salted_smoked_cooked"
shell_condition: "various"

subheading_code: "0306.99"
subheading_description: "Other: Other"
parent_category: "other_crustaceans"
classification_criteria: "not_elsewhere_specified"
temperature_state: "dried_salted_smoked_cooked"
shell_condition: "various"
```

## Table: statistical_codes_0306
```sql
statistical_code: "0306.14.20.00"
description: "King crab, frozen"
parent_subheading: "0306.14.20"
unit_of_quantity: "kg"
second_quantity: null
species: "Paralithodes spp."
temperature_state: "frozen"
crab_type: "king"

statistical_code: "0306.14.30.00"
description: "Snow crab, frozen"
parent_subheading: "0306.14.30"
unit_of_quantity: "kg"
second_quantity: null
species: "Chionoecetes spp."
temperature_state: "frozen"
crab_type: "snow"

statistical_code: "0306.14.40.00"
description: "Other crabs, frozen"
parent_subheading: "0306.14.40"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
temperature_state: "frozen"
crab_type: "other"

statistical_code: "0306.17.00.03"
description: "Shrimps and prawns, frozen, less than 15 per kg"
parent_subheading: "0306.17.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
temperature_state: "frozen"
size_category: "jumbo"
count_per_kg: "less_than_15"

statistical_code: "0306.17.00.06"
description: "Shrimps and prawns, frozen, 15-20 per kg"
parent_subheading: "0306.17.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
temperature_state: "frozen"
size_category: "extra_large"
count_per_kg: "15_to_20"

statistical_code: "0306.17.00.09"
description: "Shrimps and prawns, frozen, 21-25 per kg"
parent_subheading: "0306.17.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
temperature_state: "frozen"
size_category: "large"
count_per_kg: "21_to_25"

statistical_code: "0306.17.00.12"
description: "Shrimps and prawns, frozen, 26-30 per kg"
parent_subheading: "0306.17.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
temperature_state: "frozen"
size_category: "medium"
count_per_kg: "26_to_30"

statistical_code: "0306.17.00.15"
description: "Shrimps and prawns, frozen, more than 30 per kg"
parent_subheading: "0306.17.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
temperature_state: "frozen"
size_category: "small"
count_per_kg: "more_than_30"

statistical_code: "0306.93.00.10"
description: "Crabmeat, cooked"
parent_subheading: "0306.93.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
temperature_state: "cooked"
product_form: "meat"
```

## Table: duty_rates_0306
```sql
statistical_code: "0306.11.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0306.12.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0306.14.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0306.17.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
turtle_safe_required: true

statistical_code: "0306.93.00"
general_rate: "7.5% (crabmeat) 15% (other)"
general_rate_numeric: 7.50
general_rate_type: "ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
product_differential: true

statistical_code: "0306.95.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
```

---

# HEADING 03.07 - Molluscs

## Table: heading_0307
```sql
heading_code: "0307"
heading_description: "Molluscs, whether in shell or not, live, fresh, chilled, frozen, dried, salted or in brine; smoked molluscs, whether or not in shell"
heading_full_text: "Molluscs, whether in shell or not, live, fresh, chilled, frozen, dried, salted or in brine; smoked molluscs, whether or not in shell"
temperature_state: "all_states"
processing_level: "all_levels"
shell_condition: "in_shell_or_not"
commercial_category: "mollusc"
```

## Table: subheadings_0307
```sql
subheading_code: "0307.11"
subheading_description: "Oysters: Live, fresh or chilled"
parent_category: "bivalves"
classification_criteria: "oyster_species"
temperature_state: "live_fresh_chilled"
shell_condition: "in_shell"

subheading_code: "0307.12"
subheading_description: "Oysters: Frozen"
parent_category: "bivalves"
classification_criteria: "oyster_species"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0307.19"
subheading_description: "Oysters: Other"
parent_category: "bivalves"
classification_criteria: "oyster_species"
temperature_state: "dried_salted_smoked"
shell_condition: "various"

subheading_code: "0307.21"
subheading_description: "Scallops, including queen scallops, of the genera Pecten, Chlamys or Placopecten: Live, fresh or chilled"
parent_category: "bivalves"
classification_criteria: "scallop_genera"
temperature_state: "live_fresh_chilled"
shell_condition: "in_shell"

subheading_code: "0307.22"
subheading_description: "Scallops: Frozen"
parent_category: "bivalves"
classification_criteria: "scallop_genera"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0307.29"
subheading_description: "Scallops: Other"
parent_category: "bivalves"
classification_criteria: "scallop_genera"
temperature_state: "dried_salted_smoked"
shell_condition: "various"

subheading_code: "0307.31"
subheading_description: "Mussels (Mytilus spp., Perna spp.): Live, fresh or chilled"
parent_category: "bivalves"
classification_criteria: "mussel_genera"
temperature_state: "live_fresh_chilled"
shell_condition: "in_shell"

subheading_code: "0307.32"
subheading_description: "Mussels: Frozen"
parent_category: "bivalves"
classification_criteria: "mussel_genera"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0307.39"
subheading_description: "Mussels: Other"
parent_category: "bivalves"
classification_criteria: "mussel_genera"
temperature_state: "dried_salted_smoked"
shell_condition: "various"

subheading_code: "0307.42"
subheading_description: "Cuttle fish (Sepia officinalis, Rossia macrosoma, Sepiola spp.) and squid (Ommastrephes spp., Loligo spp., Nototodarus spp., Sepioteuthis spp.): Live, fresh or chilled"
parent_category: "cephalopods"
classification_criteria: "cuttlefish_squid_genera"
temperature_state: "live_fresh_chilled"
shell_condition: "no_shell"

subheading_code: "0307.43"
subheading_description: "Cuttle fish and squid: Frozen"
parent_category: "cephalopods"
classification_criteria: "cuttlefish_squid_genera"
temperature_state: "frozen"
shell_condition: "no_shell"

subheading_code: "0307.49"
subheading_description: "Cuttle fish and squid: Other"
parent_category: "cephalopods"
classification_criteria: "cuttlefish_squid_genera"
temperature_state: "dried_salted_smoked"
shell_condition: "no_shell"

subheading_code: "0307.51"
subheading_description: "Octopus (Octopus spp.): Live, fresh or chilled"
parent_category: "cephalopods"
classification_criteria: "octopus_genus"
temperature_state: "live_fresh_chilled"
shell_condition: "no_shell"

subheading_code: "0307.52"
subheading_description: "Octopus: Frozen"
parent_category: "cephalopods"
classification_criteria: "octopus_genus"
temperature_state: "frozen"
shell_condition: "no_shell"

subheading_code: "0307.59"
subheading_description: "Octopus: Other"
parent_category: "cephalopods"
classification_criteria: "octopus_genus"
temperature_state: "dried_salted_smoked"
shell_condition: "no_shell"

subheading_code: "0307.60"
subheading_description: "Snails, other than sea snails"
parent_category: "gastropods"
classification_criteria: "land_freshwater_snails"
temperature_state: "all_states"
shell_condition: "various"

subheading_code: "0307.71"
subheading_description: "Clams, cockles and ark shells (Arcidae, Cardiidae, Donacidae, Mactridae, Mesodesmatidae, Myidae, Semelidae, Solecurtidae, Solenidae, Tridacnidae and Veneridae): Live, fresh or chilled"
parent_category: "bivalves"
classification_criteria: "clam_families"
temperature_state: "live_fresh_chilled"
shell_condition: "in_shell"

subheading_code: "0307.72"
subheading_description: "Clams, cockles and ark shells: Frozen"
parent_category: "bivalves"
classification_criteria: "clam_families"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0307.79"
subheading_description: "Clams, cockles and ark shells: Other"
parent_category: "bivalves"
classification_criteria: "clam_families"
temperature_state: "dried_salted_smoked"
shell_condition: "various"

subheading_code: "0307.81"
subheading_description: "Abalone (Haliotis spp.): Live, fresh or chilled"
parent_category: "gastropods"
classification_criteria: "abalone_genus"
temperature_state: "live_fresh_chilled"
shell_condition: "in_shell"

subheading_code: "0307.82"
subheading_description: "Stromboid conchs (Strombus spp.): Live, fresh or chilled"
parent_category: "gastropods"
classification_criteria: "conch_genus"
temperature_state: "live_fresh_chilled"
shell_condition: "in_shell"

subheading_code: "0307.83"
subheading_description: "Abalone: Frozen"
parent_category: "gastropods"
classification_criteria: "abalone_genus"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0307.84"
subheading_description: "Stromboid conchs: Frozen"
parent_category: "gastropods"
classification_criteria: "conch_genus"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0307.87"
subheading_description: "Abalone: Other"
parent_category: "gastropods"
classification_criteria: "abalone_genus"
temperature_state: "dried_salted_smoked"
shell_condition: "various"

subheading_code: "0307.88"
subheading_description: "Stromboid conchs: Other"
parent_category: "gastropods"
classification_criteria: "conch_genus"
temperature_state: "dried_salted_smoked"
shell_condition: "various"

subheading_code: "0307.91"
subheading_description: "Other molluscs: Live, fresh or chilled"
parent_category: "other_molluscs"
classification_criteria: "not_elsewhere_specified"
temperature_state: "live_fresh_chilled"
shell_condition: "various"

subheading_code: "0307.92"
subheading_description: "Other molluscs: Frozen"
parent_category: "other_molluscs"
classification_criteria: "not_elsewhere_specified"
temperature_state: "frozen"
shell_condition: "various"

subheading_code: "0307.99"
subheading_description: "Other molluscs: Other"
parent_category: "other_molluscs"
classification_criteria: "not_elsewhere_specified"
temperature_state: "dried_salted_smoked"
shell_condition: "various"
```

## Table: statistical_codes_0307
```sql
statistical_code: "0307.11.00.00"
description: "Oysters, live, fresh or chilled"
parent_subheading: "0307.11.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Crassostrea/Ostrea spp."
temperature_state: "live_fresh_chilled"
shell_condition: "in_shell"

statistical_code: "0307.21.00.00"
description: "Scallops, live, fresh or chilled"
parent_subheading: "0307.21.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Pecten/Chlamys/Placopecten spp."
temperature_state: "live_fresh_chilled"
shell_condition: "in_shell"

statistical_code: "0307.43.00.00"
description: "Cuttle fish and squid, frozen"
parent_subheading: "0307.43.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Sepia/Loligo/Ommastrephes spp."
temperature_state: "frozen"
shell_condition: "no_shell"

statistical_code: "0307.60.00.00"
description: "Snails, other than sea snails"
parent_subheading: "0307.60.00"
unit_of_quantity: "kg"
second_quantity: null
species: "land_freshwater_snails"
temperature_state: "all_states"
shell_condition: "in_shell"

statistical_code: "0307.91.00.00"
description: "Other molluscs, live, fresh or chilled"
parent_subheading: "0307.91.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
temperature_state: "live_fresh_chilled"
shell_condition: "various"
```

## Table: duty_rates_0307
```sql
statistical_code: "0307.11.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0307.21.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0307.43.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0307.60.00"
general_rate: "5%"
general_rate_numeric: 5.00
general_rate_type: "ad_valorem"
special_rate: "Free-2.5%"
special_rate_numeric: 2.50
special_rate_type: "preferential_rate"
unit_of_duty: "kg"

statistical_code: "0307.91.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
```

---

# HEADING 03.08 - Aquatic Invertebrates Other Than Crustaceans and Molluscs

## Table: heading_0308
```sql
heading_code: "0308"
heading_description: "Aquatic invertebrates other than crustaceans and molluscs, live, fresh, chilled, frozen, dried, salted or in brine; smoked aquatic invertebrates other than crustaceans and molluscs"
heading_full_text: "Aquatic invertebrates other than crustaceans and molluscs, live, fresh, chilled, frozen, dried, salted or in brine; smoked aquatic invertebrates other than crustaceans and molluscs"
temperature_state: "all_states"
processing_level: "all_levels"
commercial_category: "other_aquatic_invertebrates"
excludes: "crustaceans_molluscs"
```

## Table: subheadings_0308
```sql
subheading_code: "0308.11"
subheading_description: "Sea cucumbers (Stichopus japonicus, Holothuroidea): Live, fresh or chilled"
parent_category: "echinoderms"
classification_criteria: "sea_cucumber_species"
temperature_state: "live_fresh_chilled"

subheading_code: "0308.12"
subheading_description: "Sea cucumbers: Frozen"
parent_category: "echinoderms"
classification_criteria: "sea_cucumber_species"
temperature_state: "frozen"

subheading_code: "0308.19"
subheading_description: "Sea cucumbers: Other"
parent_category: "echinoderms"
classification_criteria: "sea_cucumber_species"
temperature_state: "dried_salted_smoked"

subheading_code: "0308.21"
subheading_description: "Sea urchins (Strongylocentrotus spp., Paracentrotus lividus, Loxechinus albus, Echichinus esculentus): Live, fresh or chilled"
parent_category: "echinoderms"
classification_criteria: "sea_urchin_species"
temperature_state: "live_fresh_chilled"

subheading_code: "0308.22"
subheading_description: "Sea urchins: Frozen"
parent_category: "echinoderms"
classification_criteria: "sea_urchin_species"
temperature_state: "frozen"

subheading_code: "0308.29"
subheading_description: "Sea urchins: Other"
parent_category: "echinoderms"
classification_criteria: "sea_urchin_species"
temperature_state: "dried_salted_smoked"

subheading_code: "0308.30"
subheading_description: "Jellyfish (Rhopilema spp.)"
parent_category: "cnidarians"
classification_criteria: "jellyfish_genus"
temperature_state: "all_states"

subheading_code: "0308.90"
subheading_description: "Other"
parent_category: "other_invertebrates"
classification_criteria: "not_elsewhere_specified"
temperature_state: "all_states"
```

## Table: statistical_codes_0308
```sql
statistical_code: "0308.11.00.00"
description: "Sea cucumbers, live, fresh or chilled"
parent_subheading: "0308.11.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Stichopus japonicus/Holothuroidea"
temperature_state: "live_fresh_chilled"

statistical_code: "0308.21.00.00"
description: "Sea urchins, live, fresh or chilled"
parent_subheading: "0308.21.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Strongylocentrotus/Paracentrotus spp."
temperature_state: "live_fresh_chilled"

statistical_code: "0308.30.00.00"
description: "Jellyfish"
parent_subheading: "0308.30.00"
unit_of_quantity: "kg"
second_quantity: null
species: "Rhopilema spp."
temperature_state: "all_states"

statistical_code: "0308.90.00.00"
description: "Other aquatic invertebrates"
parent_subheading: "0308.90.00"
unit_of_quantity: "kg"
second_quantity: null
species: "various"
temperature_state: "all_states"
```

## Table: duty_rates_0308
```sql
statistical_code: "0308.11.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0308.21.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0308.30.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"

statistical_code: "0308.90.00"
general_rate: "Free"
general_rate_numeric: 0.00
general_rate_type: "duty_free"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
```

---

# HEADING 03.09 - Flours, Meals and Pellets Fit for Human Consumption

## Table: heading_0309
```sql
heading_code: "0309"
heading_description: "Flours, meals and pellets of fish, crustaceans, molluscs or other aquatic invertebrates, fit for human consumption"
heading_full_text: "Flours, meals and pellets of fish, crustaceans, molluscs or other aquatic invertebrates, fit for human consumption"
temperature_state: "processed"
processing_level: "ground_pelletized"
human_consumption: true
commercial_category: "processed_products"
```

## Table: subheadings_0309
```sql
subheading_code: "0309.10"
subheading_description: "Of fish"
parent_category: "fish_products"
classification_criteria: "fish_source"
processing_level: "flour_meal_pellet"
human_consumption: true

subheading_code: "0309.90"
subheading_description: "Other"
parent_category: "other_aquatic"
classification_criteria: "crustacean_mollusc_other"
processing_level: "flour_meal_pellet"
human_consumption: true
```

## Table: statistical_codes_0309
```sql
statistical_code: "0309.10.00.10"
description: "Fish flour, meal and pellets, in bulk or in immediate packagings weighing 6.8 kg or more each"
parent_subheading: "0309.10.00"
unit_of_quantity: "kg"
second_quantity: null
source_material: "fish"
packaging_type: "bulk"
processing_level: "flour_meal_pellet"

statistical_code: "0309.10.00.20"
description: "Fish flour, meal and pellets, not in bulk or in immediate packagings weighing 6.8 kg or more each"
parent_subheading: "0309.10.00"
unit_of_quantity: "kg"
second_quantity: null
source_material: "fish"
packaging_type: "retail"
processing_level: "flour_meal_pellet"

statistical_code: "0309.90.00.00"
description: "Other flours, meals and pellets"
parent_subheading: "0309.90.00"
unit_of_quantity: "kg"
second_quantity: null
source_material: "crustacean_mollusc_other"
packaging_type: "all"
processing_level: "flour_meal_pellet"
```

## Table: duty_rates_0309
```sql
statistical_code: "0309.10.00"
general_rate: "Free (bulk) 6% (retail)"
general_rate_numeric: 0.00
general_rate_type: "duty_free_or_ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
packaging_differential: true

statistical_code: "0309.90.00"
general_rate: "Free (bulk) 25% (retail)"
general_rate_numeric: 0.00
general_rate_type: "duty_free_or_ad_valorem"
special_rate: "Free"
special_rate_numeric: 0.00
special_rate_type: "duty_free"
unit_of_duty: "kg"
packaging_differential: true
```

---

# NORMALIZED REFERENCE TABLES

## Table: trade_programs
```sql
program_code: "USMCA"
program_name: "United States-Mexico-Canada Agreement"
participating_countries: "Canada, Mexico"
status: "active"

program_code: "FTA"
program_name: "Free Trade Agreement Partners"
participating_countries: "Australia, Chile, Colombia, Panama, Peru, South Korea"
status: "active"

program_code: "GSP"
program_name: "Generalized System of Preferences"
participating_countries: "Various developing countries"
status: "active"

program_code: "CBI"
program_name: "Caribbean Basin Initiative"
participating_countries: "Caribbean and Central American countries"
status: "active"

program_code: "ATPA"
program_name: "Andean Trade Preference Act"
participating_countries: "Bolivia, Colombia, Ecuador, Peru"
status: "active"
```

## Table: units_of_measure
```sql
unit_code: "kg"
unit_description: "Kilogram"
unit_type: "weight"
base_unit: "kg"

unit_code: "No."
unit_description: "Number"
unit_type: "count"
base_unit: "No."

unit_code: "MT"
unit_description: "Metric Ton"
unit_type: "weight"
base_unit: "kg"
conversion_to_base: 1000

unit_code: "L"
unit_description: "Liter"
unit_type: "volume"
base_unit: "L"

unit_code: "doz"
unit_description: "Dozen"
unit_type: "count"
base_unit: "No."
conversion_to_base: 12
```

## Table: duty_rate_types
```sql
rate_type: "duty_free"
description: "No duty charged"
calculation_method: "zero_rate"

rate_type: "specific"
description: "Fixed amount per unit"
calculation_method: "cents_per_kg"

rate_type: "ad_valorem"
description: "Percentage of value"
calculation_method: "percentage_of_value"

rate_type: "compound"
description: "Specific rate plus ad valorem"
calculation_method: "specific_plus_percentage"

rate_type: "alternative"
description: "Choice between two rates"
calculation_method: "higher_of_two_rates"
```

## Table: environmental_programs
```sql
program_code: "TURTLE_SAFE"
program_name: "Turtle-Safe Harvesting Requirements"
affected_products: "Shrimp and prawns"
implementing_authority: "NMFS"
status: "active"
public_law_reference: "Section 609 of Public Law 101-162"

program_code: "DOLPHIN_SAFE"
program_name: "Dolphin-Safe Tuna Requirements"
affected_products: "Tuna products"
implementing_authority: "NMFS"
status: "active"

program_code: "MMPA"
program_name: "Marine Mammal Protection Act"
affected_products: "Various fish products"
implementing_authority: "NMFS"
status: "active"

program_code: "CITES"
program_name: "Convention on International Trade in Endangered Species"
affected_products: "Endangered fish species"
implementing_authority: "USFWS"
status: "active"
```

## Table: scientific_classifications
```sql
taxonomic_kingdom: "Animalia"
taxonomic_phylum: "Chordata"
taxonomic_class: "Actinopterygii"
taxonomic_order: "Salmoniformes"
taxonomic_family: "Salmonidae"
taxonomic_genus: "Salmo"
common_name: "Atlantic Salmon"

taxonomic_kingdom: "Animalia"
taxonomic_phylum: "Arthropoda"
taxonomic_class: "Malacostraca"
taxonomic_order: "Decapoda"
taxonomic_family: "Nephropidae"
taxonomic_genus: "Homarus"
common_name: "Lobster"

taxonomic_kingdom: "Animalia"
taxonomic_phylum: "Mollusca"
taxonomic_class: "Bivalvia"
taxonomic_order: "Ostreoida"
taxonomic_family: "Ostreidae"
taxonomic_genus: "Crassostrea"
common_name: "Oyster"

taxonomic_kingdom: "Animalia"
taxonomic_phylum: "Cnidaria"
taxonomic_class: "Scyphozoa"
taxonomic_order: "Rhizostomeae"
taxonomic_family: "Rhizostomatidae"
taxonomic_genus: "Rhopilema"
common_name: "Jellyfish"
```

---

# DATA VALIDATION RULES

## Required Fields Validation
```sql
-- All statistical codes must have:
statistical_code: NOT NULL, FORMAT: ####.##.##.##
description: NOT NULL, MIN_LENGTH: 10
parent_subheading: NOT NULL, FOREIGN_KEY: subheadings
unit_of_quantity: NOT NULL, FOREIGN_KEY: units_of_measure

-- All duty rates must have:
general_rate: NOT NULL
special_rate: NOT NULL
unit_of_duty: NOT NULL

-- Species classifications must have:
species: NOT NULL, MIN_LENGTH: 3
temperature_state: NOT NULL
processing_level: NOT NULL
```

## Business Rules Validation
```sql
-- Live fish must have temperature_state = "live_fresh_chilled"
IF heading_code = "0301" THEN temperature_state IN ("live_fresh_chilled")

-- Frozen products must have temperature_state = "frozen"
IF subheading_code LIKE "%frozen%" THEN temperature_state = "frozen"

-- Shrimp imports must have turtle_safe_required flag
IF species LIKE "%shrimp%" OR species LIKE "%prawn%" THEN turtle_safe_required = true

-- Size classifications must be consistent with count per kg
IF count_per_kg = "less_than_15" THEN size_category = "jumbo"
IF count_per_kg = "15_to_20" THEN size_category = "extra_large"

-- Statistical codes must match parent subheading pattern
statistical_code LIKE parent_subheading + "%"

-- Packaging differentials must have both bulk and retail rates
IF packaging_differential = true THEN packaging_type IN ("bulk", "retail")
```

## Data Type Constraints
```sql
-- Numeric fields
general_rate_numeric: DECIMAL(10,2)
special_rate_numeric: DECIMAL(10,2)
conversion_to_base: INTEGER

-- Text fields
description: VARCHAR(500)
classification_criteria: VARCHAR(100)
species: VARCHAR(200)
scientific_classification: VARCHAR(100)

-- Boolean fields
turtle_safe_required: BOOLEAN DEFAULT false
packaging_differential: BOOLEAN DEFAULT false
human_consumption: BOOLEAN DEFAULT true

-- Enumeration fields
temperature_state: ENUM('live_fresh_chilled', 'frozen', 'processed', 'all_states')
processing_level: ENUM('whole_fish', 'filleted', 'other_meat', 'preserved', 'flour_meal_pellet')
```

---

**Database Schema Version**: 1.0  
**SQLite Compatible**: Yes  
**Python Scraping Ready**: Yes  
**Total Data Points**: 350+  
**Normalization Level**: 3NF  
**Last Updated**: 2025-08-26