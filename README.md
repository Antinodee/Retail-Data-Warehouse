# 🏪 Retail Data Warehouse - Star Schema Analytics

Enterprise-grade data warehouse with dimensional modeling for retail sales business intelligence using the Superstore Sales dataset.

## 📊 Project Overview

This project demonstrates data warehousing and business intelligence skills through a properly designed star schema containing fact and dimension tables optimized for analytical queries. Built using dimensional modeling principles, it enables efficient SQL analytics for retail business insights.

## 🎯 Dataset

**Source:** Superstore Sales Dataset (Tableau Sample Data)  
**Link:** https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

### Dataset Statistics:
- **Transactions:** 9,994 sales records
- **Revenue:** $2,297,200.86
- **Profit:** $286,397.02 (12.5% margin)
- **Time Period:** 2014-2017
- **Customers:** 793 unique customers
- **Products:** 1,894 unique products
- **Locations:** 632 locations across 4 US regions
- **License:** Public domain

## 🏗️ Star Schema Architecture

### Fact Table:
**fact_sales** (9,994 rows) - Sales transactions with metrics including sales amount, profit, quantity, and discount

### Dimension Tables:
- **dim_customer** (793 rows) - Customer master data with segment classification
- **dim_product** (1,894 rows) - Product catalog with category and sub-category
- **dim_location** (632 rows) - Geographic hierarchy (Country, Region, State, City)
- **dim_date** (1,434 rows) - Date dimension covering 2014-2017

### Schema Design:
The star schema follows Kimball methodology with a central fact table surrounded by denormalized dimension tables, optimized for OLAP queries and business intelligence reporting.

## 📈 Key Business Insights

### Revenue by Category:
| Category | Revenue | Percentage |
|----------|---------|------------|
| Technology | $836,154.03 | 36.4% |
| Furniture | $741,999.80 | 32.3% |
| Office Supplies | $719,047.03 | 31.3% |

### Revenue by Region:
| Region | Revenue | Transactions |
|--------|---------|--------------|
| West | $725,457.82 | 3,203 |
| East | $678,781.24 | 2,848 |
| Central | $501,239.89 | 2,323 |
| South | $391,721.91 | 1,620 |

### Performance Metrics:
- **Average Transaction Value:** $229.86
- **Profit Margin:** 12.5%
- **Top Product Category:** Technology (36.4%)
- **Top Revenue Region:** West ($725K)
- **Most Profitable Category:** Office Supplies
- **Customer Segments:** Consumer (51%), Corporate (30%), Home Office (19%)

## 🛠️ Technologies Used

**Database:**
- SQLite (relational database)
- Star schema design
- Foreign key relationships
- Optimized for OLAP queries

**Data Processing:**
- Python 3.8+
- pandas (data manipulation and analysis)
- SQL (complex analytical queries)

**Analysis Techniques:**
- Dimensional modeling (Kimball methodology)
- Fact and dimension table design
- SQL aggregations and joins
- Business intelligence metrics
- Time-series analysis

## 🚀 How to Run

### Installation:
Download or clone the repository and ensure you have Python 3.8+ with pandas installed. The project includes all necessary CSV files and a pre-built SQLite database ready for analysis.

### Files Included:
All dimension tables (dim_customer.csv, dim_product.csv, dim_location.csv, dim_date.csv), the sales fact table (fact_sales.csv), the complete SQLite database (retail_warehouse.db), and analytics scripts.

### Running Analytics:
Execute the included Python scripts to explore the data warehouse structure, run SQL queries, and generate business intelligence reports. The analytics show revenue by category, regional performance, top customers, product trends, and overall business metrics.

## 📁 Project Structure

The project contains CSV files for each dimension and fact table, a complete SQLite database with the star schema implemented, Python scripts for data exploration and analytics, and comprehensive documentation.

## 🎓 Skills Demonstrated

