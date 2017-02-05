# Transform neighbors file with int userId back to String userId

import pandas as pd
import numpy as np
import re

outfile = open("/Users/mac/Desktop/ColumbiaMSOR/2016fall/EE BigData/Project/User_Neighboor.json", "a")
outfile.writelines("{")


userId = pd.read_csv('/Users/mac/Downloads/userId.csv',header=None)
userId.columns=['userId']

userId_dict = dict()
userId_list = []
i = 0
for Id in userId['userId']:
    if Id not in userId_dict:
        userId_dict[Id] = i
        userId_list.append(Id)
    i += 1


j = 0
with open('/Users/mac/Desktop/ColumbiaMSOR/2016fall/EE BigData/Project/userneighborhood.csv') as infile:
    for line in infile:
        userName = userId_list[j]
        userNeighboor = []
        try:
            pairs = line.split(',')
            for point in pairs:
                if point!='\n' and point!='':
                    userNeighboor.append(userId_list[int(point)])
            stringLine = '"'+userName+'":'+str(userNeighboor)+",\n"
            stringLine = stringLine.replace("'",'"')
            outfile.writelines(stringLine)
        except:
            None
        j += 1
outfile.writelines("}")
outfile.close()