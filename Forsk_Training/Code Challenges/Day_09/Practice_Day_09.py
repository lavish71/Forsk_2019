# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:59:33 2019

@author: dell
"""

"""
Code Challenge 1

Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""

import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'db_University.db' )

c = conn.cursor()

#c.execute("DROP TABLE university")

c.execute("""CREATE TABLE university(
        Student_Name TEXT,
        Studen_Age INTEGER,
        Student_Roll_no INTEGER,
        Student_Branch TEXT
        )""")

c.execute("INSERT INTO university VALUES ('Aarohi',19,1,'CS')")
c.execute("INSERT INTO university VALUES ('Dushyant',18,2,'CS')")
c.execute("INSERT INTO university VALUES ('Karan',17,3,'CS')")
c.execute("INSERT INTO university VALUES ('Rohit',18,4,'CS')")
c.execute("INSERT INTO university VALUES ('Priyansh',19,5,'CS')")
c.execute("INSERT INTO university VALUES ('Meera',20,6,'CS')")
c.execute("INSERT INTO university VALUES ('Rakesh',19,7,'CS')")
c.execute("INSERT INTO university VALUES ('Preety',18,8,'CS')")
c.execute("INSERT INTO university VALUES ('Rahul',19,9,'CS')")
c.execute("INSERT INTO university VALUES ('Prateek',17,10,'CS')")

c.execute("SELECT * FROM university")

#print(c.fetchone())
#print(c.fetchmany(4))
print(c.fetchall())

conn.commit()
conn.close()


"""
Code Challenge 2

Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.

"""




"""
Code Challenge 3

In the Bid plus Code Challenege 
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database

"""

from selenium import webdriver
from time import sleep
import requests

url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome("D:/Study/Forsk_Training/Code Challenges/Day_08/chromedriver.exe")
browser.get(url)

# Creating empty Lists
gem1=[]
item1=[]
quantity1=[]
dep1=[]
start_date1=[]
start_time1=[]
end_date1=[]
end_time1=[]

for i in range(1,11):
    gem = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    gem1.append(gem)
    item = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    item1.append(item)
    quantity = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text
    quantity1.append(quantity)
    dep = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    dep1.append(dep)
    start_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[:11]
    start_date1.append(start_date)
    start_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[11:]
    start_time1.append(start_time)
    end_date = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[:11]
    end_date1.append(end_date)
    end_time = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[11:]
    end_time1.append(end_time)


# DATABASE
import mysql.connector

conn = mysql.connector.connect ( user='root', password='', host='localhost')

c = conn.cursor()

#c.execute("DROP DATABASE bid_plus;")

c.execute("CREATE DATABASE bid_plus;")

c.execute("USE bid_plus;")

c.execute("DROP TABLE bid;")

c.execute("""CREATE TABLE bid(
        BID_NO TEXT,
        ITEMS TEXT,
        QUANTITY_REQUIRED TEXT,
        DEPARTMENT_NAME_AND_ADDRESS TEXT,
        START_DATE TEXT,
        START_TIME TEXT,
        END_DATE TEXT,
        END_TIME TEXT)""")

for i in range(0,10):
    c.execute("INSERT INTO bid VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(gem1[i],item1[i],quantity1[i],dep1[i],start_date1[i],start_time1[i],end_date1[i],end_time1[i]))

c.execute("SELECT * FROM bid")

print (c.fetchall())

conn.commit()
conn.close()


"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi

"""

from bs4 import BeautifulSoup as BS
import requests

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

import sqlite3

conn = sqlite3.connect ( 'cricket.db' )

c = conn.cursor()

c.execute("DROP TABLE ranking")

c.execute("""CREATE TABLE ranking(
        Position TEXT,
        Teams TEXT,
        Matched TEXT,
        Points TEXT,
        Rating TEXT)""")

for i in range(0,15):
    c.execute("INSERT INTO ranking VALUES ('{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i]))

c.execute("SELECT * FROM ranking")

print (c.fetchall())