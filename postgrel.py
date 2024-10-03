import psycopg2 as db
from faker import Faker

fake = Faker()
data = []
i = 2

# Generate 1000 fake user records
for r in range(1000):
    data.append((i, fake.name(), fake.street_address(), fake.city(), fake.zipcode()))
    i += 1

# Connect to the database
conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='zxcrty'"
conn = db.connect(conn_string)
cur = conn.cursor()

# Prepare the insert query
query = "INSERT INTO users (id, name, street, city, zip) VALUES (%s, %s, %s, %s, %s)"

# Print a sample of the query with data
print(cur.mogrify(query, data[0]))

# Execute the insertions
cur.executemany(query, data)

# Commit the changes to the database
conn.commit()

# Clean up
cur.close()
conn.close()

print("Data inserted successfully!")
