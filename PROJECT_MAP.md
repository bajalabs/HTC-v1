# 🗺️ HTS Database Project Map

*Comprehensive navigation guide for the HTS Database project structure*

**Last Updated**: August 2025  
**Project Status**: Production Ready  
**Total Files**: 1,041 files across organized directory structure

---

## 📊 **Project Overview**

| Component | Count | Description |
|-----------|-------|-------------|
| **CSV Files** | 298 | Structured data files for import/processing |
| **JSON Files** | 387 | API-ready and analysis data formats |
| **Excel Files** | 286 | Business-friendly spreadsheet formats |
| **Markdown Files** | 42 | Documentation and guides |
| **Python Files** | 28 | Scripts, utilities, and database tools |
| **Database Files** | 3 | SQLite database with backups |

---

## 🏗️ **Directory Structure Map**

```
HTC-v1/
├── 📚 BackPack/                    # Documentation & Tools Hub
│   ├── docs/                       # User Documentation
│   ├── templates/                  # Project Templates  
│   └── tools/                      # Utilities & Validators
│
├── 🚪 Door/                        # Primary Data Entry Point
│   ├── chapters/                   # 95 HTS Chapters (Raw Data)
│   ├── json_analysis/              # JSON Analysis Tools
│   └── playwright-mcp-output11/    # Automated Data Collection
│
├── 🗄️ FileCabinet/                 # Reference Documents
│   ├── Videos/                     # Training Materials
│   └── *.pdf                      # Official HTS Documents
│
├── 🏛️ HTS/                         # Official HTS Structure
│   ├── Section_I_Live_Animals_Animal_Products/
│   ├── Section_II_Vegetable_Products/
│   └── ... (21 sections total)
│
├── 🎯 PlayGround/                  # Development & Analysis
│   ├── analysis/                   # Data Analysis Reports
│   ├── scripts/                    # Processing Scripts
│   ├── v1/ v2/ v3/ v4/            # Version Archives
│   └── research/                   # Experimental Features
│
└── 📋 Records/                     # Database System
    └── hts-local-database/         # SQLite Database Engine
        ├── agents/                 # AI Processing Tools
        ├── data/                   # Structured Data Storage
        ├── database/               # SQLite DB & Backups
        ├── scripts/                # Database Management
        └── utils/                  # Core Utilities
```

---

## 📚 **BackPack** - Documentation & Tools Hub

### 📖 **docs/** - User Documentation
| File | Purpose | Status |
|------|---------|---------|
| `quick-start.md` | 5-minute setup guide | ✅ Complete |
| `installation.md` | Detailed installation instructions | ✅ Complete |
| `search-guide.md` | Comprehensive search functionality | ✅ Complete |
| `examples.md` | Practical usage examples | ✅ Complete |

### 🏗️ **templates/** - Project Templates  
| File | Purpose | Usage |
|------|---------|-------|
| `HTS_Chapter_Dashboard_Template_v2.md` | Chapter analysis template | Data visualization |
| `HTS_Chapter_Database_Template.md` | Database integration template | Development |

### 🔧 **tools/** - Development Utilities
| File | Purpose | Function |
|------|---------|----------|
| `data_validator.py` | Data integrity validation | Quality assurance |

---

## 🚪 **Door** - Primary Data Entry Point

### 📂 **chapters/** - Core HTS Data (95 Chapters)
```
Structure: chapter-XX/
├── chapter-XX-description.csv    # Spreadsheet format
├── chapter-XX-description.json   # API/structured format  
└── chapter-XX-description.xlsx   # Business format
```

**Coverage**: Chapters 1-97 (missing 77, 85)
- **Live Animals** (Ch 1-5): Agricultural products and livestock
- **Vegetable Products** (Ch 6-14): Plants, fruits, grains
- **Chemicals** (Ch 28-38): Industrial and pharmaceutical chemicals
- **Textiles** (Ch 50-63): Fabrics and clothing
- **Machinery** (Ch 84, 86-89): Industrial equipment and vehicles
- **And 16+ more sections...**

### 🔍 **json_analysis/** - Data Processing Tools
- `analyze_all_json.py` - JSON data validation scripts
- `json_XX_*.json` - Timestamped analysis results for each chapter

### 🤖 **playwright-mcp-output11/** - Automated Collection
- Timestamped data collection results
- Raw scraping outputs in CSV/JSON/XLSX formats
- **96 directories** with automated collection data

---

## 🗄️ **FileCabinet** - Reference Materials

### 📹 **Videos/**
- `Understand_Your_Product's_Harmonized_System_(HS)_Code_Open Captioned.mp4` - Training material

