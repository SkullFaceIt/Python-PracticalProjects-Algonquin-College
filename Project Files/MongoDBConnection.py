from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
load_dotenv(find_dotenv())

class MongoDBConnection:
    """Creates and holds the database connection"""

    # Singleton instance
    __instance = None

    def __init__(self):
        """Private constructor"""
        if MongoDBConnection.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            # get the password from .env
            password = os.environ.get("MONGODB_PWD")

            # make connection string
            connection_string = f"mongodb+srv://SebastienRamsay:{password}@mallshopdb.jn1kwwg.mongodb.net/?retryWrites=true&w=majority"

            # connect the mongoclient
            self.client = MongoClient(connection_string, tlsAllowInvalidCertificates=True)

            # list of databases available
            self.databases = self.client.list_database_names()
            
             # list of collections avalible
            self.collections = self.client.Practical_Project_Part_3.list_collection_names()

            # connection to the proper database and collection
            self.db = self.client.Practical_Project_Part_3.Potato_Info

            MongoDBConnection.__instance = self

    @staticmethod
    def get_instance():
        """Static method to fetch the instance of the class"""
        if MongoDBConnection.__instance is None:
            MongoDBConnection()
        return MongoDBConnection.__instance
