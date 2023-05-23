import sqlite3

DATABASE = 'users.db'  # SQLite database file path

def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Create users table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL,
                 role TEXT NOT NULL)
                 ''')

    conn.commit()
    conn.close()

def add_user(username, password, role):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Insert user into the users table
    c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
              (username, password, role))

    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Retrieve all users from the users table
    c.execute("SELECT * FROM users")
    users = c.fetchall()

    conn.close()

    return users

def get_user_by_username(username):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Retrieve user by username from the users table
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()

    conn.close()

    return user