from pymongo import MongoClient
import pandas as pd
from faker import Faker

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Adjust if needed
db = client['learn']  # Replace with your database name
collection = db['data_engineering']  # Replace with your collection name

# Query to get 10 documents
docs = collection.find().limit(10)
print(list(docs))  # Print the raw documents

# Convert to DataFrame
docs = list(collection.find().limit(10))
df = pd.json_normalize(docs)  # Normalize to a DataFrame
print(df)

# Query for a specific user by name
user_query = {"name": "Lisa Strong"}
user = collection.find_one(user_query)
print(user)

# Alternative query using a regex (to mimic full-text search)
regex_query = {"name": {"$regex": "Lisa Strong", "$options": "i"}}
user_regex = collection.find_one(regex_query)
print(user_regex)

# Query for documents where the city is Jamesberg
city_query = {"city": "South William"}
city_docs = list(collection.find(city_query))
print(city_docs)

