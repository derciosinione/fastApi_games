from pymongo import MongoClient
from Api.Config.settings import Settings

settings = Settings()
MongoClient = MongoClient(settings.mongo_url)
db = MongoClient.WbSystemDB;