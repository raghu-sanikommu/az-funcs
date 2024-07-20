# Package Imports
from pymongo import MongoClient
from bson.objectid import ObjectId

# File Imports
import config
from logger import logger


class MongoDB:
  def __init__(self) -> None:
    client = MongoClient(config.MONGODB_CONNECTION_STRING)
    self.mongo_client = client
    self.db = client[config.MONGODB_DB_NAME]
    self.collection = self.db[config.MONGODB_COLLECTION_NAME]
  
  def get_collection(self, collection_name):
    return self.db[collection_name]
 
  
  def insert_one(self, record):
    record_inserted = self.collection.insert_one(record)
    
    return record_inserted

  
  def update_one_by_id(self, id, upsert_data):
    try:
      self.collection.update_one({"_id": ObjectId(id)}, {"$set": upsert_data})
    except Exception as e:
      logger.info(f"An error occured while updating DB: {e}")

  
  def find_by_id(self, id):
    return self.collection.find_one({"_id": ObjectId(id)})