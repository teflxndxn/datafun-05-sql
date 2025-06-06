import sqlite3
import csv
import pandas as pd

# === File paths ===
db_path = 'data/project.sqlite3'
authors_csv = 'project_data/authors.csv'
books_csv = 'project_data/books.csv'
issues_raw_csv = 'project_data/issues.csv'          # Updated path
issues_fixed_csv = 'project_data/issues_fixed.csv'
analyzing_fixed_csv = 'project_data/analyzing_fixed.csv'

# === Connect to SQLite ===
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# === Insert authors ===
def insert_authors():
    with open(authors_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute(
                "INSERT OR IGNORE INTO authors (author_id, first, last) VALUES (?, ?, ?)",
                (row['author_id'], row['first'], row['last'])
            )
    conn.commit()

# === Insert books ===
def insert_books():
    with open(books_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute(
                "INSERT OR IGNORE INTO books (book_id, title, year_published, author_id) VALUES (?, ?, ?, ?)",
                (row['book_id'], row['title'], row['year_published'], row['author_id'])
            )
    conn.commit()

# === Process and insert issues and analyzing ===
def insert_issues_and_analyzing():
    with open(issues_raw_csv, newline='') as csvfile, \
         open(issues_fixed_csv, 'w', newline='') as issues_outfile, \
         open(analyzing_fixed_csv, 'w', newline='') as analyzing_outfile:

        reader = csv.reader(csvfile, delimiter='\t')
        issues_writer = csv.writer(issues_outfile)
        analyzing_writer = csv.writer(analyzing_outfile)

        # Headers
        issues_writer.writerow(['issue_id', 'title', 'category', 'status'])
        analyzing_writer.writerow(['analysis_id', 'issue_id', 'analyst', 'summary', 'date_analyzed'])

        for row in reader:
            if len(row) < 6:
                continue  # Skip invalid rows

            analysis_id = row[0]
            issue_id = row[1]
            method = row[2]
            title_or_summary = row[3]
            resolution_or_status = row[4]
            date_analyzed = row[5]

            category = "Bug" if method.lower() == "5 whys" else "Enhancement"
            status = resolution_or_status
            analyst = "Unknown"

            issues_writer.writerow([issue_id, title_or_summary, category, status])
            analyzing_writer.writerow([analysis_id, issue_id, analyst, title_or_summary, date_analyzed])

    # Load fixed data into SQLite
    df_issues = pd.read_csv(issues_fixed_csv)
    df_issues.to_sql("issues", conn, if_exists="append", index=False)
    print("Inserted issues.")

    df_analyzing = pd.read_csv(analyzing_fixed_csv)
    df_analyzing.to_sql("analyzing", conn, if_exists="append", index=False)
    print("Inserted analyzing.")

# === Run all insertions ===
insert_authors()
insert_books()
insert_issues_and_analyzing()

# === Close connection ===
conn.close()
print("All data loaded successfully.")
