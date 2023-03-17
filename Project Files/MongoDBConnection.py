from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
load_dotenv(find_dotenv())



# get the password from .env
password = os.environ.get("MONGODB_PWD")

# make connection string
connection_string = f"mongodb+srv://SebastienRamsay:{password}@mallshopdb.jn1kwwg.mongodb.net/?retryWrites=true&w=majority"


# connect the mongoclient
client = MongoClient(connection_string, tlsAllowInvalidCertificates=True)


# list of databases avalible
databases = client.list_database_names()
# list of collections avalible
collections = client.Practical_Project_Part_3.list_collection_names()

# connection to the proper database and collection
db = client.Practical_Project_Part_3.Potato_Info