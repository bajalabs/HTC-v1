# USITC Automated Download Solution

## 🎯 **Problem Identified**
The browser MCP downloads files to temporary Docker directories that get cleaned up automatically. However, according to the research document, Playwright can be configured to download files to a specific directory.

## ✅ **Successful Testing Results**
- Export buttons work perfectly - each click downloads all 3 formats automatically
- Files are named: `htsdata.csv`, `htsdata.xlsx`, `htsdata.json`
- Export dialog shows correct HTS ranges for each chapter
- System is fully functional, just need proper file handling

## 🔧 **Solution Strategy**

### **Option 1: Configure Browser Download Directory**
Use browser MCP with proper download directory configuration to save files directly to chapter folders.

### **Option 2: Post-Processing File Movement**
Continue with current approach but implement immediate file movement after each download.

### **Option 3: Direct API Approach**
Since we understand the export mechanism, create direct API calls to the USITC export endpoint.

## 📋 **Implementation Plan**

1. **Configure Download Directory**: Set up browser MCP to download to specific local directories
2. **Systematic Chapter Processing**: Process chapters 1-97 in sequence
3. **File Organization**: Rename and organize files with proper chapter identification
4. **Verification**: Ensure all files are downloaded and properly named

## 🎯 **Expected Output**
For each chapter folder, we should have:
- `Chapter_XX_Name_2025_HTS.csv`
- `Chapter_XX_Name_2025_HTS.xlsx` 
- `Chapter_XX_Name_2025_HTS.json`

## 📊 **Progress Tracking**
- Chapters 1-5: Already have PDF files, need to add CSV/Excel/JSON
- Chapters 6-97: Need all three formats (CSV/Excel/JSON)
- Total files to download: 97 chapters × 3 formats = 291 files
