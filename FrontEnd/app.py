from flask import Flask, render_template, request, json, flash
from flask.ext.mysql import MySQL
import json
import pickle
import random
from resultGenerate import generateResultHTML


app = Flask(__name__)

with open('Euclidean_Recommendation.json') as data_file:  
    UserList = json.load(data_file)

with open('User_Neighboor.json') as file:  
    UserRecommendList = json.load(file)

with open('sorted_userDegreeDict.txt') as userfile:  
    PopularUserList = json.load(userfile)

file = open("sorted_avgDict.txt",'rb')
Booklist = pickle.load(file)
file.close()

def BookRecommendation(userId, UserList, Booklist):
    if userId in UserList:
        return (UserList[userId])
    else:
        RecommendationList = [Booklist[i] for i in random.sample(list(range(100)),  5)]
        recom = dict((m[0],m[1][0]) for m in RecommendationList)
        return (recom)

def UserRecommendation(userId, UserList, UserRecommendList):
    if userId in UserRecommendList:
        return (UserRecommendList[userId])
    else:
        PopularUser = [PopularUserList[i] for i in random.sample(list(range(100)),  5)]
        userRecom = [m[0] for m in PopularUser]
        return (userRecom)



@app.route("/")
def main():
    return render_template('index.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/showsignin')
def showsignin():
    return render_template('signin.html')

@app.route('/signin',methods=['POST'])
def signin():
 
    # read the posted values from the UI
    _name = request.form['uname']

    # validate the received values
    if _name:
        recomm = BookRecommendation(_name, UserList, Booklist)
        cluster = UserRecommendation(_name, UserList, UserRecommendList)
        m = generateResultHTML(recomm, cluster)
        print(m)
        #return (render_template("results.html", records=generateResultHTML(recomm, cluster)))
        return (render_template("results.html", records=m))

    else:
        flash('Please enter the required fields.')
        return render_template('signin.html')



@app.route('/showaboutus')
def showaboutus():
    return render_template('aboutus.html')


if __name__ == "__main__":
    app.run()