### Data Warehousing:
- Star schema design following industry best practices
- Dimensional modeling using Kimball methodology
- Fact and dimension table creation with proper granularity
- Surrogate key implementation for data warehouse integrity
- Foreign key relationships maintaining referential integrity
- Slowly changing dimension concepts (Type 1 implementation)

### SQL & Database:
- Complex JOIN operations across multiple tables
- Advanced aggregation functions (SUM, COUNT, AVG, ROUND)
- GROUP BY analysis for business metrics
- Query optimization for analytical workloads
- Subqueries and nested queries
- Window functions for advanced analytics

### Business Intelligence:
- Revenue and profit analysis by multiple dimensions
- Regional and categorical performance metrics
- Customer segmentation by purchase behavior
- Product performance tracking
- Time-series trend analysis
- KPI calculation and reporting

### Data Engineering:
- ETL pipeline design and implementation
- Data quality assurance and validation
- Referential integrity enforcement
- Schema optimization for OLAP workloads
- Denormalization strategies for query performance
- Data modeling best practices

## 📊 Business Value

This data warehouse enables executives and analysts to make data-driven decisions through:
- Real-time sales performance monitoring across regions and categories
- Customer behavior analysis for targeted marketing campaigns
- Product portfolio optimization based on profitability
- Inventory planning using demand patterns
- Financial reporting with profit margin analysis
- Strategic planning through historical trend analysis

## 🎯 Use Cases

**Executive Dashboards:** Track key performance indicators and overall business health with real-time metrics

**Sales Analysis:** Identify top-performing products, regions, and customer segments to optimize sales strategies

**Customer Analytics:** Segment customers by value and behavior to enable targeted retention and acquisition campaigns

**Inventory Planning:** Analyze product demand patterns by category and region to optimize stock levels

**Financial Reporting:** Generate comprehensive profit and loss reports with drill-down capabilities across all dimensions

**Strategic Planning:** Use historical trends to forecast future performance and guide business strategy

## 🔮 Future Enhancements

Potential improvements include implementing slowly changing dimensions (SCD Type 2) for historical tracking, creating aggregate fact tables for improved query performance, building OLAP cubes for multidimensional analysis, adding automated data quality checks and validation rules, developing a full ETL pipeline with scheduling and monitoring, and creating interactive Tableau or Power BI dashboards for end-user access.

## 💼 Interview Talking Points

**Star Schema Design:** Explain how the central fact table connects to dimension tables, the benefits of denormalization for analytical queries, and why this structure is optimal for business intelligence.

**Performance Optimization:** Discuss how the star schema reduces JOIN complexity compared to normalized databases, the use of surrogate keys for faster lookups, and query optimization strategies.

**Business Impact:** Describe how the 36.4% revenue concentration in Technology category informs inventory decisions, why the West region's $725K performance suggests expansion opportunities, and how the 12.5% profit margin compares to industry benchmarks.

**Dimensional Modeling:** Explain the Kimball methodology principles applied, the choice of grain for the fact table, and how dimensions were designed for maximum analytical flexibility.

**Real-World Application:** Connect this project to enterprise data warehousing, explain how it would scale to billions of rows, and discuss integration with BI tools and reporting systems.

## 👤 Author

**Rajeev Pernapati**
- MS Computer Science, University of Nevada, Las Vegas
- Email: rajeev30403@gmail.com
- GitHub: https://github.com/Antinodee
- LinkedIn: www.linkedin.com/in/pvn-rajeev

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Tableau for providing the Superstore sample dataset used in business intelligence training worldwide
- Kaggle community for maintaining accessible public datasets
- Ralph Kimball for pioneering dimensional modeling methodology
- The data warehousing community for best practices and guidance

---

**⭐ If you found this project useful, please consider giving it a star!**

**This project demonstrates enterprise-level data warehousing skills applicable to Data Engineer, Business Intelligence Analyst, and Analytics Engineer roles.** Public dataset
