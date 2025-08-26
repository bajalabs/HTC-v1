# 🔍 Search Guide

Master the search capabilities of the HTS Database to quickly find the right classifications.

## 🚀 Quick Search

### Basic Product Search
```python
from utils.database import HTSDatabase
db = HTSDatabase()

# Simple keyword search
results = db.search_products("cotton shirt")
for result in results:
    print(f"{result['hts_code']}: {result['description']}")
```

### Search by HTS Code
```python
# Exact HTS code lookup
product = db.get_product_by_hts("6205.20.20")
if product:
    print(f"Found: {product['description']}")
    print(f"Duty Rate: {product['general_duty']}")
```

## 🎯 Advanced Search Techniques

### Multi-word Search
```python
# All words must appear (AND logic)
results = db.search_products("leather handbag women")

# Search with quotes for exact phrases
results = db.search_products('"synthetic rubber"')

# Use wildcards for partial matches
results = db.search_products("machin*")  # Finds "machine", "machinery", etc.
```

### Search by Product Categories
```python
# Search within specific chapters
results = db.search_products("shoes", chapter_filter=[64])  # Footwear chapter

# Search within sections
textile_chapters = list(range(50, 64))  # Textile sections
results = db.search_products("cotton", chapter_filter=textile_chapters)
```

### Filter by Attributes
```python
# Find duty-free products
results = db.search_products("electronics", duty_filter="Free")

# Find products with specific units
results = db.search_products("oil", unit_filter="kg")

# Combine filters
results = db.search_products("steel", 
                           chapter_filter=[72, 73],  # Iron & steel chapters
                           duty_filter="Free")
```

## 🔤 Search Syntax Reference

### Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `AND` | All terms must appear | `cotton AND shirt` |
| `OR` | Any term can appear | `leather OR synthetic` |
| `NOT` | Exclude terms | `shoes NOT leather` |
| `"quotes"` | Exact phrase | `"stainless steel"` |
| `*` | Wildcard | `electr*` (electronic, electrical) |
| `()` | Grouping | `(cotton OR wool) AND textile` |

### Examples
```python
# Complex search with operators
db.search_products('(cotton OR polyester) AND shirt NOT "t-shirt"')

# Search with parentheses for grouping
db.search_products('(steel OR iron) AND (pipe OR tube)')

# Exclude unwanted results
db.search_products('computer NOT software')
```

## 🏷️ Search by Classification Hierarchy

### By Chapter
```python
# Get all products in a chapter
chapter_1_products = db.get_chapter_products(1)  # Live animals
print(f"Chapter 1 has {len(chapter_1_products)} classifications")

# Search within specific chapters
results = db.search_products("frozen", chapter_filter=[2, 3, 16])  # Meat, fish, preparations
```

### By Section
```python
# Define section chapter ranges
sections = {
    'chemicals': range(28, 39),      # Chemical products
    'textiles': range(50, 64),       # Textiles and clothing
    'machinery': range(84, 86),      # Machinery and electrical
    'transport': range(86, 90),      # Transportation equipment
}

# Search within a section
chemical_results = db.search_products("acid", chapter_filter=list(sections['chemicals']))
```

### Hierarchical Navigation
```python
# Start broad, then narrow down
broad_search = db.search_products("electronic")

# Analyze results by chapter
from collections import Counter
chapters = [r['chapter'] for r in broad_search]
chapter_counts = Counter(chapters)

print("Electronic products by chapter:")
for chapter, count in chapter_counts.most_common():
    print(f"  Chapter {chapter}: {count} products")

# Focus on most relevant chapter
focused_results = db.search_products("electronic", chapter_filter=[85])
```

## 📊 Search Result Analysis

### Sorting and Ranking
```python
def rank_search_results(query, results):
    """Rank results by relevance"""
    query_words = set(query.lower().split())
    
    scored_results = []
    for result in results:
        description = result['description'].lower()
        description_words = set(description.split())
        
        # Calculate relevance score
        matches = query_words.intersection(description_words)
        score = len(matches) / len(query_words) if query_words else 0
        
        # Boost exact matches
        if query.lower() in description:
            score += 0.5
            
        scored_results.append((score, result))
    
    # Sort by score (highest first)
    return [result for score, result in sorted(scored_results, reverse=True)]

# Usage
results = db.search_products("cotton fabric")
ranked_results = rank_search_results("cotton fabric", results)

for result in ranked_results[:10]:
    print(f"{result['hts_code']}: {result['description']}")
```

### Filter and Analyze Results
```python
def analyze_search_results(results):
    """Analyze search results for insights"""
    if not results:
        return "No results found"
    
    analysis = {
        'total_results': len(results),
        'chapters_covered': len(set(r['chapter'] for r in results)),
        'duty_rates': {},
        'common_units': {},
        'avg_hts_length': sum(len(r['hts_code']) for r in results) / len(results)
    }
    
    # Analyze duty rates
    for result in results:
        duty = result.get('general_duty', 'Unknown')
        analysis['duty_rates'][duty] = analysis['duty_rates'].get(duty, 0) + 1
    
    # Analyze units
    for result in results:
        unit = result.get('unit', 'No unit')
        analysis['common_units'][unit] = analysis['common_units'].get(unit, 0) + 1
    
    return analysis

# Example usage
results = db.search_products("machinery")
analysis = analyze_search_results(results)

print(f"Found {analysis['total_results']} machinery products")
print(f"Across {analysis['chapters_covered']} different chapters")
print(f"Most common duty rates: {list(analysis['duty_rates'].keys())[:3]}")
```

