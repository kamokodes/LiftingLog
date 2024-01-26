# lifting_app_backend.py

import sqlite3
from datetime import datetime

DATABASE_FILE = 'lifting_app.db'

def create_tables():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise TEXT NOT NULL,
            weight REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

def record_lift(exercise, weight):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO lifts (exercise, weight, timestamp)
        VALUES (?, ?, ?)
    ''', (exercise, weight, timestamp))

    connection.commit()
    connection.close()

def get_lift_history():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM lifts ORDER BY timestamp DESC
    ''')

    history = cursor.fetchall()

    connection.close()

    return history
