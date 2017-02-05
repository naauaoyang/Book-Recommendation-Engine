# The program is aimed at transforming string user/book Id to int to fit in data format of Mahout recommendation tools

import pandas as pd
import numpy as np

# Import processed data of Amazon Rating dataset
userId = pd.read_csv('/Users/mac/Downloads/userId.csv',header=None)
bookId = pd.read_csv('/Users/mac/Downloads/bookId.csv',header=None)
rating = pd.read_csv('/Users/mac/Downloads/rating_only.csv',header=None)

userId.columns=['userId']
bookId.columns=['bookId']
rating.columns=['rating']

print(len(userId))
print(len(bookId))

userId_dict = dict()
userId_list = []
i = 1
for Id in userId['userId']:
    if Id not in userId_dict:
        userId_dict[Id] = i
        userId_list.append(i)
        i += 1
    else:
        userId_list.append(userId_dict[Id])

print(len(userId_list))
print(len(userId_dict))

bookId_dict = dict()
bookId_list = []
i = 1
for Id in bookId['bookId']:
    if Id not in bookId_dict:
        bookId_dict[Id] = i
        bookId_list.append(i)
        i += 1
    else:
        bookId_list.append(bookId_dict[Id])

print(len(bookId_list))
print(len(bookId_dict))

a = pd.DataFrame(userId_list)
a.columns=['userId']
a.to_csv('userIdNum.csv', index=False)

b = pd.DataFrame(bookId_list)
b.columns=['bookId']
b.to_csv('bookIdNum.csv', index=False)

rating.to_csv('ratingNum.csv', index=False)

np.save('userId_dict.npy', userId_dict) 
np.save('bookId_dict.npy', bookId_dict) 


