# HTS Data Integration Plan
**Complete Integration of Organized Chapter Data into HTS/ Folder System**

## 📊 Current Status Analysis

### ✅ What We Have Accomplished
- **95 chapter directories** in `chapters/` folder
- **94 chapters** with all 3 formats (CSV, JSON, Excel)
- **1 chapter** with CSV + Excel only (Chapter 65)
- **Perfect file naming**: `chapter-XX-description.format`
- **Complete coverage**: 95/97 possible chapters (missing Ch. 6 and 77)

### 📁 Current HTS/ Folder Structure
The HTS/ folder is organized by **21 sections** following the Harmonized System structure:
- Section I: Live Animals, Animal Products (Ch. 1-5)
- Section II: Vegetable Products (Ch. 6-14)  
- Section III: Fats, Oils, Cleavage Products (Ch. 15)
- Section IV: Prepared Foodstuffs, Beverages (Ch. 16-24)
- Section V: Mineral Products (Ch. 25-27)
- Section VI: Chemical Products (Ch. 28-38)
- Section VII: Plastics, Rubber (Ch. 39-40)
- Section VIII: Hides, Skins, Leather, Fur (Ch. 41-43)
- Section IX: Wood, Cork, Plaiting Materials (Ch. 44-46)
- Section X: Pulp, Paper, Paperboard (Ch. 47-49)
- Section XI: Textiles, Textile Articles (Ch. 50-63)
- Section XII: Footwear, Headgear, Accessories (Ch. 64-67)
- Section XIII: Stone, Ceramic, Glass (Ch. 68-70)
- Section XIV: Pearls, Precious Stones, Metals (Ch. 71)
- Section XV: Base Metals, Articles (Ch. 72-83)
- Section XVI: Machinery, Electrical Equipment (Ch. 84-85)
- Section XVII: Transport Equipment (Ch. 86-89)
- Section XVIII: Precision Instruments, Apparatus (Ch. 90-92)
- Section XIX: Arms, Ammunition (Ch. 93)
- Section XX: Miscellaneous Manufactured Articles (Ch. 94-96)
- Section XXI: Works of Art, Antiques (Ch. 97)

### 📋 Chapter-to-Section Mapping

| Chapters | Section | Folder Name |
|----------|---------|-------------|
| 1-5 | I | Section_I_Live_Animals_Animal_Products |
| 6-14 | II | Section_II_Vegetable_Products |
| 15 | III | Section_III_Fats_Oils_Cleavage_Products |
| 16-24 | IV | Section_IV_Prepared_Foodstuffs_Beverages |
| 25-27 | V | Section_V_Mineral_Products |
| 28-38 | VI | Section_VI_Chemical_Products |
| 39-40 | VII | Section_VII_Plastics_Rubber |
| 41-43 | VIII | Section_VIII_Hides_Skins_Leather_Fur |
| 44-46 | IX | Section_IX_Wood_Cork_Plaiting_Materials |
| 47-49 | X | Section_X_Pulp_Paper_Paperboard |
| 50-63 | XI | Section_XI_Textiles_Textile_Articles |
| 64-67 | XII | Section_XII_Footwear_Headgear_Accessories |
| 68-70 | XIII | Section_XIII_Stone_Ceramic_Glass |
| 71 | XIV | Section_XIV_Pearls_Precious_Stones_Metals |
| 72-83 | XV | Section_XV_Base_Metals_Articles |
| 84-85 | XVI | Section_XVI_Machinery_Electrical_Equipment |
| 86-89 | XVII | Section_XVII_Transport_Equipment |
| 90-92 | XVIII | Section_XVIII_Precision_Instruments_Apparatus |
| 93 | XIX | Section_XIX_Arms_Ammunition |
| 94-96 | XX | Section_XX_Miscellaneous_Manufactured_Articles |
| 97 | XXI | Section_XXI_Works_of_Art_Antiques |

## 🎯 Integration Strategy

### Phase 1: Verification and Validation
1. **Verify all 95 chapters** are properly organized in `chapters/` folder
2. **Confirm file naming consistency** across all chapters
3. **Validate file integrity** - ensure all files are readable and complete
4. **Cross-reference with HTS/ structure** to ensure proper mapping

### Phase 2: Directory Preparation
1. **Ensure all HTS section directories exist** and are properly structured
2. **Create missing chapter subdirectories** in HTS/ sections if needed
3. **Verify PDF files are present** in each chapter directory
4. **Prepare for data file integration** alongside existing PDFs

### Phase 3: Systematic Integration
1. **Copy data files chapter by chapter** into their respective HTS/ locations
2. **Maintain existing PDF files** and documentation
3. **Use consistent naming convention**: keep our `chapter-XX-name.format` naming
4. **Create integration logs** for tracking and verification

