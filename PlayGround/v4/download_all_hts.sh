#!/bin/bash

# HTS Document Download Script
# Downloads PDF documents from three HTS sources for chapters 6-97

set -e  # Exit on error

# Base directory
BASE_DIR="/Users/ivi/VIBE/RATIOS/HTC/HTC-v1/HTS"
cd "$BASE_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to get section folder for a chapter
get_section_folder() {
    local chapter=$1
    case $chapter in
        [1-5]) echo "Section_I_Live_Animals_Animal_Products" ;;
        [6-9]|1[0-4]) echo "Section_II_Vegetable_Products" ;;
        15) echo "Section_III_Fats_Oils_Cleavage_Products" ;;
        1[6-9]|2[0-4]) echo "Section_IV_Prepared_Foodstuffs_Beverages" ;;
        2[5-7]) echo "Section_V_Mineral_Products" ;;
        2[8-9]|3[0-8]) echo "Section_VI_Chemical_Products" ;;
        39|40) echo "Section_VII_Plastics_Rubber" ;;
        4[1-3]) echo "Section_VIII_Hides_Skins_Leather_Fur" ;;
        4[4-6]) echo "Section_IX_Wood_Cork_Plaiting_Materials" ;;
        4[7-9]) echo "Section_X_Pulp_Paper_Paperboard" ;;
        5[0-9]|6[0-3]) echo "Section_XI_Textiles_Textile_Articles" ;;
        6[4-7]) echo "Section_XII_Footwear_Headgear_Accessories" ;;
        6[8-9]|70) echo "Section_XIII_Stone_Ceramic_Glass" ;;
        71) echo "Section_XIV_Pearls_Precious_Stones_Metals" ;;
        7[2-9]|8[0-3]) echo "Section_XV_Base_Metals_Articles" ;;
        8[4-5]) echo "Section_XVI_Machinery_Electrical_Equipment" ;;
        8[6-9]) echo "Section_XVII_Transport_Equipment" ;;
        9[0-2]) echo "Section_XVIII_Precision_Instruments_Apparatus" ;;
        93) echo "Section_XIX_Arms_Ammunition" ;;
        9[4-6]) echo "Section_XX_Miscellaneous_Manufactured_Articles" ;;
        97) echo "Section_XXI_Works_of_Art_Antiques" ;;
        *) echo "Unknown_Section" ;;
    esac
}

