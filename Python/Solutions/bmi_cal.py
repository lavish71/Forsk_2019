"""
Code Challenge
  Name: 
    Adult Body Mass Index Calculator
  Filename: 
    bmi_cal.py
  Problem Statement:
    Assuming your weight in kilogram and height in meters  
    Calculate your BMI value and print it ?
  Hint: 
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI
"""

# User weight
weight = float(input("Enter your weight in kilograms >"))

# User height
height = float(input("Enter your height in meters >"))

# BMI Formula
BMI_value = (weight/height)/height

print ("BMI value is :"+str(round(BMI_value,2)))