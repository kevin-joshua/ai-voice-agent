import sqlite3
from datetime import datetime

class CallLogger:
    def __init__(self):
        self.conn = sqlite3.connect("calls.db")
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS calls (
                call_id TEXT PRIMARY KEY,
                from_number TEXT,
                transcript TEXT,
                intent TEXT,
                language TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    async def log_call(self, call_id, from_number, transcript, intent, language):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO calls (call_id, from_number, transcript, intent, language)
            VALUES (?, ?, ?, ?, ?)
        """, (call_id, from_number, transcript, intent, language))
        self.conn.commit()
