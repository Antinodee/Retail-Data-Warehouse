import pandas as pd

print("=" * 70)
print("RETAIL DATA WAREHOUSE - ANALYTICS")
print("=" * 70)

# Load all CSV files
print("\n📊 Loading data...")
fact_sales = pd.read_csv('fact_sales.csv')
dim_product = pd.read_csv('dim_product.csv')
dim_location = pd.read_csv('dim_location.csv')
dim_customer = pd.read_csv('dim_customer.csv')

# Merge data (using correct lowercase column names)
sales_data = fact_sales.merge(dim_product, on='product_key')
sales_data = sales_data.merge(dim_location, on='location_key')
sales_data = sales_data.merge(dim_customer, on='customer_key')

print("✅ Data loaded and merged!")
print(f"   Total records: {len(sales_data):,}")

# Revenue by Category
print("\n" + "=" * 70)
print("📊 REVENUE BY CATEGORY")
print("=" * 70)
category_stats = sales_data.groupby('Category').agg({
    'Sales': ['count', 'sum'],
    'Profit': 'sum'
}).round(2)
category_stats.columns = ['Transactions', 'Revenue', 'Profit']
print(category_stats.sort_values('Revenue', ascending=False))

# Revenue by Region
print("\n" + "=" * 70)
print("📊 REVENUE BY REGION")
print("=" * 70)
region_stats = sales_data.groupby('Region').agg({
    'Sales': ['count', 'sum']
}).round(2)
region_stats.columns = ['Transactions', 'Revenue']
print(region_stats.sort_values('Revenue', ascending=False))

# Top 10 Customers
print("\n" + "=" * 70)
print("📊 TOP 10 CUSTOMERS BY SPENDING")
print("=" * 70)
customer_stats = sales_data.groupby(['Customer Name', 'Segment']).agg({
    'Sales': ['count', 'sum']
}).round(2)
customer_stats.columns = ['Orders', 'Total_Spent']
top_customers = customer_stats.sort_values('Total_Spent', ascending=False).head(10)
print(top_customers.to_string())

# Top 10 Products
print("\n" + "=" * 70)
print("📊 TOP 10 PRODUCTS BY REVENUE")
print("=" * 70)
product_stats = sales_data.groupby(['Product Name', 'Category']).agg({
    'Sales': 'sum'
}).round(2)
product_stats.columns = ['Revenue']
top_products = product_stats.sort_values('Revenue', ascending=False).head(10)
print(top_products.to_string())

# Overall Summary
print("\n" + "=" * 70)
print("📊 OVERALL SUMMARY")
print("=" * 70)
print(f"Total Transactions: {len(sales_data):,}")
print(f"Total Revenue: ${sales_data['Sales'].sum():,.2f}")
print(f"Total Profit: ${sales_data['Profit'].sum():,.2f}")
print(f"Profit Margin: {sales_data['Profit'].sum()/sales_data['Sales'].sum()*100:.1f}%")
print(f"Average Transaction: ${sales_data['Sales'].mean():,.2f}")

print("\n✅ Analytics Complete!")