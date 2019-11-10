import os
import glob
import pymongo
import re
import keyword
from pymongo import MongoClient
from bson.json_util import dumps, loads


connection = MongoClient('localhost',27017)
Database = connection.gCodexDB
data =Database.LinesOfCode

dataList =dumps(data.find())

print(dataList)