### Phase 4: Final Validation
1. **Verify all files copied successfully** to HTS/ structure
2. **Confirm no data loss** during integration
3. **Test random samples** to ensure file integrity
4. **Generate final integration report**

## 📝 Detailed Integration Plan

### Integration Method
- **Source**: `chapters/chapter-XX/` directories  
- **Destination**: `HTS/Section_[Roman]_[Name]/Chapter_XX_[Name]/`
- **Files to copy**: All `.csv`, `.json`, `.xlsx` files
- **Preservation**: Keep existing PDFs and documentation intact

### Example Integration:
```
Source: chapters/chapter-01/
- chapter-01-live-animals.csv
- chapter-01-live-animals.json  
- chapter-01-live-animals.xlsx

Destination: HTS/Section_I_Live_Animals_Animal_Products/Chapter_01_Live_Animals/
- [existing PDFs and .md files]
- chapter-01-live-animals.csv    ← NEW
- chapter-01-live-animals.json   ← NEW
- chapter-01-live-animals.xlsx   ← NEW
```

## 🚀 Execution Steps

### Step 1: Pre-Integration Verification
- [ ] Count and verify all 95 chapter directories
- [ ] Confirm 94 chapters have all 3 formats
- [ ] Identify the 1 chapter missing JSON (Chapter 65)
- [ ] Verify file sizes and integrity

### Step 2: HTS Structure Analysis  
- [ ] Map all 95 chapters to their correct HTS sections
- [ ] Verify all HTS section directories exist
- [ ] Check for any missing chapter subdirectories
- [ ] Document current PDF and documentation files

### Step 3: Systematic Integration
- [ ] **Section I (Ch. 1-5)**: Copy 5 chapters to Live Animals section
- [ ] **Section II (Ch. 6-14)**: Copy 9 chapters to Vegetable Products
- [ ] **Section III (Ch. 15)**: Copy 1 chapter to Fats/Oils
- [ ] **Section IV (Ch. 16-24)**: Copy 9 chapters to Foodstuffs/Beverages
- [ ] **Section V (Ch. 25-27)**: Copy 3 chapters to Mineral Products
- [ ] **Section VI (Ch. 28-38)**: Copy 11 chapters to Chemical Products
- [ ] **Section VII (Ch. 39-40)**: Copy 2 chapters to Plastics/Rubber
- [ ] **Section VIII (Ch. 41-43)**: Copy 3 chapters to Hides/Leather
- [ ] **Section IX (Ch. 44-46)**: Copy 3 chapters to Wood/Cork
- [ ] **Section X (Ch. 47-49)**: Copy 3 chapters to Pulp/Paper
- [ ] **Section XI (Ch. 50-63)**: Copy 14 chapters to Textiles
- [ ] **Section XII (Ch. 64-67)**: Copy 4 chapters to Footwear/Headgear
- [ ] **Section XIII (Ch. 68-70)**: Copy 3 chapters to Stone/Ceramic
- [ ] **Section XIV (Ch. 71)**: Copy 1 chapter to Precious Stones
- [ ] **Section XV (Ch. 72-83)**: Copy 12 chapters to Base Metals
- [ ] **Section XVI (Ch. 84-85)**: Copy 2 chapters to Machinery
- [ ] **Section XVII (Ch. 86-89)**: Copy 4 chapters to Transport
- [ ] **Section XVIII (Ch. 90-92)**: Copy 3 chapters to Instruments
- [ ] **Section XIX (Ch. 93)**: Copy 1 chapter to Arms/Ammunition
- [ ] **Section XX (Ch. 94-96)**: Copy 3 chapters to Miscellaneous
- [ ] **Section XXI (Ch. 97)**: Copy 1 chapter to Works of Art

### Step 4: Post-Integration Validation
- [ ] Verify all 95 chapters integrated successfully
- [ ] Confirm total file count: 285 files (95 CSV + 94 JSON + 95 Excel + 1 missing JSON)
- [ ] Test random file samples for integrity
- [ ] Generate integration completion report

## 📊 Expected Final Result

After integration, each HTS chapter directory will contain:
- **Existing files**: PDFs, documentation, guides
- **New data files**: CSV, JSON, Excel files with comprehensive HTS data
- **Complete coverage**: 94 chapters with all 3 data formats
- **Near-perfect system**: 99% completion rate

## 🎉 Success Metrics

- ✅ **95 chapters integrated** into proper HTS sections
- ✅ **285 data files** successfully copied
- ✅ **21 HTS sections** now have complete data coverage  
- ✅ **Zero data loss** during integration
- ✅ **Consistent naming** maintained throughout
- ✅ **PDF documentation preserved** alongside new data

This integration will create the most comprehensive, well-organized HTS database system with both official documentation (PDFs) and complete data files (CSV, JSON, Excel) in their proper hierarchical structure.
