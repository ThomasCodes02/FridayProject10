import sqlite3

# Replace 'your_database.db' with the path to your .db file
db_file = 'feedback.db'

# Connect to the database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Query to get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

# Optional: Read data from each table
for table in tables:
    table_name = table[0]
    print(f"\nData from table '{table_name}':")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Close the connection
conn.close()
