# -*- coding: utf-8 -*-
"""
Created on Tue May 14 04:02:11 2019

@author: dell
"""

"""
Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple)
   Hint:
       www.jsonlint.com
       
"""

{
	"Student1": {
		"fname": "Rahul",
		"lname": "Soni",
		"photo": "6561",
		"department": "CS",
		"research_areas": [9898, 945],
		"contact": {
			"phone": [9584236175, 7854231695],
			"email": "rahulsoni@gmail.com"
		}
	},
	"Student2": {
		"fname": "Jayesh",
		"lname": "Gupta",
		"photo": "545",
		"department": "Commerce",
		"research_areas": [454, 454],
		"contact": {
			"phone": [8542316789, 7895123654],
			"email": "jayesh04gupta@gmail.com"
		}
	}
}
        


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

response = requests.get(url)
r1 = response.content
r2 = response.text
json_data = response.json()

print("Latitude   : " + str(json_data['coord']['lat']))
print("Longitude  : " + str(json_data['coord']['lon']))
print("Weather Condition  : " + str(json_data['weather'][0]['main']))
print("Wind Speed  : " + str(json_data['wind']['speed']))
print("Sun Rise Timing  : " + str(json_data['sys']['sunrise']))
print("Sun Set Timing  : " + str(json_data['sys']['sunset']))


"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import requests

url1 = "https://free.currconv.com/api/v7/convert"
url2 = "?q=USD_INR"
url3 = "&compact=ultra&apiKey=6c3bd521fe13a3af2ca1"

url = url1 + url2 + url3

response = requests.get(url)
response.content

json_data = response.json()

print("USD to INR  : " + str(json_data['USD_INR']))




