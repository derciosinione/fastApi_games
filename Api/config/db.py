from pymongo import MongoClient
from os import getenv

MongoClient = MongoClient(getenv('MongoUrl'))
db = MongoClient.WbSystemApi;