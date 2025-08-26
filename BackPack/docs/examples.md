# 💡 Usage Examples

Practical examples for using the HTS Database in real-world scenarios.

## 🔍 Product Classification Examples

### Example 1: Finding HTS Code for Electronics
```python
from utils.database import HTSDatabase

db = HTSDatabase()

# Search for smartphones
results = db.search_products("smartphone")
for result in results:
    print(f"HTS: {result['hts_code']}")
    print(f"Description: {result['description']}")
    print(f"General Duty: {result['general_duty']}")
    print("---")
```

### Example 2: Textile Classification
```python
# Search for cotton products
cotton_products = db.search_products("cotton shirt")

# Filter by chapter (textiles are in chapters 50-63)
textile_results = [p for p in cotton_products if 50 <= int(p['chapter']) <= 63]

for product in textile_results:
    print(f"Chapter {product['chapter']}: {product['description']}")
```

## 📊 Data Analysis Examples

### Example 3: Chapter Analysis
```python
import pandas as pd
from utils.database import HTSDatabase

db = HTSDatabase()

# Get all products in machinery chapter (84)
machinery = db.get_chapter_products(84)

# Convert to DataFrame for analysis
df = pd.DataFrame(machinery)

# Analyze duty rates
print("Average General Duty Rate:", df['general_duty'].mean())
print("Products with Zero Duty:", len(df[df['general_duty'] == 0]))

# Most common unit types
print("\nCommon Units of Quantity:")
print(df['unit'].value_counts().head())
```

### Example 4: Trade Analysis by Section
```python
# Analyze all chemical products (Section VI, Chapters 28-38)
chemical_chapters = range(28, 39)
chemical_data = []

for chapter in chemical_chapters:
    products = db.get_chapter_products(chapter)
    chemical_data.extend(products)

df_chemicals = pd.DataFrame(chemical_data)

# Analysis by duty rates
duty_analysis = df_chemicals.groupby('general_duty').size()
print("Chemical Products by Duty Rate:")
print(duty_analysis.sort_index())
```

## 🚢 Import/Export Use Cases

### Example 5: Duty Calculator
```python
def calculate_total_duty(hts_code, value, quantity=1):
    """Calculate estimated duty for a product"""
    
    product = db.get_product_by_hts(hts_code)
    if not product:
        return "HTS code not found"
    
    # Parse duty rate (simplified - real calculation more complex)
    duty_rate = product['general_duty']
    if 'Free' in duty_rate:
        duty_amount = 0
    elif '%' in duty_rate:
        rate = float(duty_rate.replace('%', ''))
        duty_amount = (value * rate / 100) * quantity
    else:
        # Specific duties (per unit)
        duty_amount = float(duty_rate) * quantity
    
    return {
        'hts_code': hts_code,
        'description': product['description'],
        'duty_rate': duty_rate,
        'duty_amount': duty_amount,
        'total_value': value * quantity + duty_amount
    }

# Example usage
result = calculate_total_duty("0101.21.00", 5000, 1)  # Live horse, $5000
print(f"Product: {result['description']}")
print(f"Duty Rate: {result['duty_rate']}")  
print(f"Estimated Duty: ${result['duty_amount']:.2f}")
```

### Example 6: Compliance Check
```python
def check_trade_compliance(hts_code, country_of_origin="CN"):
    """Check for special trade provisions"""
    
    product = db.get_product_by_hts(hts_code)
    if not product:
        return "Product not found"
    
    compliance_info = {
        'hts_code': hts_code,
        'description': product['description'],
        'general_duty': product['general_duty'],
        'special_duty': product['special_duty'],
        'warnings': []
    }
    
    # Check for anti-dumping (simplified)
    if product['special_duty'] and 'AD' in product['special_duty']:
        compliance_info['warnings'].append("Anti-dumping duties may apply")
    
    # Check for quota restrictions
    if product.get('quota_quantity'):
        compliance_info['warnings'].append("Product subject to quota restrictions")
    
    return compliance_info

# Example usage
compliance = check_trade_compliance("7208.10.00")  # Steel products
print(f"Product: {compliance['description']}")
if compliance['warnings']:
    print("⚠️  Compliance Warnings:")
    for warning in compliance['warnings']:
        print(f"  - {warning}")
```

