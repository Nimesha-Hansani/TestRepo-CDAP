from github  import Github
import urllib.request
import requests
import datetime
import os
import glob
import pymongo
import re
import keyword
from pymongo import MongoClient
from pymongo import InsertOne
import datetime
import sys
import os, os.path

username = "nimeshaamarasingha@gmail.com"
password = "19950525hansani"
repo ="Nimesha-Hansani/TestRepo-CDAP"
g = Github(username,password)

repository=g.get_repo(repo)
branches=repository.get_branches()
for br in branches:

    Branch=br.name
    headCommit=br.commit.sha
    commits = repository.get_commits(headCommit)

    for com in commits:

            #CommitTime
            commitDateTime = com.commit.author.date
            print(commitDateTime)

            TimeStampStr= commitDateTime.strftime("%Y-%m-%d %H-%M-%S")
            Date = TimeStampStr.split(' ')
            commitKey = com.sha
            tree=repository.get_git_tree(com.sha).tree

            for tr in tree:
                
                try:
                    
                    if(tr.type == "tree"):
                        print(tr.type)
                        treeContent=repository.get_contents(tr.path)
                        while len(treeContent)> 0:
                            file_content=treeContent.pop(0)
                            print(file_content.type)

                            if file_content.type =="dir":
                                treeContent.extend(repository.get_contents(file_content.path))
                            else:
                                print(file_content.path)
                
                except :
                    pass 