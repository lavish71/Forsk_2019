# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 15:14:56 2019

@author: dell
"""

# importing matplotlib module  
import matplotlib.pyplot as plt

# 1. BASIC PLOTS IN MATPLOTLIB

# a. Line Plot
# x-axis values 
x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2]
  
# Function to plot 
plt.plot(x,y) 
  
# Function to show the plot 
plt.show()


# b. Bar Plot
# Function to plot the bar 
plt.bar(x,y)

# c. Histogram
# Function to plot histogram 
plt.hist(x)

# d. Scatter Plot
# Function to plot scatter 
plt.scatter(x,y)