### 📄 **Documents**
| Document | Source | Purpose |
|----------|--------|---------|
| `finalCopy_2025HTSRev19.pdf` | USITC | Official 2025 HTS revision |
| `hts_external_user_guide.pdf` | USITC | User guidance document |
| `0100_2022e.pdf` | Official | Chapter documentation |
| `WITSAPI_UserGuide (1).pdf` | World Bank | API integration guide |

---

## 🏛️ **HTS** - Official Structure Organization

### 21 HTS Sections (Complete)
| Section | Chapters | Description | Status |
|---------|----------|-------------|--------|
| **I** | 1-5 | Live Animals & Animal Products | ✅ Complete |
| **II** | 6-14 | Vegetable Products | ✅ Complete |
| **III** | 15 | Fats & Oils | ✅ Complete |
| **IV** | 16-24 | Prepared Foodstuffs & Beverages | ✅ Complete |
| **V** | 25-27 | Mineral Products | ✅ Complete |
| **VI** | 28-38 | Chemical Products | ✅ Complete |
| **VII** | 39-40 | Plastics & Rubber | ✅ Complete |
| **VIII** | 41-43 | Hides, Skins & Leather | ✅ Complete |
| **IX** | 44-46 | Wood & Cork Products | ✅ Complete |
| **X** | 47-49 | Pulp & Paper | ✅ Complete |
| **XI** | 50-63 | Textiles & Textile Articles | ✅ Complete |
| **XII** | 64-67 | Footwear & Headgear | ✅ Complete |
| **XIII** | 68-70 | Stone, Ceramics & Glass | ✅ Complete |
| **XIV** | 71 | Precious Stones & Metals | ✅ Complete |
| **XV** | 72-83 | Base Metals & Articles | ✅ Complete |
| **XVI** | 84-85 | Machinery & Electrical | ⚠️ Partial (84 only) |
| **XVII** | 86-89 | Transport Equipment | ✅ Complete |
| **XVIII** | 90-92 | Precision Instruments | ✅ Complete |
| **XIX** | 93 | Arms & Ammunition | ✅ Complete |
| **XX** | 94-96 | Miscellaneous Articles | ✅ Complete |
| **XXI** | 97 | Works of Art & Antiques | ✅ Complete |

Each section contains:
- Chapter directories with PDFs and data files
- Official government documents
- Processed data in multiple formats
- Documentation and dashboards

---

## 🎯 **PlayGround** - Development & Research Hub

### 📊 **analysis/** - Data Analysis Center
| Report | Purpose | Last Updated |
|--------|---------|--------------|
| `analysis_summary.md` | Project overview and statistics | August 2025 |
| `comprehensive_organization_report.md` | Complete structure analysis | August 2025 |
| `final_organization_report.md` | Organization completion status | August 2025 |
| `file_mapping.csv/.json` | File location mappings | August 2025 |

### ⚙️ **scripts/** - Processing Tools
| Script | Function | Status |
|--------|----------|---------|
| `analyze_hts_files.py` | File structure analysis | ✅ Active |
| `complete_organization.py` | Data organization automation | ✅ Active |
| `organize_all_formats.py` | Multi-format file organization | ✅ Active |
| `run_hts_organization.py` | Main organization controller | ✅ Active |

