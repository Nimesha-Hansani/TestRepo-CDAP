import os
import glob
import pymongo
import re
import keyword
from pymongo import MongoClient
from pymongo import InsertOne
import datetime




#DB Connection to the cognitive value collection

myclient = MongoClient('localhost',27017)
mydb = myclient["gCodexDB"]
mycol =mydb["cognitiveValues"]



mycol.update_many({"Repository":"Nimesha-Hansani/TestRepo-CDAP",
                         "Branches":{'$elemMatch':{"Branch Name":"master"}}},
                          {'$push':{"Branches.$.Commits":{
                                    "Commit Date":"2019-05-25",
                                    "Commit Time":"18-12-11"
                          }}})