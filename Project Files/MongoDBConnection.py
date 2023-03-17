import pymongo
from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, URI='mongodb+srv://rams0130:CfWJPf8FtDoyKdKh@mallshop.8p5p5d8.mongodb.net/?retryWrites=true&w=majority'):
        self.URI = URI
        self.client = None

    def __enter__(self):
        self.client = MongoClient(self.URI)
        return self.client
