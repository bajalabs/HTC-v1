# HTS File Organization Scripts

This directory contains scripts to analyze and organize the downloaded HTS (Harmonized Tariff Schedule) files from the USITC website.

## Files Overview

### 1. `analyze_hts_files.py`
**Purpose**: Analyzes all downloaded HTS files to identify which chapter each file contains.

**What it does**:
- Scans all timestamp directories in `playwright-mcp-output`
- Reads CSV files to extract HTS numbers and identify chapters
- Creates mapping files showing which directory contains which chapter
- Generates analysis summary reports

**Output**:
- `analysis/file_mapping.csv` - CSV mapping of files to chapters
- `analysis/file_mapping.json` - JSON mapping of files to chapters  
- `analysis/analysis_summary.md` - Summary report with statistics

### 2. `organize_hts_files.py`
**Purpose**: Organizes files into chapter-specific directories with proper naming.

**What it does**:
- Uses the mapping from `analyze_hts_files.py`
- Creates `chapters/` directory structure
- Copies and renames files with descriptive names
- Validates the organization was successful

**Output**:
- `chapters/chapter-XX/` directories for each chapter
- Files renamed as `chapter-XX-descriptive-name.{csv,json,xlsx}`
- `analysis/organization_report.md` - Organization results report

### 3. `run_hts_organization.py`
**Purpose**: Runs the complete workflow (analysis + organization).

**What it does**:
- Checks prerequisites (playwright output exists)
- Runs analysis script
- Runs organization script
- Provides final summary

## Usage

### Option 1: Run Complete Workflow (Recommended)
```bash
cd scripts
python3 run_hts_organization.py
```

### Option 2: Run Scripts Individually
```bash
cd scripts

# Step 1: Analyze files
python3 analyze_hts_files.py

# Step 2: Organize files
python3 organize_hts_files.py
```

## Prerequisites

1. **Playwright Output Directory**: `playwright-mcp-output/` must exist with downloaded HTS files
2. **Python 3**: Scripts require Python 3.6+
3. **Required Python modules**: `csv`, `json`, `pandas`, `pathlib`, `re` (all standard library)

## Expected Input Structure
```
playwright-mcp-output/
├── 2025-08-26T00-46-44.652Z/
│   ├── htsdata.csv
│   ├── htsdata.json
│   └── htsdata.xlsx
├── 2025-08-26T01-56-33.860Z/
│   ├── htsdata.csv
│   ├── htsdata.json
│   └── htsdata.xlsx
└── ... (285+ more files in ~95 timestamp folders)
```

## Expected Output Structure
```
HTS/
├── chapters/
│   ├── chapter-01/
│   │   ├── chapter-01-live-animals.csv
│   │   ├── chapter-01-live-animals.json
│   │   └── chapter-01-live-animals.xlsx
│   ├── chapter-02/
│   │   ├── chapter-02-meat-and-edible-meat-offal.csv
│   │   ├── chapter-02-meat-and-edible-meat-offal.json
│   │   └── chapter-02-meat-and-edible-meat-offal.xlsx
│   └── ... (95 chapter directories)
└── analysis/
    ├── file_mapping.csv
    ├── file_mapping.json
    ├── analysis_summary.md
    └── organization_report.md
```

## Chapter Information

The scripts handle all HTS chapters (1-99) with these exceptions:
- **Chapter 6**: No data available (was skipped during download)
- **Chapter 77**: Reserved chapter with no data (503 server error during download)

Expected chapters with data: **95 chapters** (1-5, 7-97, 98-99)

## Troubleshooting

### "Playwright output directory not found"
- Ensure you've successfully downloaded HTS files using the browser automation
- Check that `playwright-mcp-output/` exists in the parent directory

### "No timestamp directories found"
- Verify the download process completed successfully
- Check directory names match pattern: `YYYY-MM-DDTHH-MM-SS.sssZ`

### "Could not identify chapter"
- Some files may have unexpected format
- Check the CSV files manually to verify HTS number format
- Review analysis summary for details on unidentified files

### "Failed to copy files"
- Check file permissions
- Ensure sufficient disk space
- Verify source files exist and are readable

## File Naming Convention

Files are renamed using this pattern:
`chapter-{XX}-{descriptive-name}.{extension}`

Where:
- `XX` = Two-digit chapter number (01, 02, ..., 97)
- `descriptive-name` = Kebab-case description of chapter content
- `extension` = Original file extension (csv, json, xlsx)

Examples:
- `chapter-01-live-animals.csv`
- `chapter-95-toys-games-sports.json`
- `chapter-97-works-of-art-collectors-pieces.xlsx`
