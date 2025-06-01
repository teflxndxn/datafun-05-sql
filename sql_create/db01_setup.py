"""
db01_setup.py - Run SQL scripts to create and populate a database.
"""

import sqlite3
from pathlib import Path

# Set path to database file
db_path = Path("data.db")

# Set path to folder with SQL files
sql_path = Path(".")


# List of SQL files to run in order
sql_files = [
    "01_drop_tables.sql",
    "02_create_tables.sql",
    "03_insert_records.sql"
]

# Connect to SQLite database (will create data.db if it doesn't exist)
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()

    for file_name in sql_files:
        file_path = sql_path / file_name
        print(f"Running {file_name}...")

        # Read and execute SQL script
        sql_script = file_path.read_text()
        cursor.executescript(sql_script)

    print("Database setup complete.")
