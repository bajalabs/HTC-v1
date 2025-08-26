# HTS File Analysis and Organization Plan

## Overview
We have successfully downloaded 285+ files (95 chapters × 3 formats each) from the USITC HTS website. All files are currently named `htsdata.csv`, `htsdata.json`, and `htsdata.xlsx` in various timestamp folders within the playwright output directory.

## Current File Structure
```
playwright-mcp-output/
├── 2025-08-26T00-46-44.652Z/
│   ├── htsdata.csv
│   ├── htsdata.xlsx
│   └── htsdata.json
├── 2025-08-26T01-56-33.860Z/
│   ├── htsdata.csv
│   ├── htsdata.xlsx
│   └── htsdata.json
└── ... (285+ more files in ~95 timestamp folders)
```

## Analysis Strategy

### Step 1: File Content Analysis
Each file needs to be analyzed to determine which HTS Chapter it contains by examining:

1. **HTS Number Patterns**: 
   - Chapter 1: HTS numbers start with "01" (0101, 0102, etc.)
   - Chapter 2: HTS numbers start with "02" (0201, 0202, etc.)
   - Chapter 6: HTS numbers start with "06" (0601, 0602, etc.)
   - Chapter 97: HTS numbers start with "97" (9701, 9706, etc.)

2. **Description Content**:
   - Chapter 1: "Live animals"
   - Chapter 6: "Live trees and other plants; bulbs, roots..."
   - Chapter 95: "Toys, games and sports requisites"
   - Chapter 97: "Works of art, collectors' pieces and antiques"

### Step 2: File Identification Script
Create a script that:
1. Scans all timestamp folders in playwright-mcp-output
2. Reads the first few lines of each CSV file to identify HTS numbers
3. Extracts chapter number from HTS codes
4. Maps each file to its corresponding chapter

### Step 3: Target Directory Structure
```
HTS/
├── chapters/
│   ├── chapter-01/
│   │   ├── chapter-01-live-animals.csv
│   │   ├── chapter-01-live-animals.xlsx
│   │   └── chapter-01-live-animals.json
│   ├── chapter-02/
│   │   ├── chapter-02-meat-and-edible-meat-offal.csv
│   │   ├── chapter-02-meat-and-edible-meat-offal.xlsx
│   │   └── chapter-02-meat-and-edible-meat-offal.json
│   ├── chapter-06/  # (No Chapter 6 - skipped during download)
│   ├── chapter-95/
│   │   ├── chapter-95-toys-games-sports.csv
│   │   ├── chapter-95-toys-games-sports.xlsx
│   │   └── chapter-95-toys-games-sports.json
│   ├── chapter-96/
│   │   ├── chapter-96-miscellaneous-manufactured-articles.csv
│   │   ├── chapter-96-miscellaneous-manufactured-articles.xlsx
│   │   └── chapter-96-miscellaneous-manufactured-articles.json
│   └── chapter-97/
│       ├── chapter-97-works-of-art-collectors-pieces.csv
│       ├── chapter-97-works-of-art-collectors-pieces.xlsx
│       └── chapter-97-works-of-art-collectors-pieces.json
├── analysis/
│   ├── file_mapping.csv
│   ├── chapter_summary.md
│   └── missing_chapters.txt
└── scripts/
    ├── analyze_files.py
    ├── organize_files.py
    └── validate_chapters.py
```

## Implementation Plan

### Phase 1: Analysis Script Development
1. **File Scanner**: Script to find all htsdata files in timestamp folders
2. **Chapter Identifier**: Function to read CSV files and extract chapter numbers
3. **Mapping Generator**: Create mapping file showing which timestamp folder contains which chapter

### Phase 2: Chapter Name Mapping
Based on our download history, create mapping of chapter numbers to descriptive names:
```python
CHAPTER_NAMES = {
    1: "live-animals",
    2: "meat-and-edible-meat-offal", 
    3: "fish-and-crustaceans",
    4: "dairy-produce-birds-eggs",
    5: "products-of-animal-origin",
    7: "edible-vegetables-and-roots",  # Chapter 6 was skipped
    8: "edible-fruit-and-nuts",
    # ... continuing through all chapters
    95: "toys-games-sports",
    96: "miscellaneous-manufactured-articles", 
    97: "works-of-art-collectors-pieces"
}
```

### Phase 3: File Organization
1. **Directory Creation**: Create chapter-specific folders
2. **File Copying**: Copy and rename files from timestamp folders to chapter folders
3. **Validation**: Verify all expected chapters are present and files are valid

### Phase 4: Quality Assurance
1. **File Integrity Check**: Verify file sizes and basic structure
2. **Chapter Coverage**: Confirm we have all expected chapters (minus 6 and 77)
3. **Format Consistency**: Ensure CSV, JSON, and Excel files contain same data

## Expected Outcomes

### Chapter Distribution
- **Total Expected**: 95 chapters (97 total minus Chapter 6 and Chapter 77)
- **File Count**: 285 files (95 chapters × 3 formats)
- **Chapters with Data**: 1-5, 7-97 (excluding 6 and 77)

### File Naming Convention
`chapter-{XX}-{descriptive-name}.{extension}`

Examples:
- `chapter-01-live-animals.csv`
- `chapter-95-toys-games-sports.json`
- `chapter-97-works-of-art-collectors-pieces.xlsx`

## Next Steps
1. Implement the analysis script to identify chapters
2. Create the directory structure
3. Execute the file organization process
4. Validate the results
5. Generate summary reports

## Notes
- Chapter 6: No data available (skipped during download)
- Chapter 77: Reserved chapter with no data (503 server error during download)
- All other chapters (1-5, 7-97) should have complete data in all three formats

This plan will transform our current disorganized collection of timestamp-named files into a well-structured, easily navigable HTS database organized by chapter with descriptive names.
