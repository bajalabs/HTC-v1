# Comprehensive USITC Export Plan
## HTS Data Download in CSV, Excel & JSON Formats

### 🔍 **Problem Analysis**
Based on the research document `File Download Location in Docker and Playwright MC.md`, the previous downloads failed to persist because:

1. **Temporary Storage**: Files were downloaded to `/tmp/playwright-artifacts-<random-id>/` inside Docker container
2. **Auto-Cleanup**: Files were automatically deleted when browser context closed
3. **Container Isolation**: Downloads existed only within Docker container filesystem
4. **No Volume Mounting**: No persistent storage was configured

### 🎯 **Objective**
Download all 97 HTS chapters in 3 formats each (CSV, Excel, JSON) from USITC website:
- **Total Files Needed**: 97 chapters × 3 formats = 291 files
- **Source**: https://hts.usitc.gov/ Export functionality
- **Target Location**: Respective chapter folders in HTS directory structure

### 📋 **Technical Strategy**

#### **Method 1: Browser Automation with File Management**
1. **Navigate to USITC**: Load https://hts.usitc.gov/
2. **Click Export Button**: For each chapter (1-97)
3. **Download 3 Formats**: Each Export click downloads CSV, Excel, JSON automatically
4. **Immediate File Handling**: Move files from temp location to permanent folders
5. **Progressive Processing**: Handle one chapter at a time to avoid overwhelming system

#### **Method 2: Direct API Approach** (Backup)
- Use curl/wget with discovered export API endpoints
- Direct download to target folders
- More reliable for batch processing

### 🗂️ **File Organization Structure**
```
HTS/
├── Section_I_Live_Animals_Animal_Products/
│   ├── Chapter_01_Live_Animals/
│   │   ├── Chapter_01_2025_HTS.csv
│   │   ├── Chapter_01_2025_HTS.xlsx
│   │   └── Chapter_01_2025_HTS.json
│   └── Chapter_02_Meat_Meat_Offal/
│       ├── Chapter_02_2025_HTS.csv
│       ├── Chapter_02_2025_HTS.xlsx
│       └── Chapter_02_2025_HTS.json
└── ... (continue for all 97 chapters)
```

### 🔧 **Implementation Workflow**

#### **Phase 1: Setup & Preparation**
1. ✅ Create comprehensive plan (this document)
2. ✅ Verify folder structure exists
3. ✅ Test browser automation connectivity
4. ✅ Confirm USITC website accessibility

#### **Phase 2: Progressive Download (Chapters 1-97)**
**Per Chapter Process:**
1. **Navigate**: Go to https://hts.usitc.gov/
2. **Locate Export Button**: Find chapter-specific Export button
3. **Click Export**: Trigger download of all 3 formats
4. **Monitor Downloads**: Track download completion
5. **Move Files**: Transfer from temp to permanent location with proper naming
6. **Verify**: Confirm all 3 files saved correctly
7. **Next Chapter**: Proceed to next chapter

**Batch Processing:**
- Process 5-10 chapters per batch to avoid overwhelming system
- Add delays between downloads to respect server limits
- Implement error handling and retry logic

#### **Phase 3: Verification & Cleanup**
1. **File Count Verification**: Confirm 291 files downloaded (97 × 3)
2. **File Integrity Check**: Verify files are not corrupted/empty
3. **Naming Consistency**: Ensure proper naming convention
4. **Cleanup**: Remove any temporary files or scripts

### 📊 **Progress Tracking**

#### **Download Status Matrix**
| Chapter | CSV | Excel | JSON | Status |
|---------|-----|-------|------|---------|
| 01 | ⏳ | ⏳ | ⏳ | Pending |
| 02 | ⏳ | ⏳ | ⏳ | Pending |
| ... | ... | ... | ... | ... |
| 97 | ⏳ | ⏳ | ⏳ | Pending |

**Legend:**
- ⏳ Pending
- 🔄 In Progress  
- ✅ Complete
- ❌ Failed

### 🚨 **Risk Mitigation**

#### **Technical Risks**
1. **Server Rate Limiting**: Add delays between requests
2. **Network Timeouts**: Implement retry logic
3. **File Corruption**: Verify file integrity after download
4. **Storage Space**: Monitor disk usage during download

#### **Process Risks**
1. **Browser Context Loss**: Save files immediately after download
2. **Temporary Directory Cleanup**: Move files before context closes
3. **Naming Conflicts**: Use unique naming convention
4. **Incomplete Downloads**: Verify file completeness

### 🔄 **Recovery & Resume**
- **Checkpoint System**: Track completed chapters in progress file
- **Resume Capability**: Skip already downloaded chapters
- **Error Recovery**: Retry failed downloads with exponential backoff
- **Manual Override**: Ability to restart from specific chapter

### 📈 **Success Metrics**
1. **Completion Rate**: 291/291 files downloaded (100%)
2. **File Integrity**: All files > 0 bytes and properly formatted
3. **Proper Organization**: Files in correct chapter folders
4. **Consistent Naming**: All files follow naming convention
5. **No Duplicates**: Each chapter has exactly 3 files

### 🛠️ **Tools & Technologies**
- **Browser Automation**: Playwright MCP via Docker
- **File Management**: Shell commands for moving/organizing
- **Progress Tracking**: Markdown files and todo system
- **Verification**: File system commands and integrity checks

### ⏱️ **Estimated Timeline**
- **Setup**: 5 minutes
- **Per Chapter**: ~30 seconds (including delays)
- **Total Download Time**: ~48 minutes for all 97 chapters
- **Verification**: 10 minutes
- **Total Project Time**: ~1 hour

### 📝 **Implementation Notes**
1. **Start Fresh**: Begin from Chapter 1 since no previous files exist
2. **Progressive Approach**: Handle one chapter at a time for reliability
3. **Immediate File Handling**: Move files as soon as downloaded
4. **Comprehensive Logging**: Track all operations for debugging
5. **User Approval**: Pause for user confirmation at key milestones

---

**Status**: Ready for Implementation ✅  
**Next Step**: Begin Phase 2 - Progressive Download starting with Chapter 1
