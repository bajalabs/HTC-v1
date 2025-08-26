# Claude Code Prompt: AI-Driven HTS Database Builder

## Project Mission
Build a local-first Harmonized Tariff System database by using AI agents to systematically populate the internationally standardized HS6 structure (21 sections → 97 chapters → 1,228 headings → 5,612 subheadings). This will serve as the foundation for later country-specific extensions.

## Development Environment Setup

### Project Structure
```
hts-local-database/
├── database/
│   ├── hts.db                    # Main SQLite database
│   └── backups/                  # Database backups
├── data/
│   ├── csv/
│   │   ├── core/                 # Core HS6 tables
│   │   ├── enhanced/             # AI-enhanced data
│   │   └── manifest.json         # Data manifest
│   └── cache/                    # AI response cache
├── agents/
│   ├── __init__.py
│   ├── extractor_agent.py        # AI data extraction
│   ├── validator_agent.py        # Data validation
│   ├── enhancer_agent.py         # Keyword/search enhancement
│   └── prompts/                  # AI prompt templates
├── scripts/
│   ├── build_database.py         # Main orchestrator
│   ├── populate_sections.py      # Phase 1: Sections
│   ├── populate_chapters.py      # Phase 2: Chapters
│   ├── populate_headings.py      # Phase 3: Headings
│   ├── populate_subheadings.py   # Phase 4: Subheadings
│   └── validate_hierarchy.py     # Validation script
├── utils/
│   ├── database.py               # Database utilities
│   ├── csv_handler.py            # CSV operations
│   └── progress.py               # Progress tracking
├── config.yaml                   # Configuration
├── requirements.txt
└── README.md
```

## Phase 1: Database & Infrastructure Setup

### Task 1.1: Create SQLite Database
```python
# database/setup.py
import sqlite3
from pathlib import Path

def create_database():
    """
    Create the SQLite database with all tables from the schema.
    Include indexes, views, and triggers.
    """
    db_path = Path("database/hts.db")
    
    # Read and execute the schema
    with open("schema/sqlite_schema.sql", "r") as f:
        schema = f.read()
    
    conn = sqlite3.connect(db_path)
    conn.executescript(schema)
    
    # Enable foreign keys
    conn.execute("PRAGMA foreign_keys = ON")
    
    # Create FTS5 search index
    create_search_index(conn)
    
    print(f"✅ Database created at {db_path}")
    return conn
```

### Task 1.2: AI Agent Base Class
```python
# agents/base_agent.py
from typing import Dict, List, Any
import json
import hashlib
from pathlib import Path

class BaseExtractorAgent:
    """
    Base class for AI-powered data extraction agents.
    Handles caching, validation, and error recovery.
    """
    
    def __init__(self, cache_dir="data/cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        
    def get_cached_response(self, prompt: str) -> Dict:
        """Check if we have a cached response for this prompt"""
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
        cache_file = self.cache_dir / f"{prompt_hash}.json"
        
        if cache_file.exists():
            with open(cache_file, "r") as f:
                return json.load(f)
        return None
    
    def cache_response(self, prompt: str, response: Dict):
        """Cache the AI response for reuse"""
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
        cache_file = self.cache_dir / f"{prompt_hash}.json"
        
        with open(cache_file, "w") as f:
            json.dump(response, f, indent=2)
    
    def extract_with_ai(self, prompt: str) -> Dict:
        """
        Main extraction method - this is where you'll integrate
        with Claude API or use the AI directly
        """
        # Check cache first
        cached = self.get_cached_response(prompt)
        if cached:
            print("📎 Using cached response")
            return cached
        
        # AI extraction logic here
        response = self.call_ai(prompt)
        
        # Cache the response
        self.cache_response(prompt, response)
        
        return response
    
    def validate_extraction(self, data: Dict) -> bool:
        """Validate extracted data meets requirements"""
        raise NotImplementedError
```

## Phase 2: AI-Driven Population Scripts

