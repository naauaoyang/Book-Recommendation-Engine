# This program is designed to transform neighbors file and userId file to Vertices and Edges csv file for System G

import pandas as pd
import numpy as np


userId = pd.read_csv('/Users/mac/Downloads/userId.csv',header=None)
userId.columns=['userId']

userId_dict = dict()
userId_list = []
i = 0
for Id in userId['userId']:
    if Id not in userId_dict:
        userId_dict[Id] = i
        i += 1


Vertices = pd.DataFrame(list(userId_dict.items()), columns=['userId', 'NumIndex'])
Vertices[['NumIndex', 'userId']].to_csv('/Users/mac/Desktop/ColumbiaMSOR/2016fall/EE BigData/Project/SystemGVertices.csv',index=False)


i = 0
edgeFile = open('/Users/mac/Desktop/ColumbiaMSOR/2016fall/EE BigData/Project/SystemGEdges.csv',"a")
tempList = []
with open('/Users/mac/Desktop/ColumbiaMSOR/2016fall/EE BigData/Project/userneighborhood.csv') as infile:
    for line in infile:
        try:
            pairs = line.split(',')
            for point in pairs:
                if point!='\n' and point!='':
                    #edgeFile.writelines(str(i)+','+point+'\n')
                    tempList.append(int(i))
                    tempList.append(int(point))


        except:
            None
        i += 1

Vertices[Vertices['NumIndex'].isin(list(set(tempList)))][['NumIndex', 'userId']].to_csv('/Users/mac/Desktop/ColumbiaMSOR/2016fall/EE BigData/Project/SystemGVertices_1.csv',index=False)






