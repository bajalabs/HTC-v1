#!/bin/bash

# USITC Export Automation Script
# Downloads CSV, Excel, and JSON formats for all HTS chapters 6-97

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log() { echo -e "${BLUE}[$(date +'%H:%M:%S')]${NC} $1"; }
success() { echo -e "${GREEN}✓${NC} $1"; }
error() { echo -e "${RED}✗${NC} $1"; }
warning() { echo -e "${YELLOW}⚠${NC} $1"; }

# Base directory
BASE_DIR="/Users/ivi/VIBE/RATIOS/HTC/HTC-v1/HTS"
cd "$BASE_DIR"

log "🚀 Starting USITC Export Automation"
log "📁 Working directory: $BASE_DIR"

# Function to get chapter folder name
get_chapter_folder() {
    local chapter=$1
    local chapter_num=$(printf "%02d" $chapter)
    find . -name "Chapter_${chapter_num}_*" -type d | head -1
}

# Function to move downloaded files to appropriate chapter folder
organize_downloaded_files() {
    local chapter=$1
    local chapter_folder=$2
    local temp_dir="/tmp/playwright-mcp-output"
    
    # Look for recently downloaded files
    if [ -d "$temp_dir" ]; then
        # Find the most recent download directory
        local latest_dir=$(find "$temp_dir" -type d -name "*" | sort | tail -1)
        if [ -n "$latest_dir" ]; then
            # Move CSV file
            if [ -f "$latest_dir/htsdata.csv" ]; then
                mv "$latest_dir/htsdata.csv" "$chapter_folder/Chapter_$(printf "%02d" $chapter)_2025_HTS.csv"
                success "CSV file moved to $chapter_folder"
            fi
            
            # Move Excel file
            if [ -f "$latest_dir/htsdata.xlsx" ]; then
                mv "$latest_dir/htsdata.xlsx" "$chapter_folder/Chapter_$(printf "%02d" $chapter)_2025_HTS.xlsx"
                success "Excel file moved to $chapter_folder"
            fi
            
            # Move JSON file
            if [ -f "$latest_dir/htsdata.json" ]; then
                mv "$latest_dir/htsdata.json" "$chapter_folder/Chapter_$(printf "%02d" $chapter)_2025_HTS.json"
                success "JSON file moved to $chapter_folder"
            fi
        fi
    fi
}

# Export chapters 6-97 (we already have 1-5)
log "📊 Starting export for chapters 6-97"

total_chapters=92  # Chapters 6-97
current_chapter=0
start_chapter=6
end_chapter=97

for chapter in $(seq $start_chapter $end_chapter); do
    current_chapter=$((current_chapter + 1))
    progress=$((current_chapter * 100 / total_chapters))
    
    log "📈 Progress: $current_chapter/$total_chapters ($progress%) - Processing Chapter $chapter"
    
    # Get chapter folder
    chapter_folder=$(get_chapter_folder $chapter)
    if [ -z "$chapter_folder" ]; then
        error "Chapter folder not found for Chapter $chapter"
        continue
    fi
    
    # Check if files already exist
    csv_file="$chapter_folder/Chapter_$(printf "%02d" $chapter)_2025_HTS.csv"
    xlsx_file="$chapter_folder/Chapter_$(printf "%02d" $chapter)_2025_HTS.xlsx" 
    json_file="$chapter_folder/Chapter_$(printf "%02d" $chapter)_2025_HTS.json"
    
    if [ -f "$csv_file" ] && [ -f "$xlsx_file" ] && [ -f "$json_file" ]; then
        success "Chapter $chapter already has all 3 export formats - skipping"
        continue
    fi
    
    log "🔄 Chapter $chapter: Downloading missing export formats..."
    
    # Create a simple marker file to track progress
    echo "Processing Chapter $chapter at $(date)" > "$chapter_folder/.export_in_progress"
    
    # Note: The actual browser automation will be done manually or through 
    # the browser MCP tools in the next step
    warning "Chapter $chapter ready for browser automation export"
    
    # Remove progress marker
    rm -f "$chapter_folder/.export_in_progress"
done

log "📋 Export automation preparation complete!"
log "🎯 Ready to execute browser automation for chapters $start_chapter-$end_chapter"

# Summary
log "📊 Summary:"
log "   • Total chapters to process: $total_chapters"
log "   • Chapter range: $start_chapter-$end_chapter"  
log "   • Export formats: CSV, Excel, JSON"
log "   • Expected total files: $((total_chapters * 3)) export files"

success "🎉 Automation script ready for execution!"
