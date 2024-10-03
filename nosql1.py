from pymongo import MongoClient
from faker import Faker

# Initialize the Faker object
fake = Faker()

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Adjust if needed
db = client['learn']  # Replace with your database name
collection = db['data_engineering']  # Replace with your collection name

# Create a list of fake documents
actions = [
    {
        "name": fake.name(),
        "street": fake.street_address(),
        "city": fake.city(),
        "zip": fake.zipcode()
    }
    for _ in range(1000)  # Generate 1000 fake users
]

# Insert multiple documents into the collection
result = collection.insert_many(actions)

# Print the number of successfully indexed documents
print(f'Successfully inserted {len(result.inserted_ids)} documents.')
