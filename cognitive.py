import os
import glob
import pymongo
import re
import keyword
from pymongo import MongoClient
from pymongo import InsertOne
import datetime


file_Path = 'D:\SLIIT EDU\Year 4 Semester 2\CDAP\Documents\QTest.cs'

#Function for Calculate Cognitive Weight
def CalculateCognitiveWeight(line):
    
    cognitiveWeight = 0.0
    res = re.findall(r'[a-zA-Z]+', line)

    for w in res:
      if (w == "if") or  (w == "elif") or (w == "elseif") or (w == "else") or  (w=="then") or (w == "case"):
        cognitiveWeight = cognitiveWeight + 2
      elif (w == "for") or (w == "while") or (w == "do") or (w == "repeat") or (w == "until"):
        cognitiveWeight = cognitiveWeight + 3 
      elif (w == "continue"):
        cognitiveWeight = cognitiveWeight + 1

    return cognitiveWeight

#Function For Calculate Arithmetic operators
def CalculateArithmeticOperartors1(line):
    
    c1 = 0
    if '+' in line:
        c1= c1 + 1
    if '-' in line:
        c1 = c1 + 1
    if '*' in line:
        c1 = c1 + 1
    if '/'in line:
        c1 = c1 + 1
    if '%' in line:
        c1 = c1 + 1
    if '++' in line:
        c1 = c1 + 1
    if '+=' in line:
        c1 = c1 + 1
    if '-=' in line:
        c1 = c1 + 1
    if '*-' in line:
        c1 = c1 + 1    
    if '/=' in line:
        c1 = c1 + 1
    if '%=' in line:
        c1 = c1 + 1
    if '--' in line:
         c1 = c1 + 1
    if  '=' in line:
        c1 = c1 + 1

    print(c1)  
    return c1

def CalculateArithmeticOperartors2(line):
    
    c1 = 0
    if '+' in line:
        c1= c1 + 1
    if '-' in line:
        c1 = c1 + 1
    if '*' in line:
        c1 = c1 + 1
    if '/'in line:
        c1 = c1 + 1
    if '%' in line:
        c1 = c1 + 1
    if '++' in line:
        c1 = c1 + 1
    if '+=' in line:
        c1 = c1 + 1
    if '-=' in line:
        c1 = c1 + 1
    if '*-' in line:
        c1 = c1 + 1    
    if '/=' in line:
        c1 = c1 + 1
    if '%=' in line:
        c1 = c1 + 1
    if '--' in line:
         c1 = c1 + 1
    if  '=' in line:
        c1 = c1 + 1

    print(c1)  
    return c1
#Calculate Logical Operators 

def CalculateLogicalOperators(line):
    c2 = 0.0
    if '!' in line:
      c2 = c2 + 1
    if '!=' in line:
      c2 = c2 + 1
    if '<' in line:
      c2 = c2 + 1
    if '<=' in line:
      c2 = c2 + 1
    if '>' in line :
       c2 = c2 + 1
    if '>=' in line:
       c2 = c2 + 1
    if '&&' in line:
       c2 = c2 + 1
    if '||' in line:
        c2 = c2 + 1
    if '==' in line:
        c2 = c2 + 1
    if 'or' in line:
        c2 = c2 + 1
    if 'and' in line:
        c2 = c2 + 1
  
    return c2    


#Function for Calculate Identifier
def countIdentifiers(filePath):
    DistinctWords = 0
    with open(filePath, 'r') as filehandle:
        Identifiers=0
        filecontent = filehandle.readlines()
        wordList = []
        for line in filecontent:
          
           
            commonkeywords=['for' ,'do','while','if','else','elseif','elif','switch','case','continue','pass','try','catch',
                        'continue','int','double','float','finally' ,'from','return','null']
            keywords1 = keyword.kwlist
            keywordsJava= ['import' ,'from','abstract','boolean','break','byte','case','catch','char','class','continue','default','final','private',
                        'protected','throws','void']
            keywordJavaScript = ['react', 'extends','export']
            #keywordC=[]
            res = re.findall(r'[a-zA-Z]+', line)
            
            for w in res:
                if (w not in keywords1) and (w not in keywordsJava) and (w not in commonkeywords) and (w not in keywordJavaScript):
                    wordList.append(w)
                    
                Identifiers = set (wordList)
                    
                 
       
       
        return len(Identifiers)


def CalculateCognitiveMetricValue(filePath):
    LinesOfCode= 0
    TotalDistinctIdentifiers = countIdentifiers(filePath)
    TotalCognitiveWeight = 0
    
    with open(filePath, 'r') as filehandle:
        
        filecontent = filehandle.readlines()
        
        WordContent = str(filecontent)
        SplittedWord = WordContent.split(' ')
        charlist = list(WordContent)
        
        TotalDistinctOperators =CalculateArithmeticOperartors1(SplittedWord) + CalculateLogicalOperators(SplittedWord) + CalculateArithmeticOperartors2(charlist)
        
        for line in filecontent:
            CalculateCognitiveWeight(line)
            TotalCognitiveWeight = TotalCognitiveWeight + CalculateCognitiveWeight(line)
            if line.strip():
               LinesOfCode = LinesOfCode + 1
    
    FinalValue = (TotalCognitiveWeight + TotalDistinctIdentifiers + TotalDistinctOperators)/ LinesOfCode
    print("LinesOfCode"+ str(LinesOfCode))
    
    return [FinalValue ,TotalCognitiveWeight ,TotalDistinctIdentifiers , TotalDistinctOperators ]


if os.path.isfile(file_Path):
      x =CalculateCognitiveMetricValue(file_Path)
      print(x)
else:

    print("Not a file")