# Function to get chapter folder name
get_chapter_folder() {
    local chapter=$1
    case $chapter in
        6) echo "Chapter_06_Live_Plants_Cut_Flowers" ;;
        7) echo "Chapter_07_Edible_Vegetables" ;;
        8) echo "Chapter_08_Edible_Fruit_Nuts" ;;
        9) echo "Chapter_09_Coffee_Tea_Spices" ;;
        10) echo "Chapter_10_Cereals" ;;
        11) echo "Chapter_11_Milling_Products_Starches" ;;
        12) echo "Chapter_12_Oil_Seeds_Industrial_Plants" ;;
        13) echo "Chapter_13_Lac_Gums_Plant_Extracts" ;;
        14) echo "Chapter_14_Vegetable_Plaiting_Materials" ;;
        15) echo "Chapter_15_Fats_Oils_Cleavage_Products" ;;
        16) echo "Chapter_16_Prepared_Meat_Fish" ;;
        17) echo "Chapter_17_Sugars_Confectionery" ;;
        18) echo "Chapter_18_Cocoa_Preparations" ;;
        19) echo "Chapter_19_Cereal_Preparations" ;;
        20) echo "Chapter_20_Prepared_Vegetables_Fruit" ;;
        21) echo "Chapter_21_Miscellaneous_Edible_Preparations" ;;
        22) echo "Chapter_22_Beverages_Spirits" ;;
        23) echo "Chapter_23_Food_Industry_Residues_Fodder" ;;
        24) echo "Chapter_24_Tobacco_Substitutes" ;;
        25) echo "Chapter_25_Salt_Sulphur_Stone" ;;
        26) echo "Chapter_26_Ores_Slag_Ash" ;;
        27) echo "Chapter_27_Mineral_Fuels_Oils" ;;
        28) echo "Chapter_28_Inorganic_Chemicals" ;;
        29) echo "Chapter_29_Organic_Chemicals" ;;
        30) echo "Chapter_30_Pharmaceutical_Products" ;;
        31) echo "Chapter_31_Fertilisers" ;;
        32) echo "Chapter_32_Tanning_Extracts_Dyes" ;;
        33) echo "Chapter_33_Essential_Oils_Cosmetics" ;;
        34) echo "Chapter_34_Soap_Cleaning_Preparations" ;;
        35) echo "Chapter_35_Proteins_Starches_Enzymes" ;;
        36) echo "Chapter_36_Explosives_Pyrotechnics" ;;
        37) echo "Chapter_37_Photographic_Goods" ;;
        38) echo "Chapter_38_Miscellaneous_Chemical_Products" ;;
        39) echo "Chapter_39_Plastics_Plastic_Articles" ;;
        40) echo "Chapter_40_Rubber_Rubber_Articles" ;;
        41) echo "Chapter_41_Raw_Hides_Leather" ;;
        42) echo "Chapter_42_Leather_Articles" ;;
        43) echo "Chapter_43_Furskins_Artificial_Fur" ;;
        44) echo "Chapter_44_Wood_Wood_Articles" ;;
        45) echo "Chapter_45_Cork_Cork_Articles" ;;
        46) echo "Chapter_46_Straw_Plaiting_Materials" ;;
        47) echo "Chapter_47_Pulp_Recovered_Paper" ;;
        48) echo "Chapter_48_Paper_Paperboard" ;;
        49) echo "Chapter_49_Printed_Books_Materials" ;;
        50) echo "Chapter_50_Silk" ;;
        51) echo "Chapter_51_Wool_Animal_Hair" ;;
        52) echo "Chapter_52_Cotton" ;;
        53) echo "Chapter_53_Other_Vegetable_Textile_Fibers" ;;
        54) echo "Chapter_54_Man_Made_Filaments" ;;
        55) echo "Chapter_55_Man_Made_Staple_Fibers" ;;
        56) echo "Chapter_56_Wadding_Felt_Nonwovens" ;;
        57) echo "Chapter_57_Carpets_Textile_Floor_Coverings" ;;
        58) echo "Chapter_58_Special_Woven_Fabrics" ;;
        59) echo "Chapter_59_Impregnated_Coated_Textile_Fabrics" ;;
        60) echo "Chapter_60_Knitted_Crocheted_Fabrics" ;;
        61) echo "Chapter_61_Knitted_Crocheted_Apparel" ;;
        62) echo "Chapter_62_Woven_Apparel_Clothing" ;;
        63) echo "Chapter_63_Other_Made_Up_Textile_Articles" ;;
        64) echo "Chapter_64_Footwear" ;;
        65) echo "Chapter_65_Headgear" ;;
        66) echo "Chapter_66_Umbrellas_Walking_Sticks" ;;
        67) echo "Chapter_67_Prepared_Feathers_Artificial_Flowers" ;;
        68) echo "Chapter_68_Stone_Articles" ;;
        69) echo "Chapter_69_Ceramic_Products" ;;
        70) echo "Chapter_70_Glass_Glassware" ;;
        71) echo "Chapter_71_Pearls_Precious_Stones_Metals" ;;
        72) echo "Chapter_72_Iron_Steel" ;;
        73) echo "Chapter_73_Iron_Steel_Articles" ;;
        74) echo "Chapter_74_Copper_Articles" ;;
        75) echo "Chapter_75_Nickel_Articles" ;;
        76) echo "Chapter_76_Aluminum_Articles" ;;
        77) echo "Chapter_77_Reserved" ;;
        78) echo "Chapter_78_Lead_Articles" ;;
        79) echo "Chapter_79_Zinc_Articles" ;;
        80) echo "Chapter_80_Tin_Articles" ;;
        81) echo "Chapter_81_Other_Base_Metals" ;;
        82) echo "Chapter_82_Tools_Cutlery" ;;
        83) echo "Chapter_83_Miscellaneous_Base_Metal_Articles" ;;
        84) echo "Chapter_84_Nuclear_Reactors_Machinery" ;;
        85) echo "Chapter_85_Electrical_Machinery" ;;
        86) echo "Chapter_86_Railway_Locomotives" ;;
        87) echo "Chapter_87_Motor_Vehicles" ;;
        88) echo "Chapter_88_Aircraft_Spacecraft" ;;
        89) echo "Chapter_89_Ships_Boats" ;;
        90) echo "Chapter_90_Optical_Measuring_Instruments" ;;
        91) echo "Chapter_91_Clocks_Watches" ;;
        92) echo "Chapter_92_Musical_Instruments" ;;
        93) echo "Chapter_93_Arms_Ammunition" ;;
        94) echo "Chapter_94_Furniture_Bedding" ;;
        95) echo "Chapter_95_Toys_Games_Sports_Equipment" ;;
        96) echo "Chapter_96_Miscellaneous_Manufactured_Articles" ;;
        97) echo "Chapter_97_Works_of_Art_Antiques" ;;
        *) printf "Chapter_%02d" "$chapter" ;;
    esac
}

