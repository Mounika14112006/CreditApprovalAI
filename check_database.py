import sqlite3

conn = sqlite3.connect('user_data.db') 
cursor = conn.cursor()

cursor.execute("SELECT * FROM user_input")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
