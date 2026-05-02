import sqlite3
from pathlib import Path

DB_PATH = "database/security.db"

def create_connection():
    Path("database").mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn=create_connection()
    cursor=conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            source_ip TEXT NOT NULL,
            event_type TEXT NOT NULL,
            description TEXT NOT NULL,
            severity TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_event(date: str, source_ip: str, event_type: str, description: str, severity: str):
    conn=create_connection()
    cursor=conn.cursor()

    cursor.execute("""
        INSERT INTO events (date, source_ip, event_type, description, severity)
        VALUES (?, ?, ?, ?, ?)
    """, (date, source_ip, event_type, description, severity))

    conn.commit()
    conn.close()


