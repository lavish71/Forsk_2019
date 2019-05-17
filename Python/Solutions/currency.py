"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currency.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint: 
  http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
"""


import requests

# Hit the url "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y"
response = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y')

# Convert response into dictionary
data = response.json()

# conversion price
conversion_price = data["USD_INR"]["val"]

# take USD value from user as input
user_input_in_USD = int(input("Enter the USD value :"))

# convert USD to INR
USD_to_INR = user_input_in_USD * conversion_price

print ("{0} USD in INR is {1} RS".format(user_input_in_USD, round(USD_to_INR,2)))