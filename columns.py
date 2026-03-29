import pandas as pd

print("=" * 70)
print("CHECKING COLUMN NAMES")
print("=" * 70)

# Load files
fact_sales = pd.read_csv('fact_sales.csv')
dim_product = pd.read_csv('dim_product.csv')
dim_location = pd.read_csv('dim_location.csv')
dim_customer = pd.read_csv('dim_customer.csv')

print("\n📊 FACT_SALES columns:")
print(fact_sales.columns.tolist())

print("\n📊 DIM_PRODUCT columns:")
print(dim_product.columns.tolist())

print("\n📊 DIM_LOCATION columns:")
print(dim_location.columns.tolist())

print("\n📊 DIM_CUSTOMER columns:")
print(dim_customer.columns.tolist())

print("\n📊 Sample data from fact_sales:")
print(fact_sales.head())