# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:06:25 2019

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
"""


from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/test").text
soup = BeautifulSoup(source,"lxml")
all_tables=soup.find_all('table')
print (all_tables)
table=soup.find('table', class_='table')
print (table)

A=[]
B=[]
C=[]
D=[]
E=[]


for row in table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==5: #Only extract table body not heading
        A.append(str(cells[0].find(text=True)))
        B.append(str(cells[1].find(text=True)))
        C.append(str(cells[2].find(text=True)))        
        D.append(str(cells[3].find(text=True)))
        E.append(str(cells[4].find(text=True)))
        
import pandas as pd
df=pd.DataFrame(A,columns=['Pos'])
df['Teams']=B
df['Weighted Match']=C
df['Points']=D
df['Ratings']=E
df.to_csv("test_ranking.csv")












