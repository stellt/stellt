-- You can use this later to set up PostgreSQL
-- Example table for users and messages

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    character_name VARCHAR(100),
    message TEXT,
    sender VARCHAR(10),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
