"""
Panel Data = Pandas 

Using Pandas, we can accomplish five typical steps in the processing and 
analysis of data, regardless of the origin of data — 
load, prepare, manipulate, model, and analyze.

pip install pandas

Pandas deals with the following three data structures −
    Series      -   1 Dimensional 
    DataFrame   -   2 Dimensional 
    Panel       -   3 Dimensional 

DataFrame is a container of Series, Panel is a container of DataFrame.
(Visualisation of Data Frame)


Series is a one-dimensional array like structure with homogeneous data with immutable size. 


DataFrame ( tabular Data ) is a two-dimensional array with heterogeneous data with mutable size.
think of index (the rows) and the columns rather than axis 0 and axis 1.


Panel is a three-dimensional data structure with heterogeneous data.
Graphical Representation is similar to the 3D Array
Layers for tabular data 
(3d_visualisation.jpg)


https://www.tutorialspoint.com/python_pandas/index.htm

"""

#Import Python Libraries

import pandas as pd

# Create an Empty Series
s = pd.Series()
print (type(s))
print (s)



# Create a Series from ndarray
import numpy as np
data = np.array(['a','b','c','d'])
print (type(data ))

s = pd.Series(data)
print (type(s))
print (s)
# We did not pass any index, so by default, 
# it assigned the indexes ranging from 0 to len(data)-1, i.e., 0 to 3.


# Customised Index value
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)


# Create a Series from dict
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s)
# Dictionary keys are used to construct index.
# Dictionary values are used to represent the data


data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print (s)
# Index order is persisted and the missing element is filled with NaN (Not a Number).



# Create a Series from Scalar
s = pd.Series(5, index=[0, 1, 2, 3])
print (s)
# If data is a scalar value, an index must be provided. 
# The value will be repeated to match the length of index



# Accessing Data from Series with Position
# Data in the series can be accessed similar to that in an ndarray.
# No doubt we have given indexes, but we are accessing using position 
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print (s)

#retrieve the first element
print (s[0])

#retrieve the first three element
print (s[:3])


#retrieve the last three element
print (s[-3:])


# A Series is like a fixed-size dict in that you can 
# get and set values by index label.

# Retrieve Data Using Label (Index)
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s)

#retrieve a single element
print (s['a'])


#retrieve multiple elements
print (s[['a','c','d']])


#This will give KeyError
print (s['f'])





# A Data frame is a two-dimensional data structure, i.e., 
# data is aligned in a tabular fashion in rows and columns.
# You can think of it as an SQL table or a spreadsheet data representation


import pandas as pd

#Create an Empty DataFrame
df = pd.DataFrame()
print (df)


# Create a DataFrame from Lists
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df) 



# Create a DataFrame from List of Lists
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)


# Observe, the dtype parameter changes the type of Age 
# column to floating point.
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)


# Create a DataFrame from Dict of Lists
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)


data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print (df)


# Create a DataFrame from List of Dicts
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)
# Observe, NaN (Not a Number) is appended in missing areas.


data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print (df)



data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print (df1)


#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print (df2)

# Observe, df2 DataFrame is created with a column index other than the dictionary key; 
# thus, appended the NaN’s in place. 
# Whereas, df1 is created with column indices same as dictionary keys, 
# so NaN’s appended.


# Create a DataFrame from Dict of Series
# Dictionary of Series can be passed to form a DataFrame. 
# The resultant index is the union of all the series indexes passed.

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)


# Observe, for the series one, there is no label ‘d’ passed, 
# but in the result, for the d label, NaN is appended with NaN.

# Column Selection
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)

print (df ['one'])
print (df ['one']['a'])

 


# Column Addition

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)


# Adding a new column to an existing DataFrame object with column label by passing new series
df['three']= pd.Series([10,20,30],index=['a','b','c'])
print (df)


#Adding a new column using the existing columns in DataFrame:
df['four']=df['one']+df['three']
print (df)


# Column Deletion
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print (df)


# using del function
del df['one']
print (df)


# using pop function
df.pop('two')
print (df)


# Drop rows with label 0
# df = df.drop(0)
# print (df)
# two rows were dropped because those two contain the same label 0.



# Row Selection by Label or index
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)

