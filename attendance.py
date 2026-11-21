import sqlite3

def create_attendance_table():
    conn = sqlite3.connect("synapse.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_number TEXT,
            entry_time TEXT,
            exit_time TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_attendance_table()
    print("Attendance table created successfully!")