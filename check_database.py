import sqlite3

conn = sqlite3.connect('user_data.db') 
cursor = conn.cursor()

# Query the database to include the eligibility column
cursor.execute("SELECT * FROM user_input")
rows = cursor.fetchall()

# Print the results with the new eligibility column
for row in rows:
    print(row)

conn.close()
