-- Create the users table if it doesn't already exist
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Adds a unique ID for each user
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    preferred_os TEXT NOT NULL
);

-- Insert random user data into the users table
INSERT INTO users (name, email, preferred_os) VALUES ('Alice Johnson', 'alice.johnson@example.com', 'Linux');
INSERT INTO users (name, email, preferred_os) VALUES ('Bob Smith', 'bob.smith@example.com', 'Windows');
INSERT INTO users (name, email, preferred_os) VALUES ('Charlie Davis', 'charlie.davis@example.com', 'macOS');
INSERT INTO users (name, email, preferred_os) VALUES ('Diana Green', 'diana.green@example.com', 'Linux');
INSERT INTO users (name, email, preferred_os) VALUES ('Eve Thompson', 'eve.thompson@example.com', 'Windows');