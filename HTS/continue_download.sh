#!/bin/bash

# Continue downloading remaining chapters in batches
set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() { echo -e "${BLUE}[$(date +'%H:%M:%S')]${NC} $1"; }
success() { echo -e "${GREEN}✓${NC} $1"; }
error() { echo -e "${RED}✗${NC} $1"; }
warning() { echo -e "${YELLOW}⚠${NC} $1"; }

# Base directory
BASE_DIR="/Users/ivi/VIBE/RATIOS/HTC/HTC-v1/HTS"
cd "$BASE_DIR"

# WCO filename mapping for chapters 21+
get_wco_filename() {
    local chapter=$1
    case $chapter in
        21) echo "0421_2022e.pdf" ;;
        22) echo "0422_2022e.pdf" ;;
        23) echo "0423_2022e.pdf" ;;
        24) echo "0424_2022e.pdf" ;;
        25) echo "0525_2022e.pdf" ;;
        26) echo "0526_2022e.pdf" ;;
        27) echo "0527_2022e.pdf" ;;
        28) echo "0628_2022e.pdf" ;;
        29) echo "0629_2022e.pdf" ;;
        30) echo "0630_2022e.pdf" ;;
        31) echo "0631_2022e.pdf" ;;
        32) echo "0632_2022e.pdf" ;;
        33) echo "0633_2022e.pdf" ;;
        34) echo "0634_2022e.pdf" ;;
        35) echo "0635_2022e.pdf" ;;
        36) echo "0636_2022e.pdf" ;;
        37) echo "0637_2022e.pdf" ;;
        38) echo "0638_2022e.pdf" ;;
        39) echo "0739_2022e.pdf" ;;
        40) echo "0740_2022e.pdf" ;;
        41) echo "0841_2022e.pdf" ;;
        42) echo "0842_2022e.pdf" ;;
        43) echo "0843_2022e.pdf" ;;
        44) echo "0944_2022e.pdf" ;;
        45) echo "0945_2022e.pdf" ;;
        46) echo "0946_2022e.pdf" ;;
        47) echo "1047_2022e.pdf" ;;
        48) echo "1048_2022e.pdf" ;;
        49) echo "1049_2022e.pdf" ;;
        50) echo "1150_2022e.pdf" ;;
        51) echo "1151_2022e.pdf" ;;
        52) echo "1152_2022e.pdf" ;;
        53) echo "1153_2022e.pdf" ;;
        54) echo "1154_2022e.pdf" ;;
        55) echo "1155_2022e.pdf" ;;
        56) echo "1156_2022e.pdf" ;;
        57) echo "1157_2022e.pdf" ;;
        58) echo "1158_2022e.pdf" ;;
        59) echo "1159_2022e.pdf" ;;
        60) echo "1160_2022e.pdf" ;;
        61) echo "1161_2022e.pdf" ;;
        62) echo "1162_2022e.pdf" ;;
        63) echo "1163_2022e.pdf" ;;
        64) echo "1264_2022e.pdf" ;;
        65) echo "1265_2022e.pdf" ;;
        66) echo "1266_2022e.pdf" ;;
        67) echo "1267_2022e.pdf" ;;
        68) echo "1368_2022e.pdf" ;;
        69) echo "1369_2022e.pdf" ;;
        70) echo "1370_2022e.pdf" ;;
        71) echo "1471_2022e.pdf" ;;
        72) echo "1572_2022e.pdf" ;;
        73) echo "1573_2022e.pdf" ;;
        74) echo "1574_2022e.pdf" ;;
        75) echo "1575_2022e.pdf" ;;
        76) echo "1576_2022e.pdf" ;;
        77) echo "1577_2022e.pdf" ;;
        78) echo "1578_2022e.pdf" ;;
        79) echo "1579_2022e.pdf" ;;
        80) echo "1580_2022e.pdf" ;;
        81) echo "1581_2022e.pdf" ;;
        82) echo "1582_2022e.pdf" ;;
        83) echo "1583_2022e.pdf" ;;
        84) echo "1684_2022e.pdf" ;;
        85) echo "1685_2022e.pdf" ;;
        86) echo "1786_2022e.pdf" ;;
        87) echo "1787_2022e.pdf" ;;
        88) echo "1788_2022e.pdf" ;;
        89) echo "1789_2022e.pdf" ;;
        90) echo "1890_2022e.pdf" ;;
        91) echo "1891_2022e.pdf" ;;
        92) echo "1892_2022e.pdf" ;;
        93) echo "1993_2022e.pdf" ;;
        94) echo "2094_2022e.pdf" ;;
        95) echo "2095_2022e.pdf" ;;
        96) echo "2096_2022e.pdf" ;;
        97) echo "2197_2022e.pdf" ;;
        *) printf "%04d_2022e.pdf" "$chapter" ;;
    esac
}

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
    
    local downloaded=0
    
    # Download Census file
    local census_file="$chapter_folder/c${chapter_num}.pdf"
    if [ ! -f "$census_file" ]; then
        if curl -f -s -o "$census_file" "https://www.census.gov/foreign-trade/schedules/b/2025/c${chapter_num}.pdf"; then
            success "Census Chapter $chapter"
            downloaded=$((downloaded + 1))
        else
            error "Failed Census Chapter $chapter"
        fi
    fi
    
    # Download WCO file
    local wco_filename=$(get_wco_filename $chapter)
    local wco_file="$chapter_folder/$wco_filename"
    if [ ! -f "$wco_file" ]; then
        if curl -f -s -o "$wco_file" "https://www.wcoomd.org/-/media/wco/public/global/pdf/topics/nomenclature/instruments-and-tools/hs-nomenclature-2022/2022/$wco_filename"; then
            success "WCO Chapter $chapter"
            downloaded=$((downloaded + 1))
        else
            error "Failed WCO Chapter $chapter"
        fi
    fi
    
    # Download USITC file
    local usitc_file="$chapter_folder/Chapter ${chapter}_2025HTSRev19.pdf"
    if [ ! -f "$usitc_file" ]; then
        if curl -f -s -o "$usitc_file" "https://hts.usitc.gov/reststop/file?release=currentRelease&filename=Chapter%20${chapter}"; then
            success "USITC Chapter $chapter"
            downloaded=$((downloaded + 1))
        else
            error "Failed USITC Chapter $chapter"
        fi
    fi
    
    if [ $downloaded -eq 0 ]; then
        warning "Chapter $chapter already complete"
    fi
    
    sleep 0.3  # Brief pause
}

# Get batch range from command line arguments
BATCH_START=${1:-21}
BATCH_END=${2:-40}

log "Starting download for chapters $BATCH_START-$BATCH_END..."

for chapter in $(seq $BATCH_START $BATCH_END); do
    download_chapter $chapter
done

log "Batch complete! Downloaded chapters $BATCH_START-$BATCH_END"

# Show current progress
total_pdfs=$(find . -name "*.pdf" -type f | wc -l | tr -d ' ')
log "Total PDFs downloaded: $total_pdfs"
