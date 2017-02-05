from flask import Flask, render_template, request, json
from ConvertBookIdToBookName import getBookName, getUserName
def generateResultHTML(BookDict, UserList):
    BookList = list(BookDict.keys())
    bookNameDict = dict()
    for bookId in BookList:
        bookLink = "https://www.amazon.com/gp/product/"+bookId
        bookName, bookImageLink = getBookName(bookLink)
        if bookName!='' and ('<!doctype html>' in bookName)!=True:
            bookNameDict[bookName]={"bookRating":BookDict[bookId],"bookImage":bookImageLink,"bookLink":bookLink}
    userNameDict = dict()
    for userId in UserList:
        userLink = "https://www.amazon.com/gp/pdp/profile/"+userId
        userName, userImageLink = getUserName(userLink)
        if userName!='' and ('<!doctype html>' in userName)!=True:
            userNameDict[userName]={"userImage":userImageLink,"userLink":userLink}

    return([bookNameDict, userNameDict])

