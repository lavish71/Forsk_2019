# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:01:04 2019

@author: dell
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert from USD to INR
  Filename: 
    currecncyconv.py how to display seaborn.barplot in python3
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import requests

url = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y"
response = requests.get(url)
response.content






