### Task 2.1: Populate Sections (21 records)
```python
# scripts/populate_sections.py
"""
AI Agent to populate the 21 HS sections.
This is the easiest starting point with only 21 records.
"""

SECTIONS_PROMPT = """
Generate a complete JSON array of the 21 sections in the Harmonized System (HS) classification.

For each section, provide:
1. section_number: Roman numeral (I through XXI)
2. section_range: Chapter range (e.g., "01-05")
3. title_en: Full English title
4. title_short: Abbreviated title (max 50 chars)
5. description: Brief description of what this section covers
6. chapter_count: Number of chapters in this section

Format as a JSON array. Ensure accuracy as this is the foundation of the classification system.

The sections cover:
- Section I: Live animals and animal products (Chapters 01-05)
- Section II: Vegetable products (Chapters 06-14)
[... continue with all 21 sections ...]

Return ONLY valid JSON, no additional text.
"""

def populate_sections(conn):
    agent = SectionExtractorAgent()
    
    print("🤖 Extracting 21 HS sections via AI...")
    sections = agent.extract_sections()
    
    print("✅ Validating section data...")
    if not agent.validate_sections(sections):
        raise ValueError("Section validation failed")
    
    print("💾 Inserting sections into database...")
    insert_sections(conn, sections)
    
    print("📊 Sections populated successfully!")
    return sections
```

### Task 2.2: Populate Chapters (97 records)
```python
# scripts/populate_chapters.py
"""
AI Agent to populate the 97 HS chapters.
Note: Chapter 77 is reserved and should be skipped.
"""

CHAPTERS_PROMPT_TEMPLATE = """
Generate a complete JSON array of all chapters for HS Section {section_number} ({section_title}).

This section covers chapters {chapter_range}.

For each chapter, provide:
1. chapter_code: Two-digit code (e.g., "01", "02")
2. title_en: Full English title
3. title_short: Abbreviated title (max 50 chars)
4. description: What this chapter covers
5. heading_count: Approximate number of headings
6. general_notes: Any important notes or rules

Ensure chapter 77 is marked as "Reserved" if encountered.

Return ONLY valid JSON array, no additional text.
"""

def populate_chapters(conn):
    # First, get all sections
    sections = get_sections_from_db(conn)
    
    all_chapters = []
    for section in sections:
        print(f"🤖 Extracting chapters for Section {section['section_number']}...")
        
        prompt = CHAPTERS_PROMPT_TEMPLATE.format(
            section_number=section['section_number'],
            section_title=section['title_en'],
            chapter_range=section['section_range']
        )
        
        chapters = agent.extract_with_ai(prompt)
        all_chapters.extend(chapters)
    
    print(f"✅ Extracted {len(all_chapters)} chapters")
    insert_chapters(conn, all_chapters)
```

### Task 2.3: Populate Headings (1,228 records)
```python
# scripts/populate_headings.py
"""
AI Agent to populate ~1,228 HS headings.
Process in batches by chapter to manage volume.
"""

HEADINGS_PROMPT_TEMPLATE = """
Generate all 4-digit heading codes for HS Chapter {chapter_code}: {chapter_title}

Provide headings in groups of 10. For each heading:
1. heading_code: 4-digit code (e.g., "{chapter_code}01", "{chapter_code}02")
2. title_en: Full English title
3. title_short: Abbreviated title
4. description: What this heading covers
5. is_residual: true if this is an "Other" category

Important patterns:
- Most chapters have headings from {chapter_code}01 to {chapter_code}99
- Not all numbers are used (there are gaps)
- Usually ends with an "Other" heading (e.g., {chapter_code}99)

Return as JSON array. Be accurate with the actual HS heading codes used.
"""

def populate_headings_batch(conn, chapter, batch_size=10):
    """Process headings in batches to avoid overwhelming the AI"""
    
    # Use a more targeted approach for each chapter
    headings = []
    
    # Get approximate heading count for this chapter
    estimated_headings = estimate_headings_for_chapter(chapter['chapter_code'])
    
    for batch_start in range(0, estimated_headings, batch_size):
        batch_prompt = create_batch_prompt(chapter, batch_start, batch_size)
        batch_headings = agent.extract_with_ai(batch_prompt)
        headings.extend(batch_headings)
        
        # Show progress
        print(f"  📦 Processed {len(headings)} headings for Chapter {chapter['chapter_code']}")
    
    return headings
```

