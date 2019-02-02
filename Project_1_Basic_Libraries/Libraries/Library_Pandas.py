# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 12:54:11 2019

@author: dell
"""
# We can analyze data in pandas with:

# a. Series
# b. DataFrames

# a. Series: It is one dimensional(1-D) array defined in pandas 
# that can be used to store any data type.

# 1. CREATING SERIES

# Program to create series 
import pandas as pd  # Import Panda Library 
  
# Create series with Data, and Index
a = pd.Series(Data, Index) # but it shows error because of Data and Index


# 2. WHEN DATA CONTAIN SCALAR VALUES

# Program to Create series with scalar values  
Data =[1, 3, 4, 5, 6, 2, 9]  # Numeric data 
  
# Creating series with default index values 
s = pd.Series(Data)     
  
# predefined index values 
Index =['a', 'b', 'c', 'd', 'e', 'f', 'g']
  

# 3. WHEN DATA CONTAINS DICTIONARY

# Program to Create Dictionary series 
dictionary ={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}  
  
# Creating series of Dictionary type 
sd = pd.Series(dictionary)

# 4. WHEN DATA CONTAINS NDARRAY

# Program to Create ndarray series 
Data =[[2, 3, 4], [5, 6, 7]]  # Defining 2d-array 
  
# Creating series of 2d-array 
snd = pd.Series(Data)


# b. DataFrames: It is two-dimensional(2-D) data structure defined in pandas
# which consists of rows and columns.

# 1. CREATION OF DATAFRAME

# Program to Create DataFrame 
import pandas as pd   # Import Library 

# Create DataFrame with Data
a = pd.DataFrame(Data) # but it shows error because of Data and Index


# 2. WHEN DATA IS DICTIONARY

# Program to Create Data Frame with two dictionaries 
dict1 ={'a':1, 'b':2, 'c':3, 'd':4}        # Define Dictionary 1
dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9} # Define Dictionary 2
Data = {'first':dict1, 'second':dict2}  # Define Data with dict1 and dict2
df = pd.DataFrame(Data)  # Create DataFrame


# 3. WHEN DATA IS SERIES
# Program to create Dataframe of three series
import pandas as pd

s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])           # Define series 1
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3]) # Define series 2
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])     # Define series 3


Data ={'first':s1, 'second':s2, 'third':s3} # Define Data
dfseries = pd.DataFrame(Data)              # Create DataFrame


# 4. WHEN DATA IS 2D-NUMPY NDARRAY

# Program to create DataFrame from 2D array
import pandas as pd # Import Library
d1 =[[2, 3, 4], [5, 6, 7]] # Define 2d array 1
d2 =[[2, 4, 8], [1, 3, 9]] # Define 2d array 2
Data ={'first': d1, 'second': d2} # Define Data
df2d = pd.DataFrame(Data)    # Create DataFrame





