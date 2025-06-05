DROP TABLE IF EXISTS authors;
CREATE TABLE IF NOT EXISTS authors (
    author_id TEXT PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);

DROP TABLE IF EXISTS books;
CREATE TABLE IF NOT EXISTS books (
    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
-- Create the issues table
CREATE TABLE IF NOT EXISTS issues (
    issue_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT,
    status TEXT
);

-- Create the analyzing table
CREATE TABLE IF NOT EXISTS analyzing (
    analysis_id TEXT PRIMARY KEY,
    issue_id TEXT,
    analyst TEXT,
    summary TEXT,
    date_analyzed TEXT,
    FOREIGN KEY (issue_id) REFERENCES issues(issue_id)
);