### Task 2.4: Populate Subheadings (5,612 records)
```python
# scripts/populate_subheadings.py
"""
AI Agent to populate ~5,612 HS subheadings.
This is the most detailed level of the international classification.
"""

SUBHEADINGS_STRATEGY = """
For efficiency, use a multi-stage approach:

1. First pass: Get the structure
   - How many subheadings per heading?
   - What's the numbering pattern?
   
2. Second pass: Extract in batches
   - Process 5-10 headings at a time
   - Focus on accuracy over speed
   
3. Third pass: Validate and enhance
   - Check for gaps in numbering
   - Ensure hierarchical consistency
"""

def intelligent_subheading_extraction(conn):
    """
    Smart extraction that learns patterns and optimizes
    """
    
    # Learn the pattern from a sample
    sample_prompt = """
    Show me the subheading pattern for heading 0101 (Live horses, asses, mules and hinnies).
    Include all 6-digit codes and their titles.
    """
    
    sample = agent.extract_with_ai(sample_prompt)
    pattern = analyze_pattern(sample)
    
    # Apply pattern-based extraction
    print(f"📊 Detected pattern: {pattern}")
    
    # Now extract all subheadings using the learned pattern
    return batch_extract_with_pattern(conn, pattern)
```

## Phase 3: Validation & Enhancement

### Task 3.1: Hierarchy Validator
```python
# agents/validator_agent.py
class HierarchyValidator:
    """
    Validates the complete hierarchy for consistency
    """
    
    def validate_complete_hierarchy(self, conn):
        issues = []
        
        # Check code format compliance
        issues.extend(self.check_code_formats(conn))
        
        # Check parent-child relationships
        issues.extend(self.check_relationships(conn))
        
        # Check for gaps in numbering
        issues.extend(self.check_numbering_gaps(conn))
        
        # Check for duplicates
        issues.extend(self.check_duplicates(conn))
        
        # Use AI to validate descriptions make sense
        issues.extend(self.ai_semantic_validation(conn))
        
        return issues
    
    def ai_semantic_validation(self, conn):
        """Use AI to check if descriptions are sensible"""
        
        prompt = """
        Review these classification entries for semantic consistency:
        {entries}
        
        Check for:
        1. Descriptions that don't match the code hierarchy
        2. Inconsistent terminology
        3. Missing important details
        
        Return any issues found as JSON.
        """
        
        # Validate in batches
        return validate_with_ai(prompt)
```

### Task 3.2: Search Enhancement Agent
```python
# agents/enhancer_agent.py
class SearchEnhancerAgent:
    """
    Uses AI to generate keywords and improve searchability
    """
    
    def generate_keywords_for_subheading(self, subheading):
        prompt = f"""
        For HS code {subheading['code']}: {subheading['title']}
        
        Generate 10 relevant search keywords that someone might use to find this classification.
        Include:
        - Common trade names
        - Synonyms
        - Related terms
        - Common misspellings
        
        Return as JSON array of keywords with relevance scores (0-1).
        """
        
        keywords = self.extract_with_ai(prompt)
        return keywords
    
    def enhance_all_subheadings(self, conn):
        """Add keywords for all subheadings"""
        
        subheadings = get_all_subheadings(conn)
        
        for subheading in tqdm(subheadings, desc="Enhancing search"):
            keywords = self.generate_keywords_for_subheading(subheading)
            insert_keywords(conn, subheading['code'], keywords)
```

## Phase 4: Orchestration & Progress Tracking