print (type(df.loc['b']))
print (df.loc['b'])
# The result is a series with labels as column names of the DataFrame.
# And, the Name of the series is the label with which it is retrieved.


# Selection by integer location
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)
print (type(df.iloc[1]))
print (df.iloc[1]) # position by default starts from 0 for the indexes 


# Slice Rows

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)

print(type(df[2:4]))
print (df[2:4])


# Addition of Rows
df1 = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
print (df1)

df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
print (df2)

df = df1.append(df2)
print (df)

print(df.loc[0]) 
print(df.loc[1])  

 

# https://www.tutorialspoint.com/python_pandas/python_pandas_basic_functionality.htm
# https://realpython.com/fast-flexible-pandas/
# https://pandas.pydata.org/pandas-docs/stable/indexing.html

#df = pd.read_csv("https://bitbucket.org/ntpl_sylvester/dataset/raw/467616310ddfaf8abbbbc13bdf1e32cdf0842cbd/Salaries.csv")
#df = pd.read_csv("https://bitbucket.org/ntpl_sylvester/dataset/raw/467616310ddfaf8abbbbc13bdf1e32cdf0842cbd/training_titanic.csv")
#http://openedx.forsk.in/c4x/Forsk_Technologies/FT115/asset/Salaries.csv
#http://openedx.forsk.in/c4x/Forsk_Technologies/FT115/asset/training_titanic.csv

"""
https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-1-exploratory-data-analysis-with-pandas-de57880f1a68

https://github.com/guipsamora/pandas_exercises/
1. Getting and Knowing Your Data
2. Filtering and Sorting
3. Grouping
4. Apply
5. Merge
6. Stats
7. Visualisation
8 Creatig Series and Data FRame
9. Time Series
10. Deleting
11 Indexing

    Read and examine a dataset and classify variables by their type: quantitative vs. categorical
    Handle categorical variables with numerically coded values
    Perform univariate and bivariate analysis and derive meaningful insights about the dataset
    Identify and treat missing values and remove dataset outliers
    Build a correlation matrix to identify relevant variables

Indexing
Computation
Grouping
Aggregation

"""

import pandas as pd
#Read csv file
df = pd.read_csv("data/Salaries.csv")

# Not a good technique to print the Data Frame
print (df)


df.info()


#number of dimensions
df.ndim   


#return a tuple representing the dimensionality
df.shape 


#number of elements
df.size 


#List first 5 records
df.head()


#Try to read the first 10, 20, 50 records;
#Can you guess how to view the last few records;


df.tail(5)


# Gives the row Indexes
df.index


#list the column names / column Indexes
df.columns 


#Check types for all the columns
df.dtypes


#list the row labels/index and column names
df.axes


#numpyrepresentation of the data
df.values 


# generate descriptive statistics (for numeric columns only)
# Standard Deviation is quite useful tool to figure out 
# how the data is spread above or below the mean.
# The higher the value, the less is reliable or vice versa. 
df.describe() # Numeric Columns
print(type(df.describe()))   
 

# This gives a missing values in salary and phd columns


# In order to see statistics on non-numerical features,
# include = all
df.describe(include=['object', 'bool','float64','int64'])
df.describe(include=['object', 'bool'])
df.describe(include=['float64','int64'])
df.describe(include=['object','float64','int64'])


#return max/min values for all columns
df.max() 
df.min()

#return max/min values for all numeric columns
df.mean()
df.median()
df.std()

#What are the mean values of the first 50 records in the dataset?
df.head(50).mean()

#returns a random sample of the data frame
df.sample(5) 




"""
Data Frames: method loc

If we need to select a range of rows, using their labels/index 
we can use method loc
"""

df.loc[:1]

df.loc[10:20,['rank','sex']]