## 🏭 Business Integration Examples

### Example 7: E-commerce Integration
```python
def suggest_hts_codes(product_description, max_results=5):
    """Suggest HTS codes for e-commerce products"""
    
    # Search for similar products
    results = db.search_products(product_description)
    
    suggestions = []
    for result in results[:max_results]:
        suggestions.append({
            'hts_code': result['hts_code'],
            'description': result['description'],
            'duty_rate': result['general_duty'],
            'confidence': calculate_similarity(product_description, result['description'])
        })
    
    return sorted(suggestions, key=lambda x: x['confidence'], reverse=True)

def calculate_similarity(desc1, desc2):
    """Simple similarity calculation (in real app, use more sophisticated methods)"""
    words1 = set(desc1.lower().split())
    words2 = set(desc2.lower().split())
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    return len(intersection) / len(union) if union else 0

# Example usage
suggestions = suggest_hts_codes("leather handbag")
print("HTS Code Suggestions for 'leather handbag':")
for suggestion in suggestions:
    print(f"{suggestion['hts_code']}: {suggestion['description']}")
    print(f"Confidence: {suggestion['confidence']:.2f}")
    print("---")
```

### Example 8: Supply Chain Analysis
```python
def analyze_supply_chain_duties(product_list):
    """Analyze duty costs across a supply chain"""
    
    total_analysis = {
        'products': [],
        'total_duty_cost': 0,
        'average_duty_rate': 0,
        'highest_duty_product': None,
        'duty_free_count': 0
    }
    
    duty_rates = []
    
    for product in product_list:
        hts_info = db.get_product_by_hts(product['hts_code'])
        if hts_info:
            # Simplified duty calculation
            duty_rate_str = hts_info['general_duty']
            
            if 'Free' in duty_rate_str:
                duty_rate = 0
                total_analysis['duty_free_count'] += 1
            elif '%' in duty_rate_str:
                duty_rate = float(duty_rate_str.replace('%', ''))
            else:
                duty_rate = 0  # Specific duties - would need more complex calculation
            
            duty_cost = (product['value'] * duty_rate / 100)
            duty_rates.append(duty_rate)
            
            product_analysis = {
                'hts_code': product['hts_code'],
                'description': hts_info['description'],
                'value': product['value'],
                'duty_rate': duty_rate,
                'duty_cost': duty_cost
            }
            
            total_analysis['products'].append(product_analysis)
            total_analysis['total_duty_cost'] += duty_cost
            
            # Track highest duty product
            if not total_analysis['highest_duty_product'] or duty_rate > total_analysis['highest_duty_product']['duty_rate']:
                total_analysis['highest_duty_product'] = product_analysis
    
    if duty_rates:
        total_analysis['average_duty_rate'] = sum(duty_rates) / len(duty_rates)
    
    return total_analysis

# Example supply chain
supply_chain = [
    {'hts_code': '6203.42.40', 'value': 50000},  # Cotton trousers
    {'hts_code': '6404.11.20', 'value': 30000},  # Sports footwear  
    {'hts_code': '4202.92.30', 'value': 20000},  # Handbags
]

analysis = analyze_supply_chain_duties(supply_chain)
print(f"Total Supply Chain Value: ${sum(p['value'] for p in supply_chain):,}")
print(f"Total Estimated Duties: ${analysis['total_duty_cost']:,.2f}")
print(f"Average Duty Rate: {analysis['average_duty_rate']:.2f}%")
print(f"Duty-Free Products: {analysis['duty_free_count']}")

if analysis['highest_duty_product']:
    print(f"\nHighest Duty Product:")
    print(f"  {analysis['highest_duty_product']['hts_code']}: {analysis['highest_duty_product']['duty_rate']:.1f}%")
```