### Task 4.1: Main Orchestrator
```python
# scripts/build_database.py
"""
Main script to orchestrate the entire database building process
"""

import sqlite3
from pathlib import Path
from datetime import datetime
import json

def build_complete_database():
    """
    Build the complete HS6 database using AI agents
    """
    
    print("🚀 Starting HTS Database Builder")
    print("=" * 50)
    
    # Setup
    conn = create_database()
    stats = {"start_time": datetime.now()}
    
    try:
        # Phase 1: Sections (21 records)
        print("\n📚 PHASE 1: Extracting Sections")
        populate_sections(conn)
        stats["sections"] = count_records(conn, "sections")
        
        # Phase 2: Chapters (97 records)
        print("\n📖 PHASE 2: Extracting Chapters")
        populate_chapters(conn)
        stats["chapters"] = count_records(conn, "chapters")
        
        # Phase 3: Headings (~1,228 records)
        print("\n📑 PHASE 3: Extracting Headings")
        populate_headings(conn)
        stats["headings"] = count_records(conn, "headings")
        
        # Phase 4: Subheadings (~5,612 records)
        print("\n📄 PHASE 4: Extracting Subheadings")
        populate_subheadings(conn)
        stats["subheadings"] = count_records(conn, "subheadings")
        
        # Phase 5: Validation
        print("\n✅ PHASE 5: Validating Hierarchy")
        issues = validate_hierarchy(conn)
        stats["validation_issues"] = len(issues)
        
        # Phase 6: Enhancement
        print("\n🔍 PHASE 6: Enhancing Search")
        enhance_search(conn)
        stats["keywords"] = count_records(conn, "keywords_search")
        
        # Phase 7: Export
        print("\n💾 PHASE 7: Exporting to CSV")
        export_to_csv(conn)
        
        # Complete
        stats["end_time"] = datetime.now()
        stats["duration"] = str(stats["end_time"] - stats["start_time"])
        
        print_summary(stats)
        save_manifest(stats)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()

def print_summary(stats):
    print("\n" + "=" * 50)
    print("✅ DATABASE BUILD COMPLETE!")
    print("=" * 50)
    print(f"📊 Statistics:")
    print(f"  • Sections:     {stats['sections']:,}")
    print(f"  • Chapters:     {stats['chapters']:,}")
    print(f"  • Headings:     {stats['headings']:,}")
    print(f"  • Subheadings:  {stats['subheadings']:,}")
    print(f"  • Keywords:     {stats['keywords']:,}")
    print(f"  • Issues Found: {stats['validation_issues']}")
    print(f"  • Time Taken:   {stats['duration']}")
```

### Task 4.2: Progress Tracking
```python
# utils/progress.py
from tqdm import tqdm
import json
from datetime import datetime

class ProgressTracker:
    """
    Track and resume progress for long-running operations
    """
    
    def __init__(self, checkpoint_file="progress.json"):
        self.checkpoint_file = checkpoint_file
        self.progress = self.load_progress()
    
    def load_progress(self):
        """Load previous progress if exists"""
        try:
            with open(self.checkpoint_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "sections_complete": False,
                "chapters_complete": False,
                "headings_complete": False,
                "subheadings_complete": False,
                "last_processed": None,
                "timestamp": None
            }
    
    def save_checkpoint(self, stage, last_item=None):
        """Save progress checkpoint"""
        self.progress[f"{stage}_complete"] = True
        self.progress["last_processed"] = last_item
        self.progress["timestamp"] = datetime.now().isoformat()
        
        with open(self.checkpoint_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def can_skip(self, stage):
        """Check if stage can be skipped"""
        return self.progress.get(f"{stage}_complete", False)
```

## Phase 5: Integration & Testing

