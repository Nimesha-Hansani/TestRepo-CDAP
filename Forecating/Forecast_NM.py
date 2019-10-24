import os
import glob
import pymongo
import re
import keyword
from pymongo import MongoClient
from pymongo import InsertOne
import datetime
import pandas as pd 

connection = MongoClient('localhost',27017)
Database = connection.gCodexDB
data =Database.LinesOfCode
dataList =data.find()
New_df = pd.DataFrame() #Temporary empty dataframe

for data in dataList:

    print(data)