import pymongo
from pymongo import MongoClient


myclient = MongoClient('localhost',27017)
mydb = myclient["gCodexDB"]
mycol =mydb["LinesOfCode"]






