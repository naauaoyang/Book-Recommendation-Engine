# This program is aimed at sorting book ratings

bookDict = {}
with open("/Users/mac/Downloads/ratings_Books.csv") as infile:
    for line in infile:
        lineList = line.split(',')
        if lineList[1] in bookDict:
            bookDict[lineList[1]].append(float(lineList[2]))
        else:
            bookDict[lineList[1]]=[float(lineList[2])]        
#print(bookDict)
avgDict = {}
for k,v in bookDict.items():
    avgDict[k] = [sum(v)/ float(len(v)), len(v)]
#print (list(avgDict.values()[0]))
import operator
sorted_avgDict = sorted(avgDict.items(), key=operator.itemgetter(1),reverse=True)
#print (sorted_avgDict)

"""
import matplotlib.pyplot as plt

plt.hist(list(avgDict.values()))
plt.title("Distribution for Avg. Ratings of Amazon Book Dataset")
plt.xlabel("Rating")
plt.ylabel("Amount")
plt.show()
"""
import pickle
#print(sorted_avgDict)
with open("/Users/mac/Desktop/ColumbiaMSOR/2016fall/EE BigData/Project/sorted_avgDict.txt",'wb') as outfile:
    #outfile.write(sorted_avgDict)
    pickle.dump(sorted_avgDict, outfile)