## 🎯 Use Case Specific Searches

### For Importers/Exporters
```python
def find_similar_products(hts_code, limit=10):
    """Find products similar to a given HTS code"""
    base_product = db.get_product_by_hts(hts_code)
    if not base_product:
        return []
    
    # Extract key terms from description
    description = base_product['description']
    key_terms = extract_key_terms(description)  # Custom function
    
    # Search for similar products
    search_query = ' OR '.join(key_terms)
    similar = db.search_products(search_query, limit=limit*2)
    
    # Remove the original product and limit results
    filtered = [p for p in similar if p['hts_code'] != hts_code]
    return filtered[:limit]

def extract_key_terms(description, min_length=3):
    """Extract meaningful terms from product description"""
    import re
    
    # Remove common words and extract meaningful terms
    stop_words = {'the', 'and', 'or', 'of', 'for', 'with', 'from', 'other', 'not'}
    words = re.findall(r'\\b[a-zA-Z]{3,}\\b', description.lower())
    
    return [word for word in words if word not in stop_words][:5]

# Usage
similar_products = find_similar_products("6203.42.40")  # Men's cotton trousers
for product in similar_products:
    print(f"{product['hts_code']}: {product['description']}")
```

### For Compliance Officers
```python
def search_controlled_products():
    """Find products with special trade restrictions"""
    
    # Search for products with special duties or restrictions
    all_products = db.get_all_products()  # Implement this method
    
    controlled_products = []
    for product in all_products:
        flags = []
        
        # Check for anti-dumping
        if 'AD' in str(product.get('special_duty', '')):
            flags.append('Anti-dumping')
        
        # Check for quotas
        if product.get('quota_quantity'):
            flags.append('Quota restrictions')
        
        # Check for high duty rates
        general_duty = product.get('general_duty', '0')
        if '%' in general_duty:
            try:
                rate = float(general_duty.replace('%', ''))
                if rate > 25:  # High tariff threshold
                    flags.append('High tariff')
            except:
                pass
        
        if flags:
            controlled_products.append({
                'hts_code': product['hts_code'],
                'description': product['description'],
                'flags': flags
            })
    
    return controlled_products

# Usage
controlled = search_controlled_products()
print(f"Found {len(controlled)} products with special restrictions")
for product in controlled[:10]:
    print(f"{product['hts_code']}: {', '.join(product['flags'])}")
```

### For Researchers
```python
def trade_pattern_search(industry_keywords, years=None):
    """Search for products related to specific industries"""
    
    # Search for industry-related products
    results = []
    for keyword in industry_keywords:
        products = db.search_products(keyword)
        results.extend(products)
    
    # Remove duplicates
    unique_results = {}
    for product in results:
        unique_results[product['hts_code']] = product
    
    # Group by chapter for analysis
    by_chapter = {}
    for product in unique_results.values():
        chapter = product['chapter']
        if chapter not in by_chapter:
            by_chapter[chapter] = []
        by_chapter[chapter].append(product)
    
    return by_chapter

# Example: Green technology products
green_tech = trade_pattern_search([
    'solar', 'wind', 'electric vehicle', 'battery', 
    'renewable', 'photovoltaic', 'turbine'
])

print("Green technology products by chapter:")
for chapter, products in sorted(green_tech.items()):
    print(f"  Chapter {chapter}: {len(products)} products")
```

## 🚨 Search Tips and Best Practices

### Optimization Tips
1. **Start Broad**: Begin with general terms, then narrow down
2. **Use Synonyms**: Try different terms for the same concept
3. **Check Spelling**: Verify correct spelling of technical terms
4. **Consider Hierarchy**: Think about which HTS section your product belongs to
5. **Use Multiple Approaches**: Combine keyword search with chapter browsing

### Common Pitfalls
- **Too Specific**: Overly specific searches may miss relevant results
- **Wrong Category**: Looking in wrong HTS section/chapter
- **Terminology**: Using consumer terms instead of trade terminology
- **Incomplete Results**: Not considering all relevant product variations

### Search Strategy Workflow
```
1. Identify product → 2. Broad keyword search → 3. Analyze results by chapter
        ↓
4. Focus on relevant chapters → 5. Refine search terms → 6. Verify with similar products
        ↓
7. Cross-check with official sources → 8. Document findings
```

## 📚 Advanced Features

### Custom Search Functions
```python
# Create custom search for your specific needs
def automotive_parts_search(part_type, vehicle_type=None):
    \"\"\"Specialized search for automotive parts\"\"\"
    
    base_query = f"{part_type} automotive"
    if vehicle_type:
        base_query += f" {vehicle_type}"
    
    # Focus on automotive chapters (87-89)
    results = db.search_products(base_query, chapter_filter=[87, 88, 89])
    
    # Filter and rank results
    relevant_results = []
    for result in results:
        description = result['description'].lower()
        if part_type.lower() in description:
            relevant_results.append(result)
    
    return relevant_results

# Usage
brake_parts = automotive_parts_search("brake", "passenger")
```

Remember: The HTS Database search is designed to be flexible and powerful. Experiment with different approaches to find the search strategy that works best for your specific use case!

## 🆘 Need Help?

- **GitHub Issues**: Report search problems or suggest improvements
- **Documentation**: Check [examples.md](examples.md) for more search patterns
- **Community**: Join discussions for search tips and tricks