"""
Data Frames: method iloc

If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""
df.iloc[:2]

df.iloc[ 10:21 , [0,4] ]


df.iloc[0] # First row of a data frame

df.iloc[1:5, :-1] # Leave last columns

df.iloc[:, 0] # First column

df.iloc[:, -1] # Last column

df.iloc[0:7] #First 7 rows

df.iloc[:, 0:2] #First 2 columns

df.iloc[1:3, 0:2] #Second through third rows and first 2 columns

df.iloc[[0,5], [1,3]] #1st and 6throws and 2nd and 4thcolumns


some_df = df.iloc[10:20,]
print(some_df)
some_df.head(10)

some_df.iloc[11:20,:]
some_df.iloc[0:10,:]

some_df.iloc[0]
some_df.loc[10]



# Position is starting from 0 onwards but the 
# index is same starting from 10 
some_df.loc[10:19,:]


"""
Selecting a column in a Data Frame with all rows
Method 1:
    Using iloc
    pd.iloc[:,2]

Method 2:
    Using loc
    pd.loc[:,"phd"]
    
Method 3: 
    Subset the data frame using column name like a dictionary:
    df['sex']

Method 4: 
    Use the column name as an attribute:
    df.sex

Note:there is an attribute rank for pandas data frames, 
"""

df.iloc[:,2]

df.loc[:,'phd']
 
# Read the data from a specific Series
df.phd
# Dont use this technique
df.rank

# This is the best practice 
df['phd']



#Select column rank and salary:
df[['rank','salary']]


# Find unique values in a Series / Column
df['rank'].unique()
df['discipline'].unique()
df['sex'].unique()
list1 = df['sex'].unique().tolist()


# intuition about a Rank Series
df['rank']
df['rank'].value_counts()

# to show in Percentage 
df['rank'].value_counts(normalize = True)


# To know the count of male and female candidates
df['sex'] 
df['sex'].value_counts()
df['sex'].value_counts(normalize = True)

# count missing values 
# ( It also counts the NaN Values in the Series/Column)
df['sex'].value_counts(dropna=False)

df['phd'].value_counts()
df['phd'].value_counts(dropna=False)

df['salary'].value_counts()
df['salary'].value_counts(dropna=False)


#calculate the basic statstics on the salary column
df['salary'].mean()
df['salary'].std()
df['salary'].describe()


#Find how many values in the salary column which are non NaN (use count method);
df['salary'].count()
df['phd'].count()

# Boolean Indexing
# Find those rows which has null values in salary/phd column
df['salary'].isnull()
df[df['salary'].isnull()]

df['phd'].isnull()
df[df['phd'].isnull()]
  

"""
Data Frames groupby method

Using "group by" method we can:
Split the data into groups based on some criteria
Calculate statistics (or apply a function) to each group
"""
#Group data using rank
df_rank= df.groupby(['rank'])

df_rank.size()
df_rank.count()
df_rank.groups
# Groups returns a dictionary object
df_rank.groups['AssocProf']
df_rank.groups['AssocProf'][0]

 
#group data using rank followed  by discipline and sex
df_rank=df.groupby(['rank', 'discipline','sex'])
df_rank.groups
df_rank.count()
 
#Calculate mean value for each numeric column per each group
df_rank.mean()


#Calculate mean salary for each type of professor rank:
df.groupby('rank')[['salary','phd']].min()
df.groupby('rank')[['salary','phd']].max()
df.groupby('rank')[['salary','phd']].mean()
        


"""
Data Frame: filtering

To subset the data we can apply Boolean indexing. 
This indexing is commonly known as a filter. 
For example if we want to subset the rows in which the salary
 value is greater than $120K:

"""

# Boolean Indexing in Pandas
# select only those professors who has salary more than 120000
df['salary'] > 120000
df_sub= df[(df['salary'] > 120000) ]
df_sub

#or

df.loc[df['salary'] > 120000]


# to display only the selected series/column
df.loc[df['salary'] > 120000,'salary']



#filter using multiple columns

df_sub= df[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )
           ]
df_sub
# Or

df.loc[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )]



#Select only those rows that contain female professors:
df_sub = df[df['sex'] == 'Female' ][['salary','sex']]
df_sub

# Or

df.loc[df['sex'] == 'Female' ][['salary','sex']]



"""
DataFrame sorting
"""

# Create a new data frame from the original sorted by the column Salary
df_sorted= df.sort_values( by='service')
df_sorted.head()

# To find the lowest salary of the employee
df_sorted= df.sort_values( by='salary', ascending = [True])
df_sorted.head(1)


# To find the highest salary of the employee
df_sorted= df.sort_values( by='salary', ascending = [False])
df_sorted.head(1)


#We can sort the data using 2 or more columns:
df_sorted= df.sort_values( by=['service','salary'], ascending = [True,True])
df_sorted.head(10)

df_sorted= df.sort_values( by=['service','salary'], ascending = [True,False])
df_sorted.head(10)


"""
Missing Values

