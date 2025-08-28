import pandas as pd

try:
    df = pd.read_parquet('inventory.parquet')
    print("Success! The local Parquet file is valid.")
    print(df.head())
except Exception as e:
    print(f"Error: The local file is corrupted or invalid. \nDetails: {e}")