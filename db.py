# Package Imports
from pymongo import MongoClient
from bson.objectid import ObjectId

# File Imports
import config


class MongoDB:
  def __init__(self) -> None:
    client = MongoClient(config.MONGODB_CONNECTION_STRING)
    self.mongo_client = client
    self.db = client[config.MONGODB_DB_NAME]
  
  def get_collection(self, collection_name):
    return self.db[collection_name]
  
  def insert_one(self, record, collection_name = config.MONGODB_COLLECTION_NAME):
    collection = self.get_collection(collection_name=collection_name)
    record_inserted = collection.insert_one(record)
    
    return record_inserted
  
  def update_one_by_id(self, id, upsert_data, collection_name = config.MONGODB_COLLECTION_NAME):
    try:
      collection = self.get_collection(collection_name=collection_name)
      collection.update_one({"_id": ObjectId(id)}, {"$set": upsert_data})
    except Exception as e:
      print(f"An error occured while updating DB: {e}")
