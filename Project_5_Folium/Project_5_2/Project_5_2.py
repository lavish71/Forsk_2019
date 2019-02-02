# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:00:00 2019

@author: dell
"""

import folium
import pandas as pd
import csv
import requests
import json

data = pd.read_csv('E:/Study/Project_5_Folium/Project_5_2/total-final-2.csv')
city = []
with open("E:/Study/Project_5_Folium/Project_5_2/total-final-2.csv") as csv_data:
    doc = csv.reader(csv_data,delimiter=",")
    for i in doc:
        city.append(i[0])
com= list(set(city))


data_lon=[]
data_lat=[]
url1 = "http://api.openweathermap.org/data/2.5/weather?q="
url2 = ""
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

for i in range(0,len(com)):
    if(com[i]=="Durg-Bhilainagar"):
        data_lon.insert(i,"81.3509")
        data_lat.insert(i,"21.1938")
    elif(com[i]=="India"):
        data_lon.insert(i,"78.9629")
        data_lat.insert(i,"20.5937")
    elif(com[i]=="city"):
        continue
    else:
        url2=com[i]
        print(url2)
        url = url1 + url2 + url3
        response = requests.get(url)
        data = response.content
        add_data = json.loads(data)
        data_lon.insert(i,add_data['coord']["lon"])
        data_lat.insert(i,add_data['coord']['lat'])

rows = ["'City','Latitudes','Longitude'"]
with open("lat_lon.csv","w") as write:
    writer = (write)
    for i in range(0,len(com)):
        comp = [city[i],data_lat[i],data_lon[i]]
        print(comp)
        writer.writerow(comp)





