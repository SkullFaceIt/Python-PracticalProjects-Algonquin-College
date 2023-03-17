from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://SebastienRamsay:{password}@mallshopdb.jn1kwwg.mongodb.net/?retryWrites=true&w=majority"

def connect():
    client = MongoClient(connection_string)
    return client