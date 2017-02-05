import pandas as pd
import requests
import time
import json
import random

def getBookName(url):
    proxies = [
    {'host': '1.2.3.4', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '2.3.4.5', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '2.2.3.4', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '1.2.4.4', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '1.2.3.5', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '1.2.2.4', 'port': '1234', 'username': 'myuser', 'password': 'pw'}
    ]
    
    headers=[
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"},
    {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}]
    i = random.randint(0, 5)
    j = random.randint(0, 3)

    html = requests.get(url,headers=headers[j],proxies=proxies[i])
    page = html.text
    #print(page)
    a = page.find('<span id="productTitle"')+len('<span id="productTitle"')
    b = page[a:].find('>')+1
    c = page[a+b:].find('</span>')
    Name = page[a+b:a+b+c]

    if len(Name)>1000 or a==-1+len('<span id="productTitle"'):
        a = page.find('<meta name="title" content="')+len('<meta name="title" content="')
        b = page[a:].find('"')
        Name = page[a:a+b]

    
    
    d = page.find('miniATF_imageColumn')+len('miniATF_imageColumn')
    e = page[d:].find('<img alt="" src="')+len('<img alt="" src="')
    f = page[d+e:].find('" class=')
    Image = page[d+e:d+e+f]


    if len(Image)>1000 or d==-1+len('miniATF_imageColumn'):
        d = page.find('ebooks-img-canvas')
        e = page[d:].find('data-a-dynamic-image="{&quot;')+len('data-a-dynamic-image="{&quot;')
        f = page[d+e:].find('&quot;')
        Image = page[d+e:d+e+f]
    print(Image)


    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        Name = Name.replace(code[1], code[0])

    #time.sleep(1)


    return (Name, Image)


def getUserName(url):
    proxies = [
    {'host': '1.2.3.4', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '2.3.4.5', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '2.2.3.4', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '1.2.4.4', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '1.2.3.5', 'port': '1234', 'username': 'myuser', 'password': 'pw'},
    {'host': '1.2.2.4', 'port': '1234', 'username': 'myuser', 'password': 'pw'}
    ]
    
    headers=[
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"},
    {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}]
    i = random.randint(0, 5)
    j = random.randint(0, 3)

    html = requests.get(url,headers=headers[j],proxies=proxies[i])
    page = html.text
    #print(page)
    a = page.find('<span class="public-name-text">')+len('<span class="public-name-text">')
    b = page[a:].find('</span>')
    Name = page[a:a+b]

    #print(page)
        
    
    d = page.find("<div class='pr-image-preview-container circular-profile-image'>")+len("<div class='pr-image-preview-container circular-profile-image'>")
    e = page[d:].find('<img alt="" src="')+len('<img alt="" src="')
    f = page[d+e:].find('">')
    Image = page[d+e:d+e+f]


    #time.sleep(1)


    return (Name, Image)

if __name__=='__main__':
    #getUserName("https://www.amazon.com/gp/pdp/profile/A40N5P6DG7FOL")
    print(getBookName("https://www.amazon.com/gp/product/B00F8LQAUK"))
    #getBookName("https://www.amazon.com/gp/product/B005J4YHCE")





