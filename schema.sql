-- Bank Management System Database Schema
-- SQLite

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'user'
);

-- Accounts table
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    account_number TEXT UNIQUE NOT NULL,
    account_type TEXT NOT NULL,
    balance REAL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
);

-- Default admin account
INSERT INTO users (name, username, password, role) VALUES ('Administrator', 'admin', 'admin123', 'admin');

-- Sample test user
INSERT INTO users (name, username, password, role) VALUES ('John Doe', 'john', 'john123', 'user');
INSERT INTO accounts (user_id, account_number, account_type, balance) VALUES (2, '1234567890', 'Savings', 5000);
INSERT INTO transactions (account_id, type, amount, date) VALUES (1, 'Deposit', 5000, '2024-01-10 10:00:00');
