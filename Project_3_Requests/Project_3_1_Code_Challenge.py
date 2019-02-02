# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:34:34 2019

@author: dell
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1 + url2 + url3
print (url)

response = requests.get(url)
response.content
print (response.text)
print ("Status code: " + str(response.status_code))
print ("Headers : " + str(response.headers))

for key, value in response.headers.items():
    print (key, ":" ,value , "\n")

print ("Content type: " + response.headers['content-type'])
jsondata = response.json()
# Content in binary form
print (type(response.content))

print ("Content or Response Body : " + str(response.content))

for key, value in jsondata.items():
    print (key, ":" ,value , "\n")

print ("Longitude : " + str(jsondata["coord"]["lon"]))
print ("Latitude : " + str(jsondata["coord"]["lat"]))
print ("Weather : " + str(jsondata["weather"]))
print ("Wind : " + str(jsondata["wind"]))
print ("Sunrise : " + str(jsondata["sys"]["sunrise"]))
print ("Sunset : " + str(jsondata["sys"]["sunrise"]))
















