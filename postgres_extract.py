import psycopg2 as db

# Connect to the PostgreSQL database
conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='zxcrty'"
conn = db.connect(conn_string)
cur = conn.cursor()

# Query to select all records from the users table
query = "SELECT * FROM users"
cur.execute(query)

# Print all records in the users table
for record in cur:
    print(record)

# Fetch all records (this will consume the cursor, so be careful with subsequent fetches)
all_records = cur.fetchall()  # Store all records if needed later

# Example of fetching specific numbers of records
cur.execute(query)  # Re-execute the query to reset the cursor
records_500 = cur.fetchmany(500)  # Fetch 500 records
print(f"Fetched {len(records_500)} records.")

# Fetch one additional record
one_record = cur.fetchone()
if one_record:
    print(one_record[0])  # Print the first field of the fetched record

# Print the number of records in the cursor
print(f"Row count: {cur.rowcount}")
print(f"Current row number: {cur.rownumber}")

# Export data to CSV
with open('fromdb.csv', 'w') as f:
    cur.copy_to(f, 'users', sep=',')
print("Data exported to fromdb.csv.")

# Read the contents of the CSV file
with open('fromdb.csv', 'r') as f:
    content = f.read()
    print(content)

# Clean up
cur.close()
conn.close()
