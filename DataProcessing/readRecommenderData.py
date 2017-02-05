# Transform Mahout recommendation results to json file with string book Id

import pandas as pd
import numpy as np
import re

outfile = open("/Users/mac/Desktop/ColumbiaMSOR/2016fall/EE BigData/Project/Euclidean_Recommendation.json", "a")

userId = pd.read_csv('/Users/mac/Downloads/userId.csv',header=None)
userId.columns=['userId']

userId_dict = dict()
userId_list = [0]
i = 1
for Id in userId['userId']:
    if Id not in userId_dict:
        userId_dict[Id] = i
        userId_list.append(Id)
    i += 1

bookId = pd.read_csv('/Users/mac/Downloads/bookId.csv',header=None)
bookId.columns=['bookId']

bookId_dict = dict()
bookId_list = [0]
i = 1
for Id in bookId['bookId']:
    if Id not in bookId_dict:
        bookId_dict[Id] = i
        bookId_list.append(Id)
    i += 1


with open('/Users/mac/Downloads/euclidean_result') as infile:
    outfile.writelines('{')
    for line in infile:
        wordList = re.split('\t|\n',line)
        userId = userId_list[int(wordList[0])]
        recommendation = wordList[1][1:-1].split(',')
        userDict = {}
        for recomBook in recommendation:
            recomBooklist = recomBook.split(':')
            bookId = bookId_list[int(recomBooklist[0])]
            bookRating = float(recomBooklist[1])
            userDict[bookId] = bookRating
        outfile.writelines("'"+str(userId)+"':"+str(userDict)+',\n')
    outfile.writelines('}')


outfile.close()
            
