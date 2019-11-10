import os
import glob
import pymongo
import re
import keyword
from pymongo import MongoClient
import pandas as pd


connection = MongoClient('localhost',27017)
Database = connection.gCodexDB
data =Database.cognitiveValues

dataList =data.find()
New_df = pd.DataFrame() #Temporary empty dataframe

for data in dataList:

    print(data)