### 📚 **Version Archives (v1-v4)**
- **v1/**: Initial development prompts and schemas
- **v2/**: Docker and Playwright integration
- **v3/**: File analysis and migration systems  
- **v4/**: USITC automation and download tools

---

## 📋 **Records** - Database Engine

### 🗃️ **hts-local-database/** - SQLite System

#### 🤖 **agents/** - AI Processing
- `base_agent.py` - Core AI agent functionality
- `prompts/sections_prompt.txt` - AI processing templates

#### 📊 **data/** - Structured Storage
```
data/
├── cache/                     # Processing cache
├── csv/core/                 # Core data tables
│   ├── chapters.csv          # Chapter metadata
│   ├── headings.csv          # HTS headings
│   ├── products.csv          # Product classifications  
│   ├── sections.csv          # Section information
│   └── subheadings.csv       # Detailed classifications
├── countries/                # Country-specific data
├── enhanced/                 # Enhanced datasets
└── manifest.json            # Data catalog
```

#### 🗄️ **database/** - SQLite Engine
| File | Purpose | Size |
|------|---------|------|
| `hts.db` | Main SQLite database | ~25MB |
| `hts.db-shm` | Shared memory file | Active |
| `hts.db-wal` | Write-ahead log | Active |

**Backups**:
- `hts_backup_1756111432.db` - Automated backup
- `hts_v1_backup_20250825_014047.db` - Version 1 backup

#### 🛠️ **scripts/** - Database Management
| Script | Function | Purpose |
|--------|----------|---------|
| `build_database.py` | Main database builder | Core system |
| `build_database_v2.py` | Enhanced database system | Version 2 |
| `populate_*.py` | Data population scripts | Individual components |
| `migrate_to_v2.py` | Version migration | Upgrades |

#### ⚙️ **utils/** - Core Utilities
| Utility | Function | Usage |
|---------|----------|-------|
| `database.py` | Database connection and queries | Core operations |
| `product_manager.py` | Product classification management | Business logic |
| `validation_engine.py` | Data quality validation | Quality assurance |

---

## 🛠️ **Root Level Files**

### 📄 **Project Management**
| File | Purpose | Status |
|------|---------|---------|
| `README.md` | Main project documentation | ✅ Complete |
| `LICENSE` | MIT License | ✅ Complete |
| `CONTRIBUTING.md` | Contribution guidelines | ✅ Complete |
| `setup.py` | Automated setup script | ✅ Complete |
| `Makefile` | Development commands | ✅ Complete |
| `PROJECT_MAP.md` | This navigation guide | ✅ Complete |

### ⚙️ **Configuration**
| File | Purpose | Usage |
|------|---------|-------|
| `CLAUDE.md` | Claude Code configuration | AI assistant |
| `AGENT.md` | Agent configuration | AI processing |
| `.gitignore` | Git exclusions | Version control |

---

## 🎯 **Quick Navigation Guide**

### 🔍 **Looking for Data?**
- **Raw Chapter Data**: `Door/chapters/chapter-XX/`
- **Official HTS Structure**: `HTS/Section_XX_*/Chapter_XX_*/`
- **Database**: `Records/hts-local-database/database/hts.db`

### 📚 **Need Documentation?**
- **User Guides**: `BackPack/docs/`
- **Analysis Reports**: `PlayGround/analysis/`
- **Database Docs**: `Records/hts-local-database/README_v2.md`

### 🛠️ **Want to Develop?**
- **Tools**: `BackPack/tools/`
- **Scripts**: `PlayGround/scripts/`
- **Database Utils**: `Records/hts-local-database/utils/`

### 📋 **Project Management?**
- **Setup**: Run `python setup.py` or `make setup`
- **Validation**: `python BackPack/tools/data_validator.py`
- **Commands**: See `Makefile` for all available commands

---

## 📈 **Project Statistics**

### 📊 **Data Coverage**
- **HTS Chapters**: 95/97 (98% complete)
- **HTS Sections**: 21/21 (100% complete)
- **Data Files**: 1,000+ files across multiple formats
- **Database Records**: 135+ core classifications with search index

### 🔢 **File Distribution**
- **Primary Data**: 284 chapter files (CSV/JSON/XLSX)
- **HTS Organization**: 200+ files in sectional structure
- **Analysis Data**: 300+ timestamped analysis files
- **Documentation**: 42 markdown files
- **Scripts & Tools**: 28 Python utilities

### 💾 **Storage Information**
- **Total Project Size**: ~500MB
- **Database Size**: ~25MB (SQLite with indexes)
- **Raw Data**: ~150MB (CSV/JSON/XLSX files)
- **Documentation**: ~5MB (guides and templates)

---

## 🚀 **Getting Started Paths**

### 👤 **New Users**
1. Read `README.md` for project overview
2. Follow `BackPack/docs/quick-start.md` for 5-minute setup
3. Try examples in `BackPack/docs/examples.md`

### 👨‍💻 **Developers**
1. Run `python setup.py` for automated setup
2. Explore `Records/hts-local-database/` for database system
3. Check `PlayGround/scripts/` for processing tools
4. Read `CONTRIBUTING.md` for development guidelines

### 📊 **Data Analysts**
1. Access data through `Door/chapters/` for raw files
2. Use `Records/hts-local-database/` for structured queries
3. Review `PlayGround/analysis/` for existing analysis
4. Reference `HTS/` for official classifications

### 🏢 **Business Users**
1. Start with `BackPack/docs/installation.md`
2. Use Excel files in `Door/chapters/chapter-XX/`
3. Reference `FileCabinet/` for official documents
4. Follow search guide in `BackPack/docs/search-guide.md`

---

## 🔄 **Maintenance Notes**

### ✅ **Completed**
- ✅ Complete project restructuring and organization
- ✅ Professional documentation system
- ✅ Automated setup and validation tools
- ✅ Database system with search capabilities
- ✅ Multi-format data availability (CSV/JSON/XLSX)

### 🔜 **Future Enhancements**
- 🔜 Complete Chapter 77 and 85 data collection
- 🔜 Web interface development
- 🔜 REST API implementation
- 🔜 Advanced AI classification features
- 🔜 Real-time duty rate integration

### 📋 **Regular Maintenance**
- Monthly validation runs using `BackPack/tools/data_validator.py`
- Quarterly database backups (automated)
- Annual HTS revision updates from USITC
- Continuous integration testing (planned)

---

*This project map is automatically updated with project changes. Last comprehensive review: August 2025*

**🎉 Ready to explore? Start with the README.md or jump directly to your area of interest!**