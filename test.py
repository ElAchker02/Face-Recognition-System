import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect("face_recognition.db")
cursor = conn.cursor()

# Test the query
cursor.execute("SELECT * FROM Admins")
rows = cursor.fetchall()

print(rows)
conn.close()
