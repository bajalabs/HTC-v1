"""
Base class for AI-powered data extraction agents.
Handles caching, validation, and error recovery.
"""

from typing import Dict, List, Any, Optional
import json
import hashlib
import time
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class BaseExtractorAgent:
    """
    Base class for AI-powered data extraction agents.
    Handles caching, validation, and error recovery.
    """
    
    def __init__(self, cache_dir: str = "data/cache", confidence_threshold: float = 0.95):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.confidence_threshold = confidence_threshold
        
    def get_cached_response(self, prompt: str) -> Optional[Dict]:
        """Check if we have a cached response for this prompt"""
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
        cache_file = self.cache_dir / f"{prompt_hash}.json"
        
        if cache_file.exists():
            try:
                with open(cache_file, "r", encoding='utf-8') as f:
                    cached_data = json.load(f)
                    logger.info("Using cached response")
                    return cached_data
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load cached response: {e}")
                
        return None
    
    def cache_response(self, prompt: str, response: Dict) -> None:
        """Cache the AI response for reuse"""
        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
        cache_file = self.cache_dir / f"{prompt_hash}.json"
        
        try:
            with open(cache_file, "w", encoding='utf-8') as f:
                json.dump(response, f, indent=2, ensure_ascii=False)
            logger.info(f"Cached response to {cache_file}")
        except IOError as e:
            logger.error(f"Failed to cache response: {e}")
    
    def extract_with_ai(self, prompt: str) -> Dict:
        """
        Main extraction method - override this in subclasses
        to integrate with specific AI services (Claude, GPT-4, etc.)
        """
        # Check cache first
        cached = self.get_cached_response(prompt)
        if cached:
            return cached
        
        # This should be overridden in subclasses
        response = self.call_ai(prompt)
        
        # Cache the response
        self.cache_response(prompt, response)
        
        return response
    
    def call_ai(self, prompt: str) -> Dict:
        """
        Override this method in subclasses to implement specific AI API calls.
        Should return a structured dictionary with extracted data.
        """
        raise NotImplementedError("Subclasses must implement call_ai method")
    
    def validate_extraction(self, data: Dict, expected_fields: List[str]) -> bool:
        """Validate extracted data meets requirements"""
        if not isinstance(data, dict):
            logger.error("Extracted data is not a dictionary")
            return False
            
        # Check for required fields
        for field in expected_fields:
            if field not in data:
                logger.error(f"Missing required field: {field}")
                return False
                
        return True
    
    def retry_with_backoff(self, func, max_retries: int = 3, base_delay: float = 1.0):
        """Retry function with exponential backoff"""
        for attempt in range(max_retries):
            try:
                return func()
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                
                delay = base_delay * (2 ** attempt)
                logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                time.sleep(delay)
                
        raise RuntimeError(f"Failed after {max_retries} attempts")
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text data"""
        if not text:
            return ""
            
        # Remove extra whitespace
        text = " ".join(text.split())
        
        # Remove common formatting artifacts
        text = text.replace("—", "-")
        text = text.replace(""", '"')
        text = text.replace(""", '"')
        text = text.replace("'", "'")
        text = text.replace("'", "'")
        
        return text.strip()
    
    def log_extraction(self, batch_id: str, table_name: str, records_count: int, 
                      validation_errors: int = 0, prompt: str = "", raw_response: str = "") -> None:
        """Log extraction details for debugging and auditing"""
        log_entry = {
            "batch_id": batch_id,
            "table_name": table_name,
            "records_count": records_count,
            "validation_errors": validation_errors,
            "timestamp": time.time(),
            "prompt_hash": hashlib.md5(prompt.encode()).hexdigest()[:8],
            "raw_response_length": len(raw_response)
        }
        
        log_file = self.cache_dir / "extraction_log.jsonl"
        try:
            with open(log_file, "a", encoding='utf-8') as f:
                f.write(json.dumps(log_entry) + "\n")
        except IOError as e:
            logger.error(f"Failed to write extraction log: {e}")


class ClaudeExtractorAgent(BaseExtractorAgent):
    """
    AI extraction agent that integrates with Claude API or Claude Code environment.
    Since we're in Claude Code, this will use the current session for extractions.
    """
    
    def call_ai(self, prompt: str) -> Dict:
        """
        In Claude Code environment, we'll provide structured prompts
        and expect the human user to provide responses or we'll use
        web search and other tools to gather the data.
        """
        logger.info("AI extraction requested - in Claude Code environment")
        
        # For now, return a placeholder structure
        # In actual implementation, this would integrate with AI services
        return {
            "status": "placeholder",
            "data": [],
            "confidence": 1.0,
            "prompt_used": prompt[:100] + "..." if len(prompt) > 100 else prompt
        }


class WebScrapingAgent(BaseExtractorAgent):
    """
    Agent that extracts HS data from official sources via web scraping.
    """
    
    def __init__(self, cache_dir: str = "data/cache", confidence_threshold: float = 0.9):
        super().__init__(cache_dir, confidence_threshold)
        self.known_sources = [
            "https://unstats.un.org/unsd/tradekb/Knowledgebase/50018/Harmonized-Commodity-Description-and-Coding-Systems-HS",
            "https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs_nomenclature_2022_edition.aspx"
        ]
    
    def call_ai(self, prompt: str) -> Dict:
        """
        Use web scraping to gather HS classification data from official sources.
        """
        # This would implement web scraping logic
        return {
            "status": "web_scraping_placeholder",
            "data": [],
            "confidence": 0.8,
            "sources": self.known_sources
        }