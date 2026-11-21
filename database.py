import sqlite3

def create_database():
    conn = sqlite3.connect("synapse.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_number TEXT UNIQUE,
            student_name TEXT
        )
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO students (roll_number, student_name)
        VALUES (?, ?)
    """, ("STU001", "Rahul"))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Student added successfully!")