# 📥 Installation Guide

Complete installation instructions for the HTS Database system.

## 🖥️ System Requirements

### Minimum Requirements
- **OS**: Windows 10, macOS 10.15, or Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher
- **Memory**: 2GB RAM
- **Storage**: 1GB free space
- **Internet**: For initial data download (optional for local use)

### Recommended Requirements
- **Python**: 3.9 or higher
- **Memory**: 4GB RAM or more
- **Storage**: 2GB free space (for future expansions)
- **SSD**: For faster database queries

## 🔧 Installation Methods

### Method 1: Git Clone (Recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/hts-database.git
cd hts-database

# Verify contents
ls -la
# You should see: README.md, chapters/, HTS/, hts-local-database/, etc.
```

### Method 2: Download ZIP
1. Go to [GitHub repository](https://github.com/yourusername/hts-database)
2. Click "Code" → "Download ZIP"
3. Extract to your desired location
4. Open terminal/command prompt in extracted folder

## 🐍 Python Environment Setup

### Option A: Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv hts-env

# Activate virtual environment
# On Windows:
hts-env\\Scripts\\activate
# On macOS/Linux:
source hts-env/bin/activate

# Install dependencies
cd hts-local-database
pip install -r requirements.txt
```

### Option B: System-wide Installation
```bash
cd hts-local-database
pip install -r requirements.txt
```

### Option C: Conda Environment
```bash
conda create -n hts-env python=3.9
conda activate hts-env
cd hts-local-database
pip install -r requirements.txt
```

## 🗃️ Database Setup

### Initial Database Build
```bash
cd hts-local-database
python scripts/build_database.py
```

Expected output:
```
Building HTS Database...
✅ Created database schema
✅ Populated sections (21 entries)
✅ Populated chapters (52 entries)  
✅ Populated headings (58 entries)
✅ Built search index
✅ Database ready at: database/hts.db
```

### Verify Installation
```python
# Test the database connection
python -c "
from utils.database import HTSDatabase
db = HTSDatabase()
print('✅ Database connection successful')
print(f'📊 Sections available: {len(db.get_all_sections())}')
print(f'📋 Chapters available: {len(db.get_all_chapters())}')
"
```

## 📊 Data Verification

### Check Data Completeness
```bash
# Count data files
find chapters/ -name "*.csv" | wc -l    # Should show 95
find chapters/ -name "*.json" | wc -l   # Should show 94  
find chapters/ -name "*.xlsx" | wc -l   # Should show 95

# Check database size
ls -lh hts-local-database/database/hts.db  # Should be ~25MB
```

### Sample Data Query
```python
from utils.database import HTSDatabase
db = HTSDatabase()

# Test search functionality
results = db.search_products("live animals")
print(f"Found {len(results)} results for 'live animals'")
for result in results[:3]:
    print(f"  {result['hts_code']}: {result['description']}")
```

## 🛠️ Troubleshooting

### Common Issues

#### Issue: "ModuleNotFoundError: No module named 'utils'"
**Solution**: Make sure you're in the correct directory
```bash
cd hts-local-database  # Make sure you're in this folder
python scripts/build_database.py
```

#### Issue: "sqlite3.OperationalError: no such table"
**Solution**: Rebuild the database
```bash
rm database/hts.db  # Remove existing database
python scripts/build_database.py  # Rebuild
```

#### Issue: "Permission denied" on database file
**Solution**: Check file permissions
```bash
# On Unix systems:
chmod 644 database/hts.db

# On Windows: Right-click → Properties → Security → Edit permissions
```

#### Issue: "Empty search results"
**Solution**: Check if search index is built
```python
from utils.database import HTSDatabase
db = HTSDatabase()
db.rebuild_search_index()  # Rebuild search index
```

### Performance Issues

#### Slow Queries
```python
# Enable WAL mode for better performance
from utils.database import HTSDatabase
db = HTSDatabase()
db.connection.execute("PRAGMA journal_mode=WAL")
db.connection.execute("PRAGMA synchronous=NORMAL")
```

#### Large Memory Usage
```python
# Use connection pooling for production
import sqlite3
conn = sqlite3.connect('database/hts.db')
conn.execute("PRAGMA cache_size=-64000")  # Use 64MB cache
```

## 📱 Platform-Specific Notes

### Windows
- Use Command Prompt or PowerShell
- Paths use backslashes (`\`)
- May need to install Microsoft C++ Build Tools for some packages

### macOS
- Ensure Xcode Command Line Tools are installed: `xcode-select --install`
- May need to upgrade Python: `brew install python@3.9`

### Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt update
sudo apt install python3-dev python3-pip sqlite3

# For CentOS/RHEL
sudo yum install python3-devel python3-pip sqlite3
```

## 🔄 Updates and Maintenance

### Updating the Database
```bash
# Pull latest changes
git pull origin main

# Rebuild database with new data
cd hts-local-database
python scripts/build_database.py --update
```

### Backup Your Database
```bash
# Create backup
cp database/hts.db database/hts_backup_$(date +%Y%m%d).db

# Or use SQLite backup
sqlite3 database/hts.db ".backup database/hts_backup.db"
```

### Clean Installation
```bash
# Remove all generated files
rm -rf database/hts.db*
rm -rf __pycache__/
rm -rf utils/__pycache__/

# Rebuild everything
python scripts/build_database.py
```

## 🧪 Development Installation

### For Contributors
```bash
# Clone with development dependencies
git clone https://github.com/yourusername/hts-database.git
cd hts-database

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/
```

### IDE Setup

#### VS Code
Install recommended extensions:
- Python
- SQLite Viewer
- Markdown All in One

#### PyCharm
1. Open project folder
2. Configure Python interpreter to use virtual environment
3. Add `hts-local-database` as content root

## ✅ Verification Checklist

After installation, verify these work:

- [ ] Database connection successful
- [ ] Search functionality returns results
- [ ] All 21 sections accessible
- [ ] Chapter data loads correctly
- [ ] CSV/JSON/Excel files readable
- [ ] No error messages in Python console

## 📞 Getting Help

### If Installation Fails:

1. **Check Prerequisites**: Ensure Python 3.8+ is installed
2. **Review Error Messages**: Note specific error messages
3. **Check Permissions**: Ensure write access to installation directory
4. **Try Alternative Method**: Use different installation method
5. **Seek Help**: Create issue on GitHub with error details

### Resources:
- **GitHub Issues**: [Report problems](https://github.com/yourusername/hts-database/issues)
- **Discussions**: [Ask questions](https://github.com/yourusername/hts-database/discussions)
- **Documentation**: See other files in [docs/](.) folder

---

🎉 **Congratulations!** You're ready to start using the HTS Database. 

Next steps:
- 📖 Read the [Quick Start Guide](quick-start.md)
- 💡 Try the [Usage Examples](examples.md)
- 🔍 Learn about [Search Features](search-guide.md)