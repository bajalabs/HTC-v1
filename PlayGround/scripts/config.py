"""
Configuration file for HTS file organization scripts.
Adjust these paths as needed for your setup.
"""

# Directory paths
PLAYWRIGHT_OUTPUT_DIR = "../playwright-mcp-output11"  # Adjust this to match your actual directory
ANALYSIS_OUTPUT_DIR = "../analysis"
CHAPTERS_OUTPUT_DIR = "../chapters"

# File patterns
HTS_CSV_FILENAME = "htsdata.csv"
HTS_JSON_FILENAME = "htsdata.json"
HTS_XLSX_FILENAME = "htsdata.xlsx"

# Expected chapters (excluding 6 and 77 which were skipped/empty)
EXPECTED_CHAPTERS = set(range(1, 100)) - {6, 77}

print(f"Configuration loaded:")
print(f"  Playwright output: {PLAYWRIGHT_OUTPUT_DIR}")
print(f"  Analysis output: {ANALYSIS_OUTPUT_DIR}")
print(f"  Chapters output: {CHAPTERS_OUTPUT_DIR}")
print(f"  Expected chapters: {len(EXPECTED_CHAPTERS)} chapters")
