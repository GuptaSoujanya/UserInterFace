from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


client= MongoClient("mongodb+srv://root:root@cluster0.27da0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", server_api=ServerApi('1'))

db = client.Grt_db

collection_name = db["Grt_collection"]