Missing values are marked as NaN
dropna(how='all') >> Drop observations where all cells is NaN
dropna(axis=1, how='all') >> Drop column if all the values are missing
dropna(thresh = 5) >> Drop rows that contain less than 5 non-missing values
fillna(0) >> Replace missing values with zeros
isnull() >> returns True if the value is missing
notnull() >> Returns True for non-missing values

"""

df.info()

df[df['phd'].isnull()]

df[df['salary'].isnull()]



# mark zero values as missing or NaN
df['salary'] = df['salary'].replace(0, np.NaN)


#return a matrix by checking individual values
df.isnull()


#which column has null values in the Data Frame
df.isnull().any(axis=0)

#Check the rows that has atleast one NaN values
df.isnull().any(axis=1)

# Select the rows that have at least one missing value
df[df.isnull().any(axis=1)]

# Find those rows in which phd column has NaN
df[df['phd'].isnull()]

# Find those rows in which salary column has NaN
df[df['salary'].isnull()]

  

#There are a number of methods to deal with missing values in the data frame:
new_df = df.dropna()
new_df.count()


new_df2 = df.fillna(0)
new_df2.count()


# Fill All columns with missing values, with mean of that column
df = df.fillna(round(df.mean(),0))
df

# fill all the records with missing values, with mean of that column
df['phd'] = df['phd'].fillna(df['phd'].mean())

# fill all the records with missing values, with mean of that column
df['salary'] = df['salary'].fillna(df['salary'].median())



# How to drop columns
df.drop('discipline',axis=1, inplace=True)


# Remove the $ Sign from the Salary Column and then converted the string field into numeric
df['salary'] = df['salary'].str.replace('INR','').str.replace(',','')
df['salary'] = pd.to_numeric(df['salary'])


# Creating a new Column based on some other columns values 
# Male == 0 and Female == 1
df["bool_sex"] = df["sex"].map(lambda x: 0 if x == 'Male' else 1 )
df



#Value Conversion using apply function 
# Male == 0 and Female == 1

df = pd.read_csv("data/Salaries.csv")

def gender_code(gender_string):  
    if (gender_string == "Male") :
        return 0
    elif (gender_string == "Female") :
        return 1   
#    if isinstance(gender_string, float) and math.isnan(gender_string):

df["sex"].value_counts(dropna=False)

df["sex"] = df["sex"].apply(gender_code)

df["sex"].value_counts(dropna=False)


# Create a new column called df.Child where the value is yes
# if df.age is greater than 50 and no if not
df['child'] = np.where(df['age']<18, 'yes', 'no')


# Iterating over rows 
for i, row in df.iterrows():
    print("Index {}".format(i))
    print("Row \n{}".format(row))


# Add examples ot use eval and query 



"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""



# Data Preeprocessing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Loading the dataset
data = pd.read_csv("data/Salaries.csv")
    
# 1. Which Male and Female Professor has the highest and the lowest salaries
# Use the concept of Filtering and Boolean Indexing
male_professor = data[(data['sex']=='Male') & (data['rank']=='Prof')].sort_values('salary')
female_professor = data[(data['sex']=='Female') & (data['rank']=='Prof')].sort_values('salary')

print(male_professor[male_professor['salary'] == male_professor['salary'].max()])
print(male_professor[male_professor['salary'] == male_professor['salary'].min()])

print(female_professor[female_professor['salary'] == female_professor['salary'].max()])
print(female_professor[female_professor['salary'] == female_professor['salary'].min()])

# 2. Which Professor takes the highest and lowest salaries.
prof_data = data[data['rank']=='Prof'].sort_values('salary')
#prof_data['salary'] = prof_data['salary'].fillna(np.mean(prof_data['salary']))
#prof_data['salary'] = prof_data.groupby('service')['salary'].apply(lambda x: x.fillna(x.mean()))

print(prof_data[prof_data['salary'] == prof_data['salary'].max()])
print(prof_data[prof_data['salary'] == prof_data['salary'].min()])

   
""" 
#Alternative 1 
prof_data = data[data['rank']=='Prof']
prof_data['salary'] = prof_data.groupby('service')['salary'].apply(lambda x: x.fillna(x.mean()))
max_salary = max(prof_data['salary'])
min_salary = min(prof_data['salary'])
    

