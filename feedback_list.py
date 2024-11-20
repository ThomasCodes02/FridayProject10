import sqlite3
import pandas as pd

# Path to your .db file
db_path = "feedback.db"

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# Step 1: Retrieve the list of tables
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Initialize a list to store all data
all_data = []

# Step 2: Loop through each table and fetch data
for table in tables:
    table_name = table[0]
    print(f"Fetching data from table: {table_name}")
    
    # Fetch all data from the table
    df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
    all_data.append({"table_name": table_name, "data": df})

    # Export each table to Excel (optional: you can export all in one file)
    df.to_excel(f"{table_name}.xlsx", index=False)
    print(f"Data from {table_name} exported to {table_name}.xlsx")

# Close the connection
conn.close()

# Step 3: Save all data to a single Excel file with multiple sheets (optional)
with pd.ExcelWriter("all_data.xlsx") as writer:
    for table in all_data:
        table_name = table["table_name"]
        table_data = table["data"]
        table_data.to_excel(writer, sheet_name=table_name, index=False)

print("All data has been exported to all_data.xlsx")
