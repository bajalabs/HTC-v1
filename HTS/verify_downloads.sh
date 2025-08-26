#!/bin/bash

# Verify all downloads are complete
set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() { echo -e "${BLUE}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}✓${NC} $1"; }
error() { echo -e "${RED}✗${NC} $1"; }
warning() { echo -e "${YELLOW}⚠${NC} $1"; }

# Base directory
BASE_DIR="/Users/ivi/VIBE/RATIOS/HTC/HTC-v1/HTS"
cd "$BASE_DIR"

log "HTS Download Verification Report"
log "================================"

total_chapters=97
complete_chapters=0
incomplete_chapters=0
missing_files=0

echo ""
echo "Chapter Status Report:"
echo "====================="

for chapter in {1..97}; do
    chapter_num=$(printf "%02d" $chapter)
    chapter_folder=$(find . -name "Chapter_${chapter_num}_*" -type d | head -1)
    
    if [ -z "$chapter_folder" ]; then
        error "Chapter $chapter: Folder not found"
        incomplete_chapters=$((incomplete_chapters + 1))
        continue
    fi
    
    # Check for all three files
    census_file="$chapter_folder/c${chapter_num}.pdf"
    usitc_file="$chapter_folder/Chapter ${chapter}_2025HTSRev19.pdf"
    
    # WCO filename varies by chapter
    wco_files=$(find "$chapter_folder" -name "*_2022e.pdf" -type f)
    wco_count=$(echo "$wco_files" | wc -w)
    
    census_exists=0
    wco_exists=0
    usitc_exists=0
    
    if [ -f "$census_file" ]; then
        census_exists=1
    fi
    
    if [ $wco_count -gt 0 ]; then
        wco_exists=1
    fi
    
    if [ -f "$usitc_file" ]; then
        usitc_exists=1
    fi
    
    total_files=$((census_exists + wco_exists + usitc_exists))
    
    if [ $total_files -eq 3 ]; then
        success "Chapter $chapter: Complete (3/3 files)"
        complete_chapters=$((complete_chapters + 1))
    else
        warning "Chapter $chapter: Incomplete ($total_files/3 files)"
        incomplete_chapters=$((incomplete_chapters + 1))
        
        if [ $census_exists -eq 0 ]; then
            echo "    Missing: Census file"
            missing_files=$((missing_files + 1))
        fi
        if [ $wco_exists -eq 0 ]; then
            echo "    Missing: WCO file"
            missing_files=$((missing_files + 1))
        fi
        if [ $usitc_exists -eq 0 ]; then
            echo "    Missing: USITC file"
            missing_files=$((missing_files + 1))
        fi
    fi
done

echo ""
log "Summary Report"
log "=============="
echo "Total Chapters: $total_chapters"
echo "Complete Chapters: $complete_chapters"
echo "Incomplete Chapters: $incomplete_chapters"
echo "Missing Files: $missing_files"

total_pdfs=$(find . -name "*.pdf" -type f | wc -l | tr -d ' ')
echo "Total PDF Files: $total_pdfs"

# Expected: 97 chapters × 3 sources = 291 files
# But Chapter 77 might be missing some files in certain systems
expected_files=291
echo "Expected Files: ~$expected_files (may vary for reserved chapters)"

if [ $complete_chapters -eq $total_chapters ]; then
    success "All chapters are complete!"
else
    warning "$incomplete_chapters chapters need attention"
fi

echo ""
log "File size summary:"
find . -name "*.pdf" -type f -exec ls -lh {} \; | awk '{print $5, $9}' | sort -hr | head -10
