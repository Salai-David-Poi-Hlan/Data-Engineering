from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Adjust if needed
db = client['learn']  # Replace with your database name
collection = db['data_engineering']  # Replace with your collection name

# Define batch size
batch_size = 500
total_documents = collection.count_documents({})  # Total document count

# Loop through the documents in batches
for skip in range(0, total_documents, batch_size):
    # Create a new cursor for each batch
    docs = collection.find({}).skip(skip).limit(batch_size)  # Get the next batch
    for doc in docs:
        print(doc)  # Process each document as needed
