import sqlite3

DATABASE = 'database.db'  # SQLite database file path

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

    # Create topics table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS topics
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL)
                 ''')

    # Create posts table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 content TEXT NOT NULL,
                 topic_id INTEGER NOT NULL,
                 FOREIGN KEY (topic_id) REFERENCES topics (id))
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

def add_topic(name):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Check if the topic already exists in the database
    c.execute("SELECT name FROM topics WHERE name=?", (name,))
    existing_topic = c.fetchone()

    if existing_topic:
        # Topic already exists, do not add it again
        conn.close()
        return False

    # Insert topic into the topics table
    c.execute("INSERT INTO topics (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    return True


def add_post(content, topic_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Insert post into the posts table
    c.execute("INSERT INTO posts (content, topic_id) VALUES (?, ?)",
              (content, topic_id))

    conn.commit()
    conn.close()

def get_all_topics():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Retrieve all topics from the topics table
    c.execute("SELECT * FROM topics")
    topics = c.fetchall()

    conn.close()

    return topics

def get_all_posts():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Retrieve all posts with their associated topics from the posts and topics tables
    c.execute("SELECT DISTINCT p.*, t.name FROM topics t LEFT JOIN posts p ON t.id = p.topic_id")
    posts = c.fetchall()

    conn.close()

    return posts


def get_topic_id(topic):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Retrieve topic ID by topic name from the topics table
    c.execute("SELECT id FROM topics WHERE name=?", (topic,))
    topic_id = c.fetchone()

    conn.close()

    return topic_id[0] if topic_id else None