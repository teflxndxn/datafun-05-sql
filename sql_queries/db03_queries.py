"""
Query the product_features table and display results.
"""

import sqlite3
import pandas as pd

def query_product_features():
    # Step 1: Connect to the SQLite database
    conn = sqlite3.connect("data/my_database.db")

    # Step 2: Define the SQL query to select all records from product_features table
    query = "SELECT * FROM product_features;"

    # Step 3: Execute the query and load the results into a pandas DataFrame
    df = pd.read_sql_query(query, conn)

    # Step 4: Close the connection
    conn.close()

    return df

if __name__ == "__main__":
    df = query_product_features()
    print("\nHere are the product features:")
    print(df)