# Function to get WCO filename
get_wco_filename() {
    local chapter=$1
    case $chapter in
        1) echo "0101_2022e.pdf" ;;
        2) echo "0102_2022e.pdf" ;;
        3) echo "0103_2022e.pdf" ;;
        4) echo "0104_2022e.pdf" ;;
        5) echo "0105_2022e.pdf" ;;
        6) echo "0206_2022e.pdf" ;;
        7) echo "0207_2022e.pdf" ;;
        8) echo "0208_2022e.pdf" ;;
        9) echo "0209_2022e.pdf" ;;
        10) echo "0210_2022e.pdf" ;;
        11) echo "0211_2022e.pdf" ;;
        12) echo "0212_2022e.pdf" ;;
        13) echo "0213_2022e.pdf" ;;
        14) echo "0214_2022e.pdf" ;;
        15) echo "0315_2022e.pdf" ;;
        16) echo "0416_2022e.pdf" ;;
        17) echo "0417_2022e.pdf" ;;
        18) echo "0418_2022e.pdf" ;;
        19) echo "0419_2022e.pdf" ;;
        20) echo "0420_2022e.pdf" ;;
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

# Function to download a file
download_file() {
    local url=$1
    local target_path=$2
    local source_name=$3
    local chapter=$4
    
    log "Downloading $source_name Chapter $chapter..."
    
    if curl -f -s -o "$target_path" "$url"; then
        # Verify it's a valid PDF
        if file "$target_path" | grep -q "PDF document"; then
            local size=$(ls -lh "$target_path" | awk '{print $5}')
            success "Downloaded $source_name Chapter $chapter ($size)"
            return 0
        else
            error "Invalid PDF: $target_path"
            rm -f "$target_path"
            return 1
        fi
    else
        error "Failed to download $source_name Chapter $chapter from $url"
        return 1
    fi
}

# Main download function
download_chapter() {
    local chapter=$1
    local section_folder=$(get_section_folder $chapter)
    local chapter_folder=$(get_chapter_folder $chapter)
    local target_dir="$section_folder/$chapter_folder"
    
    # Create target directory if it doesn't exist
    mkdir -p "$target_dir"
    
    log "Processing Chapter $chapter in $target_dir"
    
    # Download from Census Bureau (Schedule B)
    local census_filename="c$(printf "%02d" $chapter).pdf"
    local census_url="https://www.census.gov/foreign-trade/schedules/b/2025/$census_filename"
    local census_target="$target_dir/$census_filename"
    
    if [ ! -f "$census_target" ]; then
        download_file "$census_url" "$census_target" "Census" "$chapter"
    else
        warning "Census Chapter $chapter already exists, skipping"
    fi
    
    # Download from WCO
    local wco_filename=$(get_wco_filename $chapter)
    local wco_url="https://www.wcoomd.org/-/media/wco/public/global/pdf/topics/nomenclature/instruments-and-tools/hs-nomenclature-2022/2022/$wco_filename"
    local wco_target="$target_dir/$wco_filename"
    
    if [ ! -f "$wco_target" ]; then
        download_file "$wco_url" "$wco_target" "WCO" "$chapter"
    else
        warning "WCO Chapter $chapter already exists, skipping"
    fi
    
    # Download from USITC
    local usitc_filename="Chapter $chapter"
    local usitc_url="https://hts.usitc.gov/reststop/file?release=currentRelease&filename=$(echo "$usitc_filename" | sed 's/ /%20/g')"
    local usitc_target="$target_dir/Chapter ${chapter}_2025HTSRev19.pdf"
    
    if [ ! -f "$usitc_target" ]; then
        download_file "$usitc_url" "$usitc_target" "USITC" "$chapter"
    else
        warning "USITC Chapter $chapter already exists, skipping"
    fi
    
    # Small delay to be respectful to servers
    sleep 1
}

# Main execution
main() {
    log "Starting HTS document download for chapters 6-97"
    log "Base directory: $BASE_DIR"
    
    local total_chapters=92
    local current=0
    local successful=0
    local failed=0
    
    for chapter in {6..97}; do
        current=$((current + 1))
        log "Progress: $current/$total_chapters (Chapter $chapter)"
        
        if download_chapter $chapter; then
            successful=$((successful + 1))
        else
            failed=$((failed + 1))
        fi
    done
    
    log "Download completed!"
    success "Successfully processed: $successful chapters"
    if [ $failed -gt 0 ]; then
        error "Failed: $failed chapters"
    fi
}

# Run if script is executed directly
if [ "${BASH_SOURCE[0]}" == "${0}" ]; then
    main "$@"
fi
