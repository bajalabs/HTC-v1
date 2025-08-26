#!/bin/bash

# Simple batch download for remaining chapters
set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

log() { echo -e "${BLUE}[$(date +'%H:%M:%S')]${NC} $1"; }
success() { echo -e "${GREEN}✓${NC} $1"; }
error() { echo -e "${RED}✗${NC} $1"; }

# Base directory
BASE_DIR="/Users/ivi/VIBE/RATIOS/HTC/HTC-v1/HTS"
cd "$BASE_DIR"

# Function to download a single chapter's documents
download_chapter() {
    local chapter=$1
    local chapter_num=$(printf "%02d" $chapter)
    
    log "Processing Chapter $chapter"
    
    # Find the chapter folder
    local chapter_folder=$(find . -name "Chapter_${chapter_num}_*" -type d | head -1)
    if [ -z "$chapter_folder" ]; then
        error "Chapter folder not found for Chapter $chapter"
        return 1
    fi
    
    # Download Census file
    local census_file="$chapter_folder/c${chapter_num}.pdf"
    if [ ! -f "$census_file" ]; then
        log "Downloading Census Chapter $chapter..."
        if curl -f -s -o "$census_file" "https://www.census.gov/foreign-trade/schedules/b/2025/c${chapter_num}.pdf"; then
            success "Census Chapter $chapter"
        else
            error "Failed Census Chapter $chapter"
        fi
    fi
    
    # Download WCO file
    local wco_filename=""
    case $chapter in
        6) wco_filename="0206_2022e.pdf" ;;
        7) wco_filename="0207_2022e.pdf" ;;
        8) wco_filename="0208_2022e.pdf" ;;
        9) wco_filename="0209_2022e.pdf" ;;
        10) wco_filename="0210_2022e.pdf" ;;
        11) wco_filename="0211_2022e.pdf" ;;
        12) wco_filename="0212_2022e.pdf" ;;
        13) wco_filename="0213_2022e.pdf" ;;
        14) wco_filename="0214_2022e.pdf" ;;
        15) wco_filename="0315_2022e.pdf" ;;
        16) wco_filename="0416_2022e.pdf" ;;
        17) wco_filename="0417_2022e.pdf" ;;
        18) wco_filename="0418_2022e.pdf" ;;
        19) wco_filename="0419_2022e.pdf" ;;
        20) wco_filename="0420_2022e.pdf" ;;
        21) wco_filename="0421_2022e.pdf" ;;
        22) wco_filename="0422_2022e.pdf" ;;
        23) wco_filename="0423_2022e.pdf" ;;
        24) wco_filename="0424_2022e.pdf" ;;
        25) wco_filename="0525_2022e.pdf" ;;
        26) wco_filename="0526_2022e.pdf" ;;
        27) wco_filename="0527_2022e.pdf" ;;
        28) wco_filename="0628_2022e.pdf" ;;
        29) wco_filename="0629_2022e.pdf" ;;
        30) wco_filename="0630_2022e.pdf" ;;
        31) wco_filename="0631_2022e.pdf" ;;
        32) wco_filename="0632_2022e.pdf" ;;
        33) wco_filename="0633_2022e.pdf" ;;
        34) wco_filename="0634_2022e.pdf" ;;
        35) wco_filename="0635_2022e.pdf" ;;
        36) wco_filename="0636_2022e.pdf" ;;
        37) wco_filename="0637_2022e.pdf" ;;
        38) wco_filename="0638_2022e.pdf" ;;
        39) wco_filename="0739_2022e.pdf" ;;
        40) wco_filename="0740_2022e.pdf" ;;
        41) wco_filename="0841_2022e.pdf" ;;
        42) wco_filename="0842_2022e.pdf" ;;
        43) wco_filename="0843_2022e.pdf" ;;
        44) wco_filename="0944_2022e.pdf" ;;
        45) wco_filename="0945_2022e.pdf" ;;
        46) wco_filename="0946_2022e.pdf" ;;
        47) wco_filename="1047_2022e.pdf" ;;
        48) wco_filename="1048_2022e.pdf" ;;
        49) wco_filename="1049_2022e.pdf" ;;
        50) wco_filename="1150_2022e.pdf" ;;
        *) wco_filename="$(printf "%04d" $chapter)_2022e.pdf" ;;
    esac
    
    local wco_file="$chapter_folder/$wco_filename"
    if [ ! -f "$wco_file" ]; then
        log "Downloading WCO Chapter $chapter..."
        if curl -f -s -o "$wco_file" "https://www.wcoomd.org/-/media/wco/public/global/pdf/topics/nomenclature/instruments-and-tools/hs-nomenclature-2022/2022/$wco_filename"; then
            success "WCO Chapter $chapter"
        else
            error "Failed WCO Chapter $chapter"
        fi
    fi
    
    # Download USITC file
    local usitc_file="$chapter_folder/Chapter ${chapter}_2025HTSRev19.pdf"
    if [ ! -f "$usitc_file" ]; then
        log "Downloading USITC Chapter $chapter..."
        if curl -f -s -o "$usitc_file" "https://hts.usitc.gov/reststop/file?release=currentRelease&filename=Chapter%20${chapter}"; then
            success "USITC Chapter $chapter"
        else
            error "Failed USITC Chapter $chapter"
        fi
    fi
    
    sleep 0.5  # Brief pause to be respectful
}

# Process chapters 7-20 first
log "Starting batch download for chapters 7-20..."
for chapter in {7..20}; do
    download_chapter $chapter
done

log "Batch 1 complete! Check results and run again for more chapters if needed."
