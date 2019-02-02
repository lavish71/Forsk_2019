# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 15:44:40 2019

@author: dell
"""

# Plotting using numpy, pandas and matplotlib
# Importing libraries
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

# Types of Plots:
# 1. BASIC PLOTTING  
ts = pd.Series(np.random.random(1000), index = pd.date_range('1/1/2000', periods = 1000)) 
ts = ts.cumsum() 
ts.plot()  


# 2. PLOT OF DIFFERENT DATA : Using more than one list of data in a plot.  
df = pd.DataFrame(np.random.randn(1000, 4),index = ts.index, columns = list('ABCD')) 
df = df.cumsum() 
plt.figure() 
df.plot() 


# 3. HISTOGRAM 
df = pd.DataFrame({'a': np.random.randn(1000) + 1,  
                    'b': np.random.randn(1000),  
                    'c': np.random.randn(1000) - 1}, 
                           columns =['a', 'b', 'c']) 
plt.figure() 
df.plot.hist(alpha = 0.5)


# 4. BOX PLOT
df = pd.DataFrame(np.random.rand(10, 5),  
      columns =['A', 'B', 'C', 'D', 'E'])
df.plot.box() 


# 5. DENSITY PLOT
df = pd.DataFrame(np.random.rand(10, 5),  
      columns =['A', 'B', 'C', 'D', 'E']) 
ser = pd.Series(np.random.randn(1000)) 
ser.plot.kde() 


# 6. AREA PLOT
df = pd.DataFrame(np.random.rand(10, 5),  
       columns =['A', 'B', 'C', 'D', 'E'])
df.plot.area()


# 7. SCATTER PLOT
df = pd.DataFrame(np.random.rand(500, 4), 
        columns =['a', 'b', 'c', 'd'])
df.plot.scatter(x ='a', y ='b')


# 8. HEXAGONAL BIN PLOT
df = pd.DataFrame(np.random.randn(1000, 2), 
        columns =['a', 'b'])
df['a'] = df['a'] + np.arange(1000) 
df.plot.hexbin(x ='a', y ='b', gridsize = 25)


# 9. PIE PLOT
series = pd.Series(3 * np.random.rand(4),
        index =['a', 'b', 'c', 'd'], name ='series') 
series.plot.pie(figsize =(4, 4))