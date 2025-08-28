import pandas as pd

inventory_data = {
    'warehouse_id': [1, 1, 1, 2, 2, 2],
    'product_id': [1, 2, 3, 4, 5, 6],
    'stock_level': [150, 200, 80, 120, 300, 95]
}
inventory_df = pd.DataFrame(inventory_data)
inventory_df.to_parquet('inventory.parquet', index=False)
print("inventory.parquet created.")