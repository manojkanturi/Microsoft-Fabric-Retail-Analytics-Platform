import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# --- 1. Generate Customers ---
customer_data = []
for i in range(1, 101): # 100 customers
    customer_data.append({
        'customer_id': i,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'city': fake.city()
    })
customers_df = pd.DataFrame(customer_data)
customers_df.to_csv('customers.csv', index=False)
print("customers.csv created.")

# --- 2. Generate Products ---
products = [
    ("T-Shirt", 25.00), ("Jeans", 75.00), ("Jacket", 120.00),
    ("Sneakers", 90.00), ("Hat", 20.00), ("Socks", 10.00)
]
product_data = []
for i, p in enumerate(products, 1):
    product_data.append({
        'product_id': i,
        'product_name': p[0],
        'price': p[1]
    })
products_df = pd.DataFrame(product_data)
products_df.to_csv('products.csv', index=False)
print("products.csv created.")

# --- 3. Generate Sales Transactions ---
sales_data = []
start_date = datetime(2023, 1, 1)
for i in range(1, 501): # 500 sales transactions
    customer_id = random.randint(1, 100)
    product_id = random.randint(1, 6)
    units_sold = random.randint(1, 5)
    sale_date = start_date + timedelta(days=random.randint(0, 550))

    sales_data.append({
        'transaction_id': i,
        'customer_id': customer_id,
        'product_id': product_id,
        'units_sold': units_sold,
        'transaction_date': sale_date.strftime('%Y-%m-%d')
    })
sales_df = pd.DataFrame(sales_data)
sales_df.to_csv('sales.csv', index=False)
print("sales.csv created.")