#Alternative 2
prof_data = data[data['rank']=='Prof']
salary_data = np.array(prof_data['salary'])
salary_data = salary_data[~np.isnan(salary_data)]
max_salary = np.max(salary_data)
min_salary = np.min(prof_data['salary'])
"""
 
   
# 3. Missing Salaries - should be mean of the matching salaries of those whose service is the same
#data['salary'] = data.groupby('discipline')['salary'].apply(lambda x: x.fillna(x.mean()))
   
# First Finding the mean of the salries according to the different discipline 
a = data['salary'][data['discipline'] == 'A'].mean()
b = data['salary'][data['discipline'] == 'B'].mean()
    
# Filling the mean salaries for the different categories of discipline
data['salary'][data['discipline'] == 'A'] = data['salary'].fillna(a)
data['salary'][data['discipline'] == 'B'] = data['salary'].fillna(b)

    
# 4. Missing phd - should be mean of the matching service 
#data['phd'] = data.groupby('discipline')['phd'].apply(lambda x: x.fillna(x.mean()))
    
# First Finding the mean of the phd according to the different discipline 
a1 = data['phd'][data['discipline'] == 'A'].mean()
b1 = data['phd'][data['discipline'] == 'B'].mean()
    
# Filling the mean phd by rounding its value for the different categories of discipline
data['phd'][data['discipline'] == 'A'] = data['phd'].fillna(round(a1))
data['phd'][data['discipline'] == 'B'] = data['phd'].fillna(round(b1)) 


# 5. How many are Male Staff and How many are Female Staff. 
# Show both in numbers and Graphically using Pie Chart.  
# Show both numbers and in percentage
data_gender = data['sex'].value_counts().reset_index()
"""Alternative-
1.data_gender = data.groupby('sex').size().reset_index()
2. data_gender = pd.DataFrame(data['sex'].value_counts())
"""
data_gender_ref = pd.DataFrame()
data_gender_ref['Male'] = [data_gender['sex'][0]]
data_gender_ref['Female'] = [data_gender['sex'][1]]
    
vis1 = plt.pie([data_gender_ref['Male'], data_gender_ref['Female']], explode=[0, 0], labels=['male','female'], autopct="%1.1f%%")
plt.axis('equal')
plt.show(vis1)
    
# Function to show the actual values in pie chart
def absolute_value(val):
   a  = np.round(val/100.*(np.array([39,39])).sum(), 0)
   return a

vis2 = plt.pie([data_gender_ref['Male'], data_gender_ref['Female']], explode=[0, 0], labels=['male','female'], autopct=absolute_value)
plt.axis('equal')
plt.show(vis2)
    
# 6. How many are Prof, AssocProf and AsstProf. 
# Show both in numbers adn Graphically using a Pie Chart
data_rank = data['rank'].value_counts().reset_index()
data_rank_ref = pd.DataFrame()
data_rank_ref['Prof'] = [data_rank['rank'][0]]
data_rank_ref['AsstProf'] = [data_rank['rank'][1]]
data_rank_ref['AsscProf'] = [data_rank['rank'][2]]
    
vis3 =  plt.pie([data_rank_ref['Prof'], data_rank_ref['AsstProf'],data_rank_ref['AsscProf'] ], explode=[0, 0,0], labels=['Prof','AsstProf', 'AsscProf'], autopct="%1.1f%%")
plt.axis('equal')
plt.show(vis3)


def absolute_value(val):
    a  = np.round(val/100.*(np.array([46,19,13])).sum(), 0)
    return a

vis4 = plt.pie([data_rank_ref['Prof'], data_rank_ref['AsstProf'],data_rank_ref['AsscProf'] ], explode=[0, 0,0], labels=['Prof','AsstProf', 'AsscProf'], autopct=absolute_value)
plt.axis('equal')
plt.show(vis4)
    
# 7. Who are the senior and junior most employees in the organization.
data_service = data.sort_values(['service'])
print(data_service[data_service['service'] == data_service['service'].max()])
print(data_service[data_service['service'] == data_service['service'].min()])
   

# 8. Draw a histogram of the salaries divided into bin starting from 50K and increment of 15K
plt.hist(data['salary'], bins=range(50000, 190000, 15000), facecolor='g')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary distribution')
plt.grid(True)
plt.show()


#distribution of salary using histogram with pandas
new_df = df['salary']
new_df.hist(bins=20,grid=False)







"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Titanic
  Filename: 
      titanic.py
  Dataset:
      training_titanic.csv
  Data Description:      
      survival: Survival (0 = No; 1 = Yes)
      pclass: Passenger Class (1 = Upper; 2 = Middle; 3 = Lower)
      name: Name
      sex: Sex
      age: Age 
      sibsp: Number of Siblings/Spouses Aboard
      parch: Number of Parents/Children Aboard
      ticket: Ticket Number
      fare: Passenger Fare
      cabin: Cabin
      embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

  Problem Statement:
      Titanic ship that crashed in April, 1912.
      Real-world data containing the details of titanic ships passengers list.
      There were lifeboats for only 1178 people
      There were 2224 passengers on board
      Answer the Following:
      0. Total number of Passengers in the dataset
      0. Find all large families (Sibsp > 3)
      0. Find all the features which has missing
      0. Drop the column which has the max missing
      0. Embarked Feature missing values needs to be fixed
      0. Age missing value needs to be fixed
      1. How many people survived the disaster ?
      2. How many people died the disaster ?
      3. Plot the people who survived Vs died appropriately.
      4. Calculate and print the survival rates as proportions (percentage) 
      5. Which gender have greater survival rate ?
         Were females given high priority while rescue.
         Males that survived vs males that passed away
         Females that survived vs Females that passed away
         Also plot it
      6. Does age play a role for survival?
         Since it's probable that children were saved first.
  
  Advanced Problem Statements:
     7. Does Pclass feature plays role in survival
         Survived Vs Died according to Pclass and sex
         Plot it (FactorPlot and CrossTab)
      8. Who was the oldest person survived 
      9. Yougest person survived
      10. Is there a relationship between Pclass and the survival 
          Draw violen plots PClass and Age Vs Survived 
          Sex and Age Vs Survived 
      11. Find the title from the name and show its value counts
          train['title'] = train.Name.str.extract('\, ([A-Z][^ ]*\.)',expand=False)
      12. If a passanger is alone in ship with no siblings, survival rate is 
          If I have a family onboard, I will save them instead of saving myself.
          But there’s something wrong, the survival rate for families 
          with 5–8 members is 0%. Is this because of PClass? Yes this is PClass,
          large families in Pclass3(>3) died.
      13. Everything except ‘PassengerId’, ‘Ticket’ and ‘Name’ would be 
          correlated with a high survival rate
      14. Do Not Delete the Cabin Column, but recreate using Deck
      
      
  Hint: 
      https://medium.com/@mjamilmoughal786/exploratory-data-analysis-of-titanic-dataset-with-python-94b0c84cd108
      https://www.kaggle.com/aselad/exploratory-data-analysis-on-the-titanic-dataset
      https://towardsdatascience.com/predicting-the-survival-of-titanic-passengers-30870ccc7e8
      
      
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
 
     You can test this by creating a new column with a Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.

      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
      
"""



