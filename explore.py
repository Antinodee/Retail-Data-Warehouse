import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect('retail_warehouse.db')

print("=" * 70)
print("RETAIL DATA WAREHOUSE - EXPLORATION")
print("=" * 70)

# Check tables
print("\n📊 Available Tables:")
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
print(tables)

# Summary stats
print("\n" + "=" * 70)
print("WAREHOUSE STATISTICS")
print("=" * 70)

stats = pd.read_sql_query("""
    SELECT 
        COUNT(*) as Total_Transactions,
        ROUND(SUM(Sales), 2) as Total_Revenue,
        ROUND(SUM(Profit), 2) as Total_Profit,
        ROUND(AVG(Sales), 2) as Avg_Transaction
    FROM fact_sales
""", conn)
print(stats)

# Dimension counts
print("\n📊 Dimension Tables:")
for table in ['dim_customer', 'dim_product', 'dim_location', 'dim_date']:
    count = pd.read_sql_query(f"SELECT COUNT(*) as count FROM {table}", conn).iloc[0, 0]
    print(f"  {table}: {count:,} rows")

# Sample data
print("\n" + "=" * 70)
print("SAMPLE SALES DATA (First 5 rows)")
print("=" * 70)
sample = pd.read_sql_query("SELECT * FROM fact_sales LIMIT 5", conn)
print(sample)

conn.close()
print("\n✅ Data Warehouse Loaded Successfully!")