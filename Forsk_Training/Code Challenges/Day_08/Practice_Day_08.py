# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:38:55 2019

@author: dell
"""

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi   
    https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    https://www.icc-cricket.com/rankings/mens/team-rankings/test

"""

from bs4 import BeautifulSoup as BS
import pandas as pd
import requests
from collections import OrderedDict

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(url).text

soup = BS(source,'lxml')
print(soup.prettify())

right_table = soup.find('table', class_ = 'table')
print(right_table.prettify())

A=[]
B=[]
C=[]
D=[]
E=[]

for i in right_table.findAll('tr'):
    rows = i.findAll('td')
    if len(rows) == 5:
        A.append(rows[0].text.strip())
        B.append(rows[1].text.strip())
        C.append(rows[2].text.strip())
        D.append(rows[3].text.strip())
        E.append(rows[4].text.strip())

columns = ['Position','Team','Weighted_Matches','Points','Rating']
add_col = OrderedDict(zip(columns,[A,B,C,D,E]))
df = pd.DataFrame(add_col)
df.to_csv("ranking_odi.csv")


"""
Code Challenge:
  Name:
    Bid Plus
  Filename:
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. Items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
      
"""

from selenium import webdriver
from time import sleep
import pandas as pd
import requests
from collections import OrderedDict


url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("D:/Study/Forsk_Training/Code Challenges/Day_08/chromedriver.exe")
browser.get(url)

dwnld1 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[1]/p[1]')
dwnld1.click()

sleep(2)

dwnld2 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[2]/div[1]/p[1]')
dwnld2.click()

sleep(2)

dwnld3 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[3]/div[1]/p[1]')
dwnld3.click()
  
sleep(2)

dwnld4 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[4]/div[1]/p[1]')
dwnld4.click()

sleep(2)

dwnld5 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[5]/div[1]/p[1]')
dwnld5.click()
  
sleep(2)

dwnld6 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[6]/div[1]/p[1]')
dwnld6.click()
  
sleep(2)

dwnld7 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[7]/div[1]/p[1]')
dwnld7.click()

sleep(2)

dwnld8 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[8]/div[1]/p[1]')
dwnld8.click()
      
sleep(2)

dwnld9 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[9]/div[1]/p[1]')
dwnld9.click()
    
sleep(2)

dwnld10 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[10]/div[1]/p[1]')
dwnld10.click()

sleep(5)

browser.quit()

# 

from selenium import webdriver
from time import sleep
import pandas as pd
import requests
from collections import OrderedDict

url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("D:/Study/Forsk_Training/Code Challenges/Day_08/chromedriver.exe")
browser.get(url)

# Creating empty Lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]

for i in range(1,11):
    gem = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    A.append(gem)
    item = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    B.append(item)
    quantity = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text
    C.append(quantity)
    dep = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    D.append(dep)
    start_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[:11]
    E.append(start_date)
    start_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[11:]
    F.append(start_time)
    end_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[:11]
    G.append(end_date)
    end_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[11:]
    H.append(end_time)


columns = ['GEM_BID','ITEMS','QUANTITY','DEPARTMENT NAME AND ADDRESS','STARTING_DATE','STARTING_TIME','ENDING_DATE','ENDING_TIME']
add_col = OrderedDict(zip(columns,[A,B,C,D,E,F,G,H]))
df = pd.DataFrame(add_col)


"""
Code Challenge

url = "http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image.

"""

from PIL import Image
from io import BytesIO
import requests

responce = requests.get('http://forsk.in/images/Forsk_logo_bw.png')
image1 = Image.open(BytesIO(responce.content))
image1.save("Forsk_logo_bw.png")