"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""


"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""



"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""



"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
  Hint:

import pandas as pd
import requests
import StringIO as StringIO
import numpy as np
        
url = "https://data.baltimorecity.gov/api/views/2j28-xzd7/rows.csv?accessType=DOWNLOAD"
r = requests.get(url)
data = StringIO.StringIO(r.content)

dataframe = pd.read_csv(data,header=0)

dataframe['AnnualSalary'] = dataframe['AnnualSalary'].str.lstrip('$')
dataframe['AnnualSalary'] = dataframe['AnnualSalary'].astype(float)

# group the data
grouped = dataframe.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

# sort the data
pd.set_option('display.max_rows', 10000000)
output = aggregated.sort(['amax'],ascending=0)
output.head(15)


aggregated = grouped.agg([np.sum])
output = aggregated.sort(['sum'],ascending=0)
output = output.head(15)
output.rename(columns={'sum': 'Salary'}, inplace=True)


from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind='bar',title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d'))



"""

"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   
  Hint:

    The columns contain information about that game:

    score_phrase — how IGN described the game in one word. 
                   This is linked to the score it received.
    title — the name of the game.
    url — the URL where you can see the full review.
    platform — the platform the game was reviewed on (PC, PS4, etc).
    score — the score for the game, from 1.0 to 10.0.
    genre — the genre of the game.
    editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
    release_year — the year the game was released.
    release_month — the month the game was released.
    release_day — the day the game was released.



xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
      
%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()
        
"""



