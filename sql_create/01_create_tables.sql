-- Create authors table
CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);

-- Create books table
CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    year_published INTEGER,
    author_id TEXT NOT NULL,
    is_favorite INTEGER DEFAULT 0,
    FOREIGN KEY (author_id) REFERENCES authors (author_id)
);
