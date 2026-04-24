import sqlite3


class DBHelper:

    def __init__(self, db_name="customers.db"):
        self.db_name = db_name

    def create_api_users_table(self):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS api_users (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    job TEXT
                )
            """)

            connection.commit()

    def insert_api_user(self, user_id, name, job):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT OR REPLACE INTO api_users (id, name, job)
                VALUES (?, ?, ?)
            """, (user_id, name, job))

            connection.commit()

    def get_api_user_by_id(self, user_id):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()

            cursor.execute("""
                SELECT id, name, job
                FROM api_users
                WHERE id = ?
            """, (user_id,))

            return cursor.fetchone()