#!/bin/bash

# USITC Export Download Script with Proper File Handling
# Downloads CSV, Excel, and JSON files for all HTS chapters

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log() { echo -e "${BLUE}[$(date +'%H:%M:%S')]${NC} $1"; }
success() { echo -e "${GREEN}✓${NC} $1"; }
error() { echo -e "${RED}✗${NC} $1"; }
warning() { echo -e "${YELLOW}⚠${NC} $1"; }

# Base directory
BASE_DIR="/Users/ivi/VIBE/RATIOS/HTC/HTC-v1/HTS"
cd "$BASE_DIR"

log "🚀 Starting USITC Export Download Process"
log "📁 Working directory: $BASE_DIR"

# Function to get chapter folder name
get_chapter_folder() {
    local chapter=$1
    local chapter_num=$(printf "%02d" $chapter)
    find . -name "Chapter_${chapter_num}_*" -type d | head -1
}

# Function to process downloaded files
process_chapter_files() {
    local chapter=$1
    local chapter_folder="$2"
    
    log "Processing downloaded files for Chapter $chapter"
    
    # Look for downloaded files in common browser download locations
    local download_paths=(
        "/tmp/playwright-mcp-output"
        "$HOME/Downloads"
        "/tmp"
    )
    
    local files_found=0
    
    for path in "${download_paths[@]}"; do
        if [ -d "$path" ]; then
            # Find recently downloaded htsdata files
            local csv_file=$(find "$path" -name "htsdata.csv" -mtime -1 2>/dev/null | head -1)
            local xlsx_file=$(find "$path" -name "htsdata.xlsx" -mtime -1 2>/dev/null | head -1)
            local json_file=$(find "$path" -name "htsdata.json" -mtime -1 2>/dev/null | head -1)
            
            if [ -n "$csv_file" ] && [ -f "$csv_file" ]; then
                cp "$csv_file" "$chapter_folder/Chapter_$(printf '%02d' $chapter)_2025_HTS.csv"
                success "Copied CSV file for Chapter $chapter"
                ((files_found++))
            fi
            
            if [ -n "$xlsx_file" ] && [ -f "$xlsx_file" ]; then
                cp "$xlsx_file" "$chapter_folder/Chapter_$(printf '%02d' $chapter)_2025_HTS.xlsx"
                success "Copied Excel file for Chapter $chapter"
                ((files_found++))
            fi
            
            if [ -n "$json_file" ] && [ -f "$json_file" ]; then
                cp "$json_file" "$chapter_folder/Chapter_$(printf '%02d' $chapter)_2025_HTS.json"
                success "Copied JSON file for Chapter $chapter"
                ((files_found++))
            fi
        fi
    done
    
    if [ $files_found -eq 0 ]; then
        warning "No files found for Chapter $chapter"
        return 1
    else
        success "Processed $files_found files for Chapter $chapter"
        return 0
    fi
}

# Main processing function
process_chapter() {
    local chapter=$1
    local chapter_num=$(printf "%02d" $chapter)
    
    log "📋 Processing Chapter $chapter"
    
    # Find the chapter folder
    local chapter_folder=$(get_chapter_folder $chapter)
    if [ -z "$chapter_folder" ]; then
        error "Chapter folder not found for Chapter $chapter"
        return 1
    fi
    
    success "Found chapter folder: $chapter_folder"
    
    # Check if files already exist
    local existing_files=0
    [ -f "$chapter_folder/Chapter_${chapter_num}_2025_HTS.csv" ] && ((existing_files++))
    [ -f "$chapter_folder/Chapter_${chapter_num}_2025_HTS.xlsx" ] && ((existing_files++))
    [ -f "$chapter_folder/Chapter_${chapter_num}_2025_HTS.json" ] && ((existing_files++))
    
    if [ $existing_files -eq 3 ]; then
        success "Chapter $chapter already has all 3 export files - skipping"
        return 0
    fi
    
    log "Chapter $chapter needs export files (has $existing_files/3)"
    
    # Note: Browser automation would happen here
    # For now, we'll prepare the structure and wait for manual browser automation
    
    return 0
}

# Process chapters
log "📊 Starting chapter processing..."

total_chapters=97
processed=0
skipped=0
errors=0

for chapter in {1..97}; do
    if process_chapter $chapter; then
        ((processed++))
    else
        ((errors++))
    fi
done

log "📈 Processing Summary:"
log "   Total chapters: $total_chapters"
log "   Processed: $processed"
log "   Errors: $errors"

success "USITC export download preparation completed!"
