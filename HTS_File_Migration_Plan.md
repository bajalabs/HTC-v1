# HTS File Migration Plan

## Overview
This plan outlines the systematic migration of chapter files from the `/chapters/` directory to their corresponding locations in the `/HTS/` directory structure.

## Current Status Analysis

### Source Directory (`/chapters/`)
- **Total Files**: 284 files across 95 chapter directories
- **File Types Per Chapter**: 3 files (CSV, JSON, XLSX)
- **Coverage**: Chapters 1-97 (missing chapters 77, 85)
- **Pattern**: `chapter-XX-description.{csv,json,xlsx}`

### Destination Directory (`/HTS/`)
- **Current Chapter Files**: 174 files (58 CSV, 58 JSON, 58 XLSX)
- **Structure**: Organized by Sections > Chapters
- **Missing Coverage**: 37 chapters need file migration
- **Existing Files**: Some chapters already have the required files

## Migration Strategy

### Phase 1: Gap Analysis
- Identify which of the 95 chapters in `/chapters/` are missing files in `/HTS/`
- Create mapping between chapter numbers and HTS section/chapter paths
- Verify file integrity and consistency

### Phase 2: File Mapping
Create precise mapping for each chapter:
```
Chapter 01: /chapters/chapter-01/ → /HTS/Section_I_Live_Animals_Animal_Products/Chapter_01_Live_Animals/
Chapter 02: /chapters/chapter-02/ → /HTS/Section_I_Live_Animals_Animal_Products/Chapter_02_Meat_Meat_Offal/
Chapter 03: /chapters/chapter-03/ → /HTS/Section_I_Live_Animals_Animal_Products/Chapter_03_Fish_Aquatic_Invertebrates/
...and so on for all 95 chapters
```

### Phase 3: Pre-Migration Validation
- Verify all destination directories exist
- Check for existing files to avoid overwrites
- Validate file formats and content consistency
- Create backup plan for existing files

### Phase 4: Systematic Migration
Execute migration in batches by HTS Section:

1. **Section I**: Live Animals & Animal Products (Chapters 1-5)
2. **Section II**: Vegetable Products (Chapters 6-14) 
3. **Section III**: Fats & Oils (Chapter 15)
4. **Section IV**: Prepared Foodstuffs (Chapters 16-24)
5. **Section V**: Mineral Products (Chapters 25-27)
6. **Section VI**: Chemical Products (Chapters 28-38)
7. **Section VII**: Plastics & Rubber (Chapters 39-40)
8. **Section VIII**: Hides & Leather (Chapters 41-43)
9. **Section IX**: Wood & Cork (Chapters 44-46)
10. **Section X**: Pulp & Paper (Chapters 47-49)
11. **Section XI**: Textiles (Chapters 50-63)
12. **Section XII**: Footwear & Headgear (Chapters 64-67)
13. **Section XIII**: Stone & Ceramics (Chapters 68-70)
14. **Section XIV**: Precious Metals (Chapter 71)
15. **Section XV**: Base Metals (Chapters 72-83)
16. **Section XVI**: Machinery & Electrical (Chapters 84-85)
17. **Section XVII**: Transport Equipment (Chapters 86-89)
18. **Section XVIII**: Precision Instruments (Chapters 90-92)
19. **Section XIX**: Arms & Ammunition (Chapter 93)
20. **Section XX**: Miscellaneous Manufactured Articles (Chapters 94-96)
21. **Section XXI**: Works of Art (Chapter 97)

### Phase 5: Post-Migration Verification
- Verify all files copied successfully
- Check file integrity and sizes match
- Validate no data corruption occurred
- Generate migration report

## File Operations

### For Each Chapter:
1. **Copy** (not move) files to preserve originals
2. **Maintain** original filenames
3. **Preserve** file permissions and timestamps
4. **Log** each operation for audit trail

### File Types to Migrate:
- `chapter-XX-description.csv`
- `chapter-XX-description.json` 
- `chapter-XX-description.xlsx`

## Risk Mitigation

### Existing File Conflicts
- Strategy: Compare file sizes and modification dates
- If files identical: Skip copy
- If files different: Create backup of existing file before overwrite
- Log all conflict resolutions

### Data Integrity
- Pre-migration: Calculate checksums for all source files
- Post-migration: Verify checksums match
- Rollback plan: Restore from backups if needed

### Missing Destinations
- Some HTS chapter directories may not exist yet
- Plan includes creating missing directory structure
- Follow existing naming conventions

## Expected Outcomes

### Files to Process
- **Total Source Files**: 284 files
- **Estimated New Copies**: ~110 files (37 missing chapters × 3 files)
- **Conflicts to Resolve**: ~58 existing files to verify/update

### Directory Structure Impact
- No structural changes to existing HTS organization
- All files placed in appropriate chapter subdirectories
- Maintains consistency with existing file patterns

## Success Criteria
- All 95 chapters have their 3 data files in corresponding HTS locations
- No data loss or corruption
- Complete audit trail of all operations
- Existing file conflicts properly resolved
- HTS directory maintains organizational integrity

## Approval Required
This plan requires approval before execution. Upon approval, migration will proceed systematically with detailed logging and verification at each step.