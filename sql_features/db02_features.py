"""
db02_features.py
Create a table with product features and populate it.
"""

import sqlite3

# Connect to your database (adjust the path if needed)
conn = sqlite3.connect("data/my_database.db")
cursor = conn.cursor()

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS product_features;")

# Create a new table for product features
cursor.execute("""
CREATE TABLE product_features (
    product_id INTEGER PRIMARY KEY,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    rating REAL,
    stock INTEGER
);
""")

# Insert some sample data
products = [
    (1, "Electronics", 499.99, 4.5, 100),
    (2, "Electronics", 299.99, 4.2, 50),
    (3, "Home", 89.99, 3.9, 200),
    (4, "Fashion", 59.99, 4.0, 150),
    (5, "Fashion", 109.99, 4.7, 75)
]

cursor.executemany("INSERT INTO product_features VALUES (?, ?, ?, ?, ?);", products)

# Commit and close
conn.commit()
conn.close()

print("Table 'product_features' created and populated.")
