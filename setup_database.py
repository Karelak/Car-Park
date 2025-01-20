import sqlite3
import os

def setup_database():
    db_path = os.path.join(os.path.dirname(__file__), 'car_park.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create vehicles table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        make TEXT NOT NULL,
        model TEXT NOT NULL,
        registration TEXT UNIQUE NOT NULL
    )
    ''')

    # Create permits table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS permits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        vehicle_id INTEGER NOT NULL,
        permit_type INTEGER NOT NULL,  -- 1: Staff, 2: Student, 3: Visitor
        FOREIGN KEY (vehicle_id) REFERENCES vehicles (id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database created successfully")