### Task 5.1: CSV Export/Import
```python
# utils/csv_handler.py
import pandas as pd
import sqlite3
from pathlib import Path

class CSVHandler:
    """
    Handle CSV import/export for all tables
    """
    
    def export_to_csv(self, conn, output_dir="data/csv/core"):
        """Export all tables to CSV files"""
        
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        tables = ['sections', 'chapters', 'headings', 'subheadings']
        
        for table in tables:
            print(f"  📁 Exporting {table}.csv")
            df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
            df.to_csv(f"{output_dir}/{table}.csv", index=False)
        
        # Create manifest
        self.create_manifest(output_dir, tables)
    
    def import_from_csv(self, conn, input_dir="data/csv/core"):
        """Import CSV files to database"""
        
        tables = ['sections', 'chapters', 'headings', 'subheadings']
        
        for table in tables:
            csv_file = f"{input_dir}/{table}.csv"
            if Path(csv_file).exists():
                print(f"  📥 Importing {table}.csv")
                df = pd.read_csv(csv_file)
                df.to_sql(table, conn, if_exists='append', index=False)
```

### Task 5.2: Query Interface
```python
# utils/query_interface.py
class HTSQuery:
    """
    Simple query interface for the database
    """
    
    def search(self, conn, query):
        """Full-text search across all classifications"""
        
        sql = """
        SELECT 
            subheading_code as code,
            title_en as title,
            description
        FROM search_index
        WHERE search_index MATCH ?
        ORDER BY rank
        LIMIT 20
        """
        
        return pd.read_sql_query(sql, conn, params=[query])
    
    def get_hierarchy(self, conn, code):
        """Get complete hierarchy for a code"""
        
        sql = """
        SELECT * FROM v_complete_hierarchy
        WHERE subheading_code = ? OR
              heading_code = ? OR
              chapter_code = ?
        """
        
        return pd.read_sql_query(sql, conn, params=[code, code[:4], code[:2]])
```

## Configuration File
```yaml
# config.yaml
database:
  path: "database/hts.db"
  backup_dir: "database/backups"
  enable_fts: true

ai_extraction:
  cache_responses: true
  cache_dir: "data/cache"
  retry_attempts: 3
  confidence_threshold: 0.95
  
  # Batch sizes for extraction
  batch_sizes:
    sections: 21      # Get all at once
    chapters: 10      # Process 10 at a time
    headings: 20      # Process 20 at a time
    subheadings: 50   # Process 50 at a time

validation:
  strict_mode: true
  required_confidence: 0.90
  check_relationships: true
  check_formats: true

export:
  csv:
    encoding: "utf-8"
    include_metadata: true
  
  sqlite:
    vacuum_on_complete: true
    analyze_on_complete: true

progress:
  show_progress_bars: true
  save_checkpoints: true
  checkpoint_interval: 100
```

## Quick Start Commands

```bash
# Install dependencies
pip install sqlite3 pandas tqdm pyyaml requests

# Initialize database
python scripts/build_database.py --init

# Run complete build
python scripts/build_database.py --full

# Run specific phase
python scripts/populate_sections.py
python scripts/populate_chapters.py
python scripts/populate_headings.py
python scripts/populate_subheadings.py

# Validate data
python scripts/validate_hierarchy.py

# Export to CSV
python scripts/export_csv.py

# Run tests
python -m pytest tests/

# Interactive query
python -i utils/query_interface.py
```

## Tips for Claude Code & Cursor Integration

1. **Start Small**: Begin with sections (21 records) to test your pipeline
2. **Cache AI Responses**: Save AI responses to avoid re-querying
3. **Use Checkpoints**: Allow resuming from where you left off
4. **Validate Often**: Run validation after each phase
5. **Version Control**: Commit after each successful phase

## Expected Timeline

- **Phase 1 (Setup)**: 30 minutes
- **Phase 2 (Sections)**: 10 minutes
- **Phase 3 (Chapters)**: 30 minutes
- **Phase 4 (Headings)**: 2-3 hours
- **Phase 5 (Subheadings)**: 4-6 hours
- **Phase 6 (Validation)**: 1 hour
- **Phase 7 (Enhancement)**: 2-3 hours

Total: ~1-2 days of development with AI assistance

## Success Metrics

✅ All 21 sections populated
✅ All 97 chapters populated (excluding 77)
✅ ~1,228 headings with proper hierarchy
✅ ~5,612 subheadings with descriptions
✅ Zero validation errors
✅ Search keywords for top classifications
✅ CSV exports match database
✅ Manifest file with checksums