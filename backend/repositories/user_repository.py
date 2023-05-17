import sqlite3
from models.user import User
from utils.database import db_connect

class UserRepository:
    @staticmethod
    def create_user(username, password, role):
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                       (username, password, role))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id

    @staticmethod
    def find_user_by_username(username):
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(*row)
        return None