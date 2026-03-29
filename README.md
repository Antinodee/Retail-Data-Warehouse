# Retail Data Warehouse & Advanced SQL Analytics

## Dataset: Superstore Sales (Public Dataset)

**Source:** Tableau Sample Data  
**Link:** https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

## Dataset Statistics
- **9,994 sales transactions** (2014-2017)
- **793 unique customers**
- **1,894 unique products**
- **$2.3M total sales**
- **$286K total profit** (12.5% margin)

## Star Schema Design
✅ **dim_customer** - 793 customers  
✅ **dim_product** - 1,894 products (3 categories)  
✅ **dim_location** - 632 locations (4 US regions)  
✅ **dim_date** - 1,434 dates  
✅ **fact_sales** - 9,994 transactions

## Project Features
✅ Dimensional modeling (star schema)  
✅ Advanced SQL analytics (7 queries)  
✅ Automated PDF report generation  
✅ Business intelligence insights

## Key Insights
- **Technology:** $836K (36.4% of revenue)
- **Furniture:** $742K (32.3% of revenue)
- **Office Supplies:** $719K (31.3% of revenue)

## Files
- `dim_*.csv` - Dimension tables
- `fact_sales.csv` - Fact table
- `retail_warehouse.db` - SQLite database

## How to Use
1. Download Superstore dataset from Kaggle
2. Process data into star schema
3. Run SQL analytics

**License:** Public dataset
