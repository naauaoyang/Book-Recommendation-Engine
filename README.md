# Book_Recommendation_Engine
## Final Project for E6893 Big Data Analytics

Huashu Li(hl2919), Yunfan Zhang(yz2866), Zhuangfei Yang(zy2233)

### Project Description

- **Dataset Description**

We use Amazon Books Review data spanning May 1996 - July 2014 from http://jmcauley.ucsd.edu/data/amazon/ .
It is 9 gigabytes containing 8,898,041 reviews (ratings, text, helpfulness votes etc.).

- **Project Overview**

Build a recommendation system to recommend new books to customers. This includes recommending books to the existing users based on their tastes and recommending reading list to new users based on books’ popularity. 

Group users based on their similarities and recommend friends to users.

Explore the relationship between reviews and helpfulness. Recommend potential useful reviews.

Visualize the findings through System G and Web application.



### How to Open Web GUI
- Download FrontEnd folder
- Download the result files in the following link into downloaded FrontEnd folder
  https://www.dropbox.com/s/mfnl3015r5hyllv/Euclidean_Recommendation.json?dl=0
  https://www.dropbox.com/s/cqoyh6odj056qfa/sorted_avgDict.txt?dl=0
- In terminal run
```
pip install flask
pip install requests
python app.py
```
- Open http://127.0.0.1:5000/ in any of your browser(Chrome, FireFox, IE)

### YouTube Presentation Link
[Click Here](https://youtu.be/ek94sMkvtv4)


