# HTS Database Project Makefile
# Provides common commands for development and maintenance

.PHONY: help setup install clean test validate build-db backup restore lint docs

# Default target
help:
	@echo "🚢 HTS Database Project Commands"
	@echo "================================"
	@echo ""
	@echo "Setup and Installation:"
	@echo "  make setup        - Complete project setup"
	@echo "  make install      - Install Python dependencies"
	@echo "  make build-db     - Build/rebuild the SQLite database"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean        - Clean up temporary files"
	@echo "  make validate     - Validate data integrity"
	@echo "  make backup       - Backup database"
	@echo "  make test         - Run tests (when available)"
	@echo ""
	@echo "Development:"
	@echo "  make lint         - Run code formatting and linting"
	@echo "  make docs         - Generate/update documentation"
	@echo "  make stats        - Show project statistics"
	@echo ""
	@echo "Data Management:"
	@echo "  make count-files  - Count data files by type"
	@echo "  make check-missing - Check for missing chapter data"
	@echo ""

# Setup and Installation
setup:
	@echo "🚀 Setting up HTS Database..."
	python3 setup.py

install:
	@echo "📦 Installing dependencies..."
	cd hts-local-database && pip install -r requirements.txt
	@echo "✅ Dependencies installed"

build-db:
	@echo "🗄️ Building database..."
	cd hts-local-database && python scripts/build_database.py
	@echo "✅ Database built successfully"

# Maintenance
clean:
	@echo "🧹 Cleaning up..."
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name "*.pyo" -delete 2>/dev/null || true
	find . -name ".DS_Store" -delete 2>/dev/null || true
	find . -name "*.tmp" -delete 2>/dev/null || true
	rm -f migration_log*.txt
	@echo "✅ Cleanup completed"

validate:
	@echo "🔍 Validating data integrity..."
	python3 tools/data_validator.py

backup:
	@echo "💾 Creating database backup..."
	@mkdir -p backups
	@cp hts-local-database/database/hts.db backups/hts_backup_$(shell date +%Y%m%d_%H%M%S).db
	@echo "✅ Backup created in backups/ directory"

test:
	@echo "🧪 Running tests..."
	@if [ -d "tests" ]; then \
		python -m pytest tests/ -v; \
	else \
		echo "⚠️ No tests directory found. Creating sample test..."; \
		mkdir -p tests; \
		echo "# TODO: Add tests" > tests/test_database.py; \
	fi

# Development
lint:
	@echo "🔧 Running code formatting..."
	@if command -v black >/dev/null 2>&1; then \
		black hts-local-database/ --line-length 88; \
		echo "✅ Code formatted with black"; \
	else \
		echo "⚠️ black not installed. Run: pip install black"; \
	fi
	@if command -v flake8 >/dev/null 2>&1; then \
		flake8 hts-local-database/ --max-line-length=88; \
		echo "✅ Code linted with flake8"; \
	else \
		echo "⚠️ flake8 not installed. Run: pip install flake8"; \
	fi

docs:
	@echo "📚 Checking documentation..."
	@echo "Documentation files:"
	@find docs/ -name "*.md" -exec basename {} \; | sort
	@echo "✅ Documentation check completed"

stats:
	@echo "📊 Project Statistics"
	@echo "===================="
	@echo "Chapters: $$(find chapters/ -name 'chapter-*' -type d | wc -l | tr -d ' ')"
	@echo "CSV files: $$(find chapters/ -name '*.csv' | wc -l | tr -d ' ')"
	@echo "JSON files: $$(find chapters/ -name '*.json' | wc -l | tr -d ' ')"
	@echo "XLSX files: $$(find chapters/ -name '*.xlsx' | wc -l | tr -d ' ')"
	@echo "HTS sections: $$(find HTS/ -name 'Section_*' -type d | wc -l | tr -d ' ')"
	@if [ -f "hts-local-database/database/hts.db" ]; then \
		echo "Database size: $$(du -h hts-local-database/database/hts.db | cut -f1)"; \
	else \
		echo "Database: Not built"; \
	fi
	@echo "Python files: $$(find . -name '*.py' | wc -l | tr -d ' ')"
	@echo "Documentation files: $$(find docs/ -name '*.md' | wc -l | tr -d ' ')"

# Data Management  
count-files:
	@echo "📊 File Counts by Type"
	@echo "====================="
	@find chapters/ -name "*.csv" | wc -l | xargs echo "CSV files:"
	@find chapters/ -name "*.json" | wc -l | xargs echo "JSON files:"
	@find chapters/ -name "*.xlsx" | wc -l | xargs echo "XLSX files:"
	@find HTS/ -name "chapter-*.csv" | wc -l | xargs echo "CSV in HTS:"
	@find HTS/ -name "chapter-*.json" | wc -l | xargs echo "JSON in HTS:"
	@find HTS/ -name "chapter-*.xlsx" | wc -l | xargs echo "XLSX in HTS:"

check-missing:
	@echo "🔍 Checking for missing chapter data..."
	@for i in $$(seq -f "%02g" 1 97); do \
		if [ ! -d "chapters/chapter-$$i" ]; then \
			echo "❌ Missing: chapter-$$i"; \
		fi; \
	done
	@echo "✅ Missing chapter check completed"

# Quick development workflow
dev: clean install build-db validate
	@echo "🎉 Development environment ready!"

# Production preparation
prod: clean install build-db validate backup
	@echo "🚀 Production environment ready!"

# Database operations
reset-db:
	@echo "⚠️  Resetting database..."
	@rm -f hts-local-database/database/hts.db*
	@make build-db

# Git operations (optional)
git-status:
	@echo "📋 Git Status Summary"
	@echo "===================="
	@git status --porcelain | wc -l | xargs echo "Modified files:"
	@git ls-files --others --exclude-standard | wc -l | xargs echo "Untracked files:"
	@git log --oneline -5 | head -1 | xargs echo "Latest commit:"

# Performance testing
perf-test:
	@echo "⚡ Performance Testing"
	@echo "====================="
	@cd hts-local-database && python -c "\
import time; \
from utils.database import HTSDatabase; \
db = HTSDatabase(); \
start = time.time(); \
results = db.search_products('steel'); \
end = time.time(); \
print(f'Search test: {len(results)} results in {end-start:.3f}s')"