# Contributing to HTS Database Project

Thank you for your interest in contributing to the HTS Database Project! This project aims to democratize access to Harmonized Tariff System data through open-source collaboration.

## 🌟 Ways to Contribute

### 📊 Data Quality & Accuracy
- **Verify Classifications**: Review HTS codes for accuracy
- **Report Errors**: Identify incorrect tariff classifications
- **Add Missing Data**: Help complete Chapter 77 and 85
- **Validate Structure**: Ensure data consistency across formats

### 👨‍💻 Development
- **Bug Fixes**: Identify and fix issues in scripts or database
- **Feature Development**: Add new functionality to the database system
- **Performance Optimization**: Improve query speed and data processing
- **API Development**: Help build RESTful API endpoints

### 📚 Documentation
- **User Guides**: Write tutorials and how-to guides
- **Code Documentation**: Improve inline code comments
- **Use Case Examples**: Document real-world applications
- **Translation**: Help translate documentation for global users

### 🔍 Research & Analysis
- **Trade Analysis**: Conduct research using the HTS data
- **Data Visualization**: Create charts and insights from the data
- **Compliance Guidance**: Write classification guidance documents
- **Industry Studies**: Analyze trade patterns by industry

## 🚀 Getting Started

### 1. Fork the Repository
```bash
git clone https://github.com/yourusername/hts-database.git
cd hts-database
```

### 2. Set Up Development Environment
```bash
# Install dependencies
cd hts-local-database
pip install -r requirements.txt

# Build the database
python scripts/build_database.py

# Run tests (if available)
python -m pytest tests/
```

### 3. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## 📋 Contribution Guidelines

### Data Contributions
- **Sources**: Only use official government sources (USITC, CBP, etc.)
- **Accuracy**: Verify all data against official publications
- **Format**: Follow existing CSV/JSON/XLSX structure
- **Documentation**: Include source references and update dates

### Code Contributions
- **Style**: Follow PEP 8 for Python code
- **Testing**: Add tests for new functionality where possible  
- **Documentation**: Update relevant documentation files
- **Dependencies**: Minimize new dependencies; justify if needed

### Documentation Contributions
- **Clarity**: Write clear, concise explanations
- **Examples**: Include practical examples where helpful
- **Structure**: Follow existing markdown formatting
- **Links**: Ensure all links work and are relevant

## 🔍 Issue Reporting

### Bug Reports
Please include:
- **Description**: Clear description of the issue
- **Environment**: OS, Python version, dependencies
- **Steps to Reproduce**: Detailed steps to recreate the bug
- **Expected vs Actual**: What should happen vs what does happen
- **Data**: Sample data that demonstrates the issue (if applicable)

### Feature Requests
Please include:
- **Use Case**: Why this feature would be valuable
- **Description**: Detailed description of the proposed feature
- **Implementation Ideas**: Any thoughts on how to implement
- **Alternatives**: Other solutions you've considered

## 📊 Data Sources & Standards

### Official Sources
- **USITC**: US International Trade Commission (primary source)
- **CBP**: US Customs and Border Protection
- **Census Bureau**: Trade data and statistics
- **WTO**: World Trade Organization classifications

### Data Quality Standards
- **Completeness**: All required fields must be populated
- **Consistency**: Data must follow established patterns
- **Accuracy**: Cross-reference with official sources
- **Timeliness**: Include effective dates and update information

## 🎯 Priority Areas

### High Priority
1. **Complete Chapter 85**: Electrical machinery and equipment
2. **Add Chapter 77**: Reserved chapter (if activated)
3. **Database Performance**: Optimize search and query speed
4. **API Development**: Build RESTful endpoints for data access

### Medium Priority  
1. **Web Interface**: Browser-based search and classification
2. **Data Validation**: Automated quality checking
3. **Historical Data**: Multi-year tariff tracking
4. **Mobile Support**: Mobile-friendly interfaces

## 📝 Pull Request Process

### Before Submitting
1. **Test Your Changes**: Ensure your code works as expected
2. **Update Documentation**: Update relevant docs if needed
3. **Check Data Quality**: Verify any data changes for accuracy
4. **Clean Commits**: Make sure commit messages are clear

### Pull Request Template
```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] I have tested my changes locally
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] I have updated documentation as needed

## Data Sources (if applicable)
- List any official sources used for data changes
- Include URLs and access dates
```

## 🤝 Community Guidelines

### Be Respectful
- Treat all contributors with respect and professionalism
- Welcome newcomers and help them get started
- Provide constructive feedback on contributions
- Respect different perspectives and approaches

### Be Collaborative  
- Share knowledge and expertise freely
- Help others learn and grow
- Work together to solve problems
- Credit others for their contributions

### Be Professional
- Focus on trade accuracy and data quality
- Maintain professional standards in communications
- Follow proper citation practices for data sources
- Respect intellectual property and licensing terms

## 📞 Contact & Support

### Getting Help
- **GitHub Discussions**: For general questions and community support
- **Issues**: For bug reports and feature requests
- **Email**: [Contact information] for sensitive matters

### Community Channels
- **GitHub Discussions**: Project planning and general discussion
- **Issue Tracker**: Bug reports and feature requests
- **Documentation**: Guides and tutorials in the docs/ folder

---

## 🙏 Recognition

Contributors are recognized in several ways:
- **README Contributors**: Listed in the main README file
- **Release Notes**: Acknowledged in version release notes  
- **Documentation**: Credited in relevant documentation sections
- **Database**: Contributing organization/individual noted in database metadata

Thank you for helping make international trade data more accessible to everyone! 🚀🌍