import sqlite3

# This creates a local file named 'company.db' which acts as our database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create two tables: employees and sales
cursor.execute(
    "CREATE TABLE IF NOT EXISTS employees (id INTEGER, name TEXT, department"
    " TEXT, salary INTEGER);"
)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS sales (sale_id INTEGER, employee_id INTEGER,"
    " amount INTEGER, month TEXT);"
)

# Insert sample dummy data into them
cursor.execute("INSERT INTO employees VALUES (1, 'Alice', 'Sales', 75000);")
cursor.execute("INSERT INTO employees VALUES (2, 'Bob', 'Engineering', 90000);")
cursor.execute("INSERT INTO sales VALUES (101, 1, 5000, 'January');")
cursor.execute("INSERT INTO sales VALUES (102, 1, 8000, 'February');")

conn.commit()
conn.close()
print("Success! Your database 'company.db' has been created.")