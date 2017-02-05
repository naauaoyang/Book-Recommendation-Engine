import json
import operator

with open('/Users/mac/Desktop/ColumbiaMSOR/2016fall/EE BigData/Project/User_Neighboor.json') as data_file:  
    User_Neighboor = json.load(data_file)

userDegreeDict = dict()

for key, value in User_Neighboor.items():
    if key in userDegreeDict:
        userDegreeDict[key] += 1
    else:
        userDegreeDict[key] = 1
    for uid in value:
        if uid in userDegreeDict:
            userDegreeDict[uid] += 1
        else:
            userDegreeDict[uid] = 1


sorted_userDegreeDict = sorted(userDegreeDict.items(), key=operator.itemgetter(1), reverse=True)
with open('sorted_userDegreeDict.txt', 'w') as outfile:
    json.dump(sorted_userDegreeDict, outfile)

outfile.close()