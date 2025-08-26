#!/usr/bin/env python3
"""
AI Agent to populate the 21 HS sections.
This is the easiest starting point with only 21 records.
"""

import json
import logging
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from agents.base_agent import ClaudeExtractorAgent
from utils.database import HTSDatabase

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class SectionExtractorAgent(ClaudeExtractorAgent):
    """Specialized agent for extracting HS sections."""
    
    def __init__(self, cache_dir: str = "data/cache"):
        super().__init__(cache_dir)
        self.sections_data = None
    
    def load_prompt(self) -> str:
        """Load the sections extraction prompt."""
        prompt_file = Path("agents/prompts/sections_prompt.txt")
        if prompt_file.exists():
            with open(prompt_file, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            # Fallback prompt if file doesn't exist
            return self.get_fallback_prompt()
    
    def get_fallback_prompt(self) -> str:
        """Fallback prompt for sections extraction."""
        return """
        Generate a complete JSON array of the 21 sections in the Harmonized System (HS) classification.
        
        For each section, provide:
        1. section_number: Roman numeral (I through XXI)
        2. section_range: Chapter range (e.g., "01-05")
        3. title_en: Full English title
        4. title_short: Abbreviated title (max 50 chars)
        5. description: Brief description of what this section covers
        6. chapter_count: Number of chapters in this section
        
        Return ONLY valid JSON array, no additional text.
        """
    
    def get_hardcoded_sections(self) -> list:
        """
        Hardcoded sections data as fallback or for immediate implementation.
        Based on HS 2022 edition.
        """
        return [
            {
                "section_number": "I",
                "section_range": "01-05",
                "title_en": "Live animals; animal products",
                "title_short": "Live animals & animal products",
                "description": "Live animals and products derived from animals including meat, dairy, eggs, honey, and other animal products",
                "chapter_count": 5,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "II",
                "section_range": "06-14",
                "title_en": "Vegetable products",
                "title_short": "Vegetable products",
                "description": "Live plants, vegetables, fruits, nuts, spices, cereals, and other products of plant origin",
                "chapter_count": 9,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "III",
                "section_range": "15",
                "title_en": "Animal, vegetable fats and oils, cleavage products, etc.",
                "title_short": "Fats, oils & cleavage products",
                "description": "Animal and vegetable fats and oils and their cleavage products; prepared edible fats; animal or vegetable waxes",
                "chapter_count": 1,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "IV",
                "section_range": "16-24",
                "title_en": "Prepared foodstuffs; beverages, spirits and vinegar; tobacco and manufactured tobacco substitutes",
                "title_short": "Prepared foodstuffs & beverages",
                "description": "Prepared food products, beverages, alcoholic drinks, vinegar, tobacco and tobacco substitutes",
                "chapter_count": 9,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "V",
                "section_range": "25-27",
                "title_en": "Mineral products",
                "title_short": "Mineral products",
                "description": "Salt, sulphur, earths and stone, plastering materials, lime, cement, ores, mineral fuels, oils and products of their distillation",
                "chapter_count": 3,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "VI",
                "section_range": "28-38",
                "title_en": "Products of the chemical or allied industries",
                "title_short": "Chemical products",
                "description": "Inorganic and organic chemicals, pharmaceutical products, fertilizers, tanning and dyeing extracts, paints, varnishes, soap, cosmetics, explosives, photographic supplies, and miscellaneous chemical products",
                "chapter_count": 11,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "VII",
                "section_range": "39-40",
                "title_en": "Plastics and articles thereof; rubber and articles thereof",
                "title_short": "Plastics & rubber",
                "description": "Plastics and plastic articles, rubber and rubber articles",
                "chapter_count": 2,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "VIII",
                "section_range": "41-43",
                "title_en": "Raw hides and skins, leather, furskins and articles thereof; saddlery and harness; travel goods, handbags and similar containers; articles of animal gut",
                "title_short": "Hides, skins, leather & fur",
                "description": "Raw hides and skins, leather, furskins and articles made from these materials, saddlery, harness, travel goods and handbags",
                "chapter_count": 3,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "IX",
                "section_range": "44-46",
                "title_en": "Wood and articles of wood; wood charcoal; cork and articles of cork; manufactures of straw, of esparto or of other plaiting materials; basketware and wickerwork",
                "title_short": "Wood, cork & plaiting materials",
                "description": "Wood and wood articles, wood charcoal, cork and cork articles, and manufactures of straw or other plaiting materials",
                "chapter_count": 3,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "X",
                "section_range": "47-49",
                "title_en": "Pulp of wood or of other fibrous cellulosic material; recovered (waste and scrap) paper or paperboard; paper and paperboard and articles thereof",
                "title_short": "Pulp, paper & paperboard",
                "description": "Pulp of wood or other fibrous cellulosic material, recovered paper or paperboard, and paper and paperboard articles",
                "chapter_count": 3,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XI",
                "section_range": "50-63",
                "title_en": "Textiles and textile articles",
                "title_short": "Textiles & textile articles",
                "description": "Silk, wool, cotton, synthetic and artificial fibers, fabrics, carpets, special woven fabrics, knitted and crocheted fabrics, apparel and clothing accessories, and other made-up textile articles",
                "chapter_count": 14,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XII",
                "section_range": "64-67",
                "title_en": "Footwear, headgear, umbrellas, sun umbrellas, walking sticks, seat-sticks, whips, riding-crops and parts thereof; prepared feathers and articles made therewith; artificial flowers; articles of human hair",
                "title_short": "Footwear, headgear & accessories",
                "description": "Footwear, headgear, umbrellas, walking sticks, prepared feathers, artificial flowers and articles of human hair",
                "chapter_count": 4,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XIII",
                "section_range": "68-70",
                "title_en": "Articles of stone, plaster, cement, asbestos, mica or similar materials; ceramic products; glass and glassware",
                "title_short": "Stone, ceramic & glass",
                "description": "Articles of stone, plaster, cement, asbestos, mica or similar materials, ceramic products, and glass and glassware",
                "chapter_count": 3,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XIV",
                "section_range": "71",
                "title_en": "Natural or cultured pearls, precious or semi-precious stones, precious metals, metals clad with precious metal, and articles thereof; imitation jewellery; coin",
                "title_short": "Pearls, precious stones & metals",
                "description": "Natural or cultured pearls, precious or semi-precious stones, precious metals and articles thereof, imitation jewellery and coin",
                "chapter_count": 1,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XV",
                "section_range": "72-83",
                "title_en": "Base metals and articles of base metal",
                "title_short": "Base metals & articles",
                "description": "Iron and steel, copper, nickel, aluminium, lead, zinc, tin, other base metals, tools, cutlery, hardware, and various articles of base metal",
                "chapter_count": 12,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XVI",
                "section_range": "84-85",
                "title_en": "Machinery and mechanical appliances; electrical equipment; parts thereof; sound recorders and reproducers, television image and sound recorders and reproducers, and parts and accessories of such articles",
                "title_short": "Machinery & electrical equipment",
                "description": "Nuclear reactors, boilers, machinery, mechanical appliances, electrical machinery and equipment, sound and television apparatus",
                "chapter_count": 2,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XVII",
                "section_range": "86-89",
                "title_en": "Vehicles, aircraft, vessels and associated transport equipment",
                "title_short": "Transport equipment",
                "description": "Railway locomotives and rolling stock, motor vehicles, aircraft, ships, boats and floating structures",
                "chapter_count": 4,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XVIII",
                "section_range": "90-92",
                "title_en": "Optical, photographic, cinematographic, measuring, checking, precision, medical or surgical instruments and apparatus; clocks and watches; musical instruments; parts and accessories thereof",
                "title_short": "Precision instruments & apparatus",
                "description": "Optical, photographic, cinematographic, measuring, checking, precision, medical or surgical instruments and apparatus, clocks, watches, and musical instruments",
                "chapter_count": 3,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XIX",
                "section_range": "93",
                "title_en": "Arms and ammunition; parts and accessories thereof",
                "title_short": "Arms & ammunition",
                "description": "Arms and ammunition and parts and accessories thereof",
                "chapter_count": 1,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XX",
                "section_range": "94-96",
                "title_en": "Miscellaneous manufactured articles",
                "title_short": "Miscellaneous manufactured articles",
                "description": "Furniture, bedding, lamps, prefabricated buildings, toys, games, sports equipment, and various other manufactured articles",
                "chapter_count": 3,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            },
            {
                "section_number": "XXI",
                "section_range": "97",
                "title_en": "Works of art, collectors' pieces and antiques",
                "title_short": "Works of art & antiques",
                "description": "Paintings, drawings, original engravings, prints and lithographs, original sculptures, postage stamps, collections and collectors' pieces, and antiques",
                "chapter_count": 1,
                "confidence_score": 1.0,
                "source_reference": "HS_2022_manual"
            }
        ]
    
    def extract_sections(self) -> list:
        """Extract sections data using AI or fallback to hardcoded data."""
        try:
            # Load prompt
            prompt = self.load_prompt()
            logger.info("Loading sections data...")
            
            # For now, use hardcoded data for immediate implementation
            # In production, this would call AI services
            sections = self.get_hardcoded_sections()
            
            logger.info(f"Extracted {len(sections)} sections")
            self.sections_data = sections
            return sections
            
        except Exception as e:
            logger.error(f"Failed to extract sections: {e}")
            # Fallback to hardcoded data
            return self.get_hardcoded_sections()
    
    def validate_sections(self, sections: list) -> bool:
        """Validate sections data."""
        if not sections:
            logger.error("No sections data provided")
            return False
        
        if len(sections) != 21:
            logger.error(f"Expected 21 sections, got {len(sections)}")
            return False
        
        required_fields = ['section_number', 'section_range', 'title_en', 'chapter_count']
        
        for i, section in enumerate(sections):
            for field in required_fields:
                if field not in section or not section[field]:
                    logger.error(f"Section {i+1}: Missing required field '{field}'")
                    return False
            
            # Validate section number format (Roman numerals I-XXI)
            if not section['section_number'] in [
                'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
                'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI'
            ]:
                logger.error(f"Invalid section number: {section['section_number']}")
                return False
        
        logger.info("✅ All sections validated successfully")
        return True


def main():
    """Main function to populate sections."""
    logger.info("🤖 Starting HS Sections Population")
    logger.info("=" * 50)
    
    try:
        # Initialize database
        db = HTSDatabase()
        
        # Check if tables exist, create if not
        try:
            db.create_tables()
        except Exception as e:
            logger.warning(f"Tables might already exist: {e}")
        
        # Initialize agent
        agent = SectionExtractorAgent()
        
        # Extract sections
        logger.info("🤖 Extracting 21 HS sections...")
        sections = agent.extract_sections()
        
        # Validate sections
        logger.info("✅ Validating section data...")
        if not agent.validate_sections(sections):
            raise ValueError("Section validation failed")
        
        # Insert into database
        logger.info("💾 Inserting sections into database...")
        inserted_count = db.insert_sections(sections)
        
        # Get statistics
        stats = db.get_statistics()
        
        logger.info("📊 Sections populated successfully!")
        logger.info(f"   • Sections inserted: {inserted_count}")
        logger.info(f"   • Total in database: {stats['total_sections']}")
        
        return sections
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()