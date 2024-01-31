from pymongo import MongoClient

uri = "mongodb+srv://mongo1:EQw3tHnTTRzZW6PR@cluster0.xtixkkf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.textenger_db

collection = db.textenger_collection