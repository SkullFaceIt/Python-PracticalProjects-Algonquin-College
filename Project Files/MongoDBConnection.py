from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
load_dotenv(find_dotenv())



    
password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://SebastienRamsay:{password}@mallshopdb.jn1kwwg.mongodb.net/?retryWrites=true&w=majority"
    
client = MongoClient(connection_string, tlsAllowInvalidCertificates=True)
    
databases = client.list_database_names()
    
collections = client.Practical_Project_Part_3.list_collection_names()

db = client.Practical_Project_Part_3.Potato_Info