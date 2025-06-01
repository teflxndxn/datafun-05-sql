import sqlite3
import csv
import os

DB_PATH = "data/my_database.db"
AUTHORS_CSV = "data/authors.csv"
BOOKS_CSV = "data/books.csv"

def create_tables(conn):
    cur = conn.cursor()
    # Create authors table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            author_id TEXT PRIMARY KEY,
            first TEXT NOT NULL,
            last TEXT NOT NULL
        )
    """)
    # Create books table with is_favorite defaulting to 0 (False)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            year_published INTEGER,
            author_id TEXT NOT NULL,
            is_favorite INTEGER DEFAULT 0,
            FOREIGN KEY (author_id) REFERENCES authors (author_id)
        )
    """)
    conn.commit()

def insert_authors(conn):
    cur = conn.cursor()
    with open(AUTHORS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        authors = [(row['author_id'], row['first'], row['last']) for row in reader]
    cur.executemany("INSERT OR IGNORE INTO authors (author_id, first, last) VALUES (?, ?, ?)", authors)
    conn.commit()

def insert_books(conn):
    cur = conn.cursor()
    with open(BOOKS_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        books = []
        for row in reader:
            # Insert is_favorite as 0 by default
            books.append((row['book_id'], row['title'], int(row['year_published']), row['author_id'], 0))
    cur.executemany(
        "INSERT OR IGNORE INTO books (book_id, title, year_published, author_id, is_favorite) VALUES (?, ?, ?, ?, ?)",
        books
    )
    conn.commit()

def display_books_with_authors(conn):
    cur = conn.cursor()
    query = """
        SELECT b.book_id, b.title, b.year_published, a.first, a.last, b.is_favorite
        FROM books b
        JOIN authors a ON b.author_id = a.author_id
        ORDER BY b.year_published
    """
    cur.execute(query)
    rows = cur.fetchall()
    print("\nBooks with Authors (and is_favorite):\n")
    for book_id, title, year, first, last, is_fav in rows:
        fav_status = "Yes" if is_fav else "No"
        print(f"{title} ({year}) by {first} {last} — Favorite? {fav_status}")

def main():
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    # Connect to SQLite DB
    conn = sqlite3.connect(DB_PATH)
    print(f"Connected to database {DB_PATH}")

    create_tables(conn)
    print("Tables created or verified.")

    insert_authors(conn)
    print("Authors inserted.")

    insert_books(conn)
    print("Books inserted.")

    display_books_with_authors(conn)

    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()
