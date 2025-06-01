# sql_utils.py

import sqlite3
import pandas as pd

def query_product_features():
    """
    Connect to the database and return the product_features table as a DataFrame.
    """
    conn = sqlite3.connect("data/my_database.db")
    query = "SELECT * FROM product_features;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
