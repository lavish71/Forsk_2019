# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 16:47:39 2019

@author: dell
"""

# Plotting graph using Seaborn


# importing the required module 
import matplotlib.pyplot as plt 
import seaborn as sns


# Plotting categorical scatter plots with Seaborn

# 1. STRIPPLOT

# x axis values 
x =['sun', 'mon', 'fri', 'sat', 'tue', 'wed', 'thu'] 
  
# y axis values 
y =[5, 6.7, 4, 6, 2, 4.9, 1.8] 
  
# plotting strip plot with seaborn 
ax = sns.stripplot(x, y); 
  
# giving labels to x-axis and y-axis 
ax.set(xlabel ='Days', ylabel ='Amount_spend') 
  
# giving title to the plot 
plt.title('My first graph'); 


# 2. STRIPPLOT USING INBUILT DATA-SET GIVEN IN SEABORN
  
# use to set style of background of plot 
sns.set(style ="whitegrid") 
  
# loading data-set 
iris = sns.load_dataset('iris'); 
  
# plotting strip plot with seaborn 
# deciding the attributes of dataset on which plot should be made 
ax = sns.stripplot(x = 'species', y = 'sepal_length', data = iris); 
  
# giving title to the plot 
plt.title('Graph')


# 3. SWARMPLOT

# use to set style of background of plot 
sns.set(style ="whitegrid") 
  
# loading data-set 
iris = sns.load_dataset('iris'); 
  
# plotting strip plot with seaborn 
# deciding the attributes of dataset on which plot should be made 
ax = sns.swarmplot(x = 'species', y = 'sepal_length', data = iris); 
  
# giving title to the plot 
plt.title('Graph')




