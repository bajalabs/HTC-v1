# 🚀 Quick Start Guide

Get up and running with the HTS Database in minutes!

## 📋 Prerequisites

- Python 3.8 or higher
- ~500MB free disk space
- Git (for cloning the repository)

## ⚡ 5-Minute Setup

### 1. Clone and Navigate
```bash
git clone https://github.com/yourusername/hts-database.git
cd hts-database
```

### 2. Quick Data Exploration
```bash
# Browse the chapter data
ls chapters/                    # See all 95 chapters
ls chapters/chapter-01/         # Example: Live animals data

# Check HTS structure
ls HTS/                        # See all 21 sections
ls HTS/Section_I_Live_Animals_Animal_Products/
```

### 3. Database Setup
```bash
cd hts-local-database
pip install -r requirements.txt
python scripts/build_database.py
```

### 4. First Query
```python
from utils.database import HTSDatabase

# Initialize database
db = HTSDatabase()

# Search for products
results = db.search_products("live animals")
for result in results[:5]:
    print(f"{result['hts_code']}: {result['description']}")

# Get chapter information  
chapter_info = db.get_chapter(1)
print(f"Chapter {chapter_info['number']}: {chapter_info['title']}")
```

## 📊 Data Formats Available

### CSV Format
```bash
# View tariff data in spreadsheet format
head chapters/chapter-01/chapter-01-live-animals.csv
```
- Human-readable
- Excel compatible
- Good for analysis

### JSON Format  
```bash
# View structured API data
head chapters/chapter-01/chapter-01-live-animals.json
```
- Programmatic access
- API integration
- Structured queries

### Excel Format
```bash
# Open in Excel or LibreOffice
open chapters/chapter-01/chapter-01-live-animals.xlsx
```
- Business users
- Formatted reports
- Advanced filtering

## 🔍 Common Use Cases

### Find HTS Code for a Product
```python
from utils.database import HTSDatabase
db = HTSDatabase()

# Search by product description
results = db.search_products("leather shoes")
for result in results:
    print(f"HTS: {result['hts_code']} - {result['description']}")
```

### Get All Products in a Chapter
```python
# Get all live animal classifications
chapter_1 = db.get_chapter_products(1)
print(f"Found {len(chapter_1)} classifications in Chapter 1")
```

### Calculate Basic Duty Information
```python
# Get duty rates for a specific HTS code
product = db.get_product_by_hts("0101.21.00")  
if product:
    print(f"General Duty: {product['general_duty']}")
    print(f"Special Duty: {product['special_duty']}")
```

## 🎯 Next Steps

### For Traders & Importers
1. **Classification**: Use search to find correct HTS codes
2. **Documentation**: Extract duty rates and special provisions  
3. **Compliance**: Review general notes and restrictions

### For Developers
1. **Integration**: Connect the SQLite database to your application
2. **API**: Build REST endpoints using the database utilities
3. **Automation**: Create classification workflows with the search functions

### For Researchers
1. **Analysis**: Export data to pandas/Excel for trade analysis
2. **Visualization**: Create charts from the structured data
3. **Studies**: Use comprehensive data for trade policy research

## ❓ Need Help?

- **Issues**: [GitHub Issues](https://github.com/yourusername/hts-database/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/hts-database/discussions)  
- **Documentation**: Check the [docs/](../docs/) folder
- **Examples**: See [docs/examples.md](examples.md)

## 📈 What's Included

- **95 Complete Chapters** with tariff classifications
- **284+ Data Files** in multiple formats
- **SQLite Database** with search capabilities
- **21 HTS Sections** properly organized
- **50,000+ Individual Classifications** ready to query

Ready to start classifying products? 🚢📊