## 🎓 Educational Examples

### Example 9: Trade Policy Research
```python
def analyze_protection_by_industry():
    """Analyze tariff protection levels by industry sector"""
    
    industry_analysis = {}
    
    # Define industry mappings (simplified)
    industries = {
        'Agriculture': range(1, 25),      # Chapters 1-24
        'Chemicals': range(28, 39),       # Chapters 28-38  
        'Textiles': range(50, 64),        # Chapters 50-63
        'Machinery': range(84, 86),       # Chapters 84-85
        'Transportation': range(86, 90),  # Chapters 86-89
    }
    
    for industry_name, chapters in industries.items():
        duty_rates = []
        product_count = 0
        
        for chapter in chapters:
            products = db.get_chapter_products(chapter)
            for product in products:
                duty_str = product.get('general_duty', 'Free')
                if 'Free' in duty_str:
                    duty_rates.append(0)
                elif '%' in duty_str:
                    try:
                        rate = float(duty_str.replace('%', ''))
                        duty_rates.append(rate)
                    except:
                        continue
                product_count += 1
        
        if duty_rates:
            industry_analysis[industry_name] = {
                'average_duty': sum(duty_rates) / len(duty_rates),
                'max_duty': max(duty_rates),
                'min_duty': min(duty_rates),
                'product_count': product_count,
                'duty_free_percent': (duty_rates.count(0) / len(duty_rates)) * 100
            }
    
    return industry_analysis

# Run analysis
protection_analysis = analyze_protection_by_industry()

print("Tariff Protection by Industry:")
print("=" * 50)
for industry, stats in protection_analysis.items():
    print(f"\n{industry}:")
    print(f"  Average Duty Rate: {stats['average_duty']:.2f}%")
    print(f"  Range: {stats['min_duty']:.1f}% - {stats['max_duty']:.1f}%")
    print(f"  Products Analyzed: {stats['product_count']:,}")
    print(f"  Duty-Free Products: {stats['duty_free_percent']:.1f}%")
```

## 🔧 Integration Templates

### Example 10: REST API Endpoint Template
```python
from flask import Flask, jsonify, request
from utils.database import HTSDatabase

app = Flask(__name__)
db = HTSDatabase()

@app.route('/api/search')
def search_products():
    """Search HTS products"""
    query = request.args.get('q', '')
    limit = min(int(request.args.get('limit', 10)), 100)
    
    if not query:
        return jsonify({'error': 'Query parameter required'}), 400
    
    results = db.search_products(query)[:limit]
    
    return jsonify({
        'query': query,
        'count': len(results),
        'results': results
    })

@app.route('/api/chapter/<int:chapter_id>')
def get_chapter(chapter_id):
    """Get chapter information"""
    if not 1 <= chapter_id <= 97:
        return jsonify({'error': 'Invalid chapter number'}), 400
    
    chapter_info = db.get_chapter(chapter_id)
    products = db.get_chapter_products(chapter_id)
    
    return jsonify({
        'chapter': chapter_info,
        'product_count': len(products),
        'products': products[:50]  # Limit for performance
    })

@app.route('/api/hts/<hts_code>')
def get_product(hts_code):
    """Get specific HTS product information"""
    product = db.get_product_by_hts(hts_code)
    
    if not product:
        return jsonify({'error': 'HTS code not found'}), 404
    
    return jsonify(product)

if __name__ == '__main__':
    app.run(debug=True)
```

These examples demonstrate the versatility of the HTS Database for various business, research, and development use cases. Adapt them to your specific needs!

## 📚 Additional Resources

- [Database Schema](../hts-local-database/README_v2.md)
- [Search Guide](search-guide.md)
- [Contributing Guidelines](../CONTRIBUTING.md)
- [API Documentation](api.md) *(Coming Soon)*