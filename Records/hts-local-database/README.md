# HTS Local Database - AI-Driven Population System

A local-first Harmonized Tariff System database builder that uses AI agents to systematically populate the internationally standardized HS6 structure.

## Overview

This system builds a comprehensive HTS database starting with the core international classification structure:

- **21 Sections** (I-XXI)
- **97 Chapters** (01-97, excluding reserved chapter 77)
- **~1,228 Headings** (4-digit codes)
- **~5,612 Subheadings** (6-digit codes)

## Quick Start

### 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Build Database

```bash
# Build complete database (all phases)
python3 scripts/build_database.py

# Or run individual phases
python3 scripts/build_database.py --init        # Initialize database
python3 scripts/build_database.py --sections    # Populate sections only
python3 scripts/build_database.py --chapters    # Populate chapters only
```

### 3. Verify Results

The system will create:
- `database/hts.db` - SQLite database file
- `database/backups/` - Database backups
- `data/csv/manifest.json` - Build metadata

## Project Structure

```
hts-local-database/
├── database/
│   ├── hts.db                    # Main SQLite database
│   └── backups/                  # Database backups
├── data/
│   ├── csv/                      # CSV exports
│   ├── cache/                    # AI response cache
│   └── manifest.json             # Build metadata
├── agents/
│   ├── base_agent.py             # Base AI agent class
│   └── prompts/                  # AI prompt templates
├── scripts/
│   ├── build_database.py         # Main orchestrator
│   ├── populate_sections.py      # Phase 1: Sections
│   └── populate_chapters.py      # Phase 2: Chapters
├── utils/
│   └── database.py               # Database utilities
├── schema/
│   └── sql/sqlite/               # Database schema
├── config.yaml                   # Configuration
└── requirements.txt
```

## Current Status

✅ **Completed Features:**
- Database schema and structure
- Section population (21 records)
- Chapter population (52 of 97 records)
- Validation and integrity checks
- Backup and manifest generation

🚧 **In Progress:**
- Complete chapter dataset
- Heading population (~1,228 records)
- Subheading population (~5,612 records)

## Database Schema

The system uses a hierarchical structure:

```sql
sections (21) → chapters (97) → headings (~1,228) → subheadings (~5,612)
```

Key features:
- Foreign key constraints
- Validation triggers
- Full-text search capability
- AI extraction logging
- Progress tracking

## Configuration

Edit `config.yaml` to customize:

```yaml
ai_extraction:
  cache_responses: true
  confidence_threshold: 0.95
  batch_sizes:
    sections: 21
    chapters: 10
    headings: 20
    subheadings: 50
```

## Data Quality

The system includes comprehensive validation:
- Code format validation (2-digit, 4-digit, 6-digit)
- Hierarchical integrity checks
- Duplicate detection
- Orphan record detection

## Extending the System

### Adding New Population Scripts

1. Create script in `scripts/` directory
2. Inherit from `BaseExtractorAgent`
3. Implement extraction and validation logic
4. Add to main orchestrator

### Country-Specific Extensions

The schema supports country-specific 8/10/12-digit codes:
- Add country records to `countries` table
- Populate `country_classifications` table
- Extend validation rules as needed

## API Integration

For production use, replace hardcoded data with AI API calls:

```python
class ProductionExtractorAgent(BaseExtractorAgent):
    def call_ai(self, prompt: str) -> Dict:
        # Integrate with Claude API, GPT-4, etc.
        return api_response
```

## Contributing

1. Run existing phases to understand the structure
2. Add new extraction logic for headings/subheadings
3. Enhance validation rules
4. Add export formats (Excel, JSON, etc.)

## License

This project is designed for defensive security and legitimate HTS database management purposes only.