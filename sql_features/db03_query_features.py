# sql_features/db03_query_features.py

"""
Query the product_features table and display results.
"""

import sqlite3
import pandas as pd

# Step 1: Connect to the database
conn = sqlite3.connect("data/my_database.db")

# Step 2: Define the SQL query
query = "SELECT * FROM product_features;"

# Step 3: Read results into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Display the results
print("\n Here are the product features:")
print(df)

# Step 5: Close the connection
conn.close()
