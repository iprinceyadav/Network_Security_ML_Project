from pymongo.mongo_client import MongoClient
import os
from urllib.parse import quote_plus

username = "iprinceyadav"
password = quote_plus("Admin123")  # encodes @ → %40

uri = os.getenv("MONGO_DB_URL")

# Create a new client and connect to the server
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
