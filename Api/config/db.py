from pymongo import MongoClient
from os import getenv

conn = MongoClient(getenv('MongoUrl'))