"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""
      
"""      
import pandas as pd

data = pd.read_csv("thanksgiving-2015-poll-data.csv", encoding="Latin-1")
data.head()

data["gender"] = data["What is your gender?"].apply(gender_code)
data["gender"].value_counts(dropna=False)

data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts(dropna=False)

import numpy as np

def clean_income(value):
    if value == "$200,000 and up":
        return 200000
    elif value == "Prefer not to answer":
        return np.nan
    elif isinstance(value, float) and math.isnan(value):
        return np.nan
    value = value.replace(",", "").replace("$", "")
    income_high, income_low = value.split(" to ")
    return (int(income_high) + int(income_low)) / 2
    
data["income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(clean_income)
data["income"].head()



data["What type of cranberry saucedo you typically have?"].value_counts()

homemade = data[data["What type of cranberry saucedo you typically have?"] == "Homemade"]
canned = data[data["What type of cranberry saucedo you typically have?"] == "Canned"]

print(homemade["income"].mean())
print(canned["income"].mean())


grouped = data.groupby("What type of cranberry saucedo you typically have?")
grouped
grouped.groups
grouped.size()
      
for name, group in grouped:
    print(name)
    print(group.shape)
    print(type(group))
    
grouped["income"]
grouped["income"].size()


grouped["income"].agg(np.mean)
grouped.agg(np.mean)

grouped = data.groupby(["What type of cranberry saucedo you typically have?", "What is typically the main dish at your Thanksgiving dinner?"])
grouped.agg(np.mean)

grouped = data.groupby("How would you describe where you live?")["What is typically the main dish at your Thanksgiving dinner?"]
grouped.apply(lambda x:x.value_counts())


"""


"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
        
        
https://bigml.com/user/francisco/gallery/dataset/5163ad540c0b5e5b22000383
https://www.kaggle.com/kashnitsky/topic-1-exploratory-data-analysis-with-pandas       
https://github.com/guipsamora/pandas_exercises/
        
        
"""



#few assignments

import re 
import pandas as pd


data = {'raw': ['TZOV42x34F1-020-0223']}
df = pd.DataFrame(data, columns = ['raw'])


# In the column 'raw', extract single digit in the strings

df['col1'] = df['raw'].str.extract('(\w\w)', expand=True)
df['col1']

df['col2'] = df['raw'].str.extract('((?<=^..)[\w]{2})', expand=True)
df['col2']

df['col3'] = df['raw'].str.extract('((?<=^....)[\d]{1,}x[\d]{1,})', expand=True)
df['col3']

df['col4'] = df['raw'].str.extract('(\w\d(?=-\d{1,}))', expand=True)
df['col4']

df['col5'] = df['raw'].str.extract('(\d{1,}(?=-\d{1,}$))', expand=True)
df['col5']

df['col6'] = df['raw'].str.extract('(\d{1,}$)', expand=True)
df['col6']


#version2

str1 = 'TZOV4x3F1-020-022'



print ([re.match('(\w{2})', str1).groups()[0]])

print (re.findall('((?<=^..)[\w]{2})', str1))

print (re.findall('((?<=^....)[\w]{3})', str1))

print (re.findall('((?<=^[\w]{7})[\w]{2})', str1))

print ([re.findall('(\d\d\d)', str1)[0]])

print ([re.findall('(\d\d\d)', str1)[1]])