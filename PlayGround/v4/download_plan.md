# HTS Document Download Plan

## Sources Analysis

### 1. WCO (World Customs Organization) - HS Nomenclature 2022
- **Base URL**: https://www.wcoomd.org/-/media/wco/public/global/pdf/topics/nomenclature/instruments-and-tools/hs-nomenclature-2022/2022/
- **Pattern**: `{chapter_code}_2022e.pdf`
- **Example**: `0102_2022e.pdf` for Chapter 2
- **Chapters**: 01-97 (some have different prefixes like 0206 for Ch6, 0315 for Ch15)

### 2. US Census Bureau - Schedule B 2025
- **Base URL**: https://www.census.gov/foreign-trade/schedules/b/2025/
- **Pattern**: `c{NN}.pdf`
- **Example**: `c02.pdf` for Chapter 2
- **Chapters**: 01-98 (straightforward numbering)

### 3. USITC - HTS 2025 Revision 19
- **Base URL**: https://hts.usitc.gov/reststop/file?release=currentRelease&filename=
- **Pattern**: `Chapter%20{N}` (URL encoded)
- **Example**: `Chapter%202` for Chapter 2
- **Chapters**: 1-99 (no leading zeros)

## Chapter Mapping for WCO (Special Cases)

Based on the scraped content, WCO has specific filename patterns:
- Ch01: 0101_2022e.pdf
- Ch02: 0102_2022e.pdf
- Ch03: 0103_2022e.pdf
- Ch04: 0104_2022e.pdf
- Ch05: 0105_2022e.pdf
- Ch06: 0206_2022e.pdf (note the prefix change)
- Ch07: 0207_2022e.pdf
- Ch08: 0208_2022e.pdf
- Ch09: 0209_2022e.pdf
- Ch10: 0210_2022e.pdf
- Ch11: 0211_2022e.pdf
- Ch12: 0212_2022e.pdf
- Ch13: 0213_2022e.pdf
- Ch14: 0214_2022e.pdf
- Ch15: 0315_2022e.pdf (note the prefix change)
- Ch16: 0416_2022e.pdf (note the prefix change)
- And so on...

## Download Tasks

### Completed (Chapters 1-5):
- ✅ Chapter 1: WCO, Census, USITC
- ✅ Chapter 2: WCO, Census, USITC  
- ✅ Chapter 3: WCO, Census, USITC
- ✅ Chapter 4: WCO, Census, USITC
- ✅ Chapter 5: WCO, Census, USITC

### Remaining (Chapters 6-97):
- 🔄 Chapters 6-97: Need to download from all 3 sources
- Total files to download: 92 chapters × 3 sources = 276 files

## File Naming Convention

Each chapter folder will contain:
1. `{chapter_code}_2022e.pdf` (WCO source)
2. `c{NN}.pdf` (Census source) 
3. `Chapter {N}_2025HTSRev19.pdf` (USITC source)

## Automation Approach

1. Use Puppeteer for reliable PDF downloads
2. Batch process by source to avoid rate limiting
3. Implement error handling and retry logic
4. Verify file sizes and successful downloads
5. Organize files into appropriate chapter folders
