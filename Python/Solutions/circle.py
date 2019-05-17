"""
Code Challenge
  Name: 
    Area and Perimeter of Circle
  Filename: 
    circle.py
  Problem Statement:
    Take the radius of the circle from the keyboard as input from the user 
    Calculate the area and perimeter of it.
  Hint: 
    Pi * radius * radius is the area of circle
    2 * Pi * radius is the perimeter of circle 
    Use math module to get the value of Pi ( 3.14 ) 
  Input:
    Take the radius from the keyboard as input from the user.
"""

import math

radius_of_circle = input("Enter radius of circle >")

radius_of_circle = float(radius_of_circle)

area_of_circle = math.pi*(radius_of_circle)*(radius_of_circle)

perimeter_of_circle = 2*math.pi*radius_of_circle

print ("Area of Circle is "+str(area_of_circle))

print ("Perimeter of Circle is "+str(perimeter_of_circle))
