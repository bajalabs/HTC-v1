# USITC Export Analysis & Plan

## 🔍 Export Functionality Analysis

Based on the screenshot and scraped content, USITC provides export functionality for each chapter in three formats:
- **CSV** - Comma-separated values
- **Excel** - Microsoft Excel format
- **JSON** - JavaScript Object Notation

## 📋 Export Mechanism

From the scraped content, the export form requires:
1. **Export Format**: CSV/Excel/JSON dropdown selection
2. **HTS Numbers From**: Starting HTS code (e.g., 0201)
3. **HTS Numbers To**: Ending HTS code (e.g., 0299.99.9999)
4. **Include styles**: Checkbox for formatting
5. **Export button**: Triggers download

## 🎯 Chapter HTS Code Ranges

Each chapter has a specific HTS code range:
- Chapter 1: 0101 - 0199.99.9999
- Chapter 2: 0201 - 0299.99.9999
- Chapter 3: 0301 - 0399.99.9999
- ...and so on

## 🔧 Technical Implementation Strategy

### Option 1: Direct API Calls (Failed)
- Attempted: `https://hts.usitc.gov/export?release=currentRelease&format=CSV&from=0201&to=0210.99.9000&styles=true`
- Result: Returns HTML instead of CSV data
- Reason: Likely requires session/authentication or POST request

### Option 2: Browser Automation (Recommended)
Use Puppeteer to:
1. Navigate to USITC homepage
2. Click on chapter "Export" link
3. Fill export form with appropriate parameters
4. Submit form and download file
5. Repeat for all 3 formats (CSV, Excel, JSON)

### Option 3: Session-based API
1. Establish session with USITC
2. Extract necessary tokens/cookies
3. Make authenticated requests to export endpoint

## 📁 File Organization

For each chapter folder, add:
- `Chapter_{N}_data.csv` - CSV export
- `Chapter_{N}_data.xlsx` - Excel export  
- `Chapter_{N}_data.json` - JSON export

## 🚀 Implementation Plan

1. **Test Export Process**: Use Puppeteer to manually test export for one chapter
2. **Automate Single Chapter**: Create script for downloading all 3 formats for one chapter
3. **Batch Processing**: Scale to all 97 chapters
4. **Error Handling**: Handle failed downloads and retries
5. **Verification**: Ensure all files downloaded correctly

## 📊 Expected Output

- **Total Files**: 97 chapters × 3 formats = 291 export files
- **File Types**: CSV, XLSX, JSON
- **Organization**: Files placed in appropriate chapter folders
- **Naming**: Consistent naming convention
