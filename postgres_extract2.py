import psycopg2 as db
import pandas as pd

# Connection string
conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='zxcrty'"

# Connect to the PostgreSQL database
conn = db.connect(conn_string)

# Read data from the users table into a DataFrame
df = pd.read_sql("SELECT * FROM users", conn)

# Convert DataFrame to JSON format
json_data = df.to_json(orient='records')

# Optionally, print the JSON data
print(json_data)

# Clean up
conn.close()
