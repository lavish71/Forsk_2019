
import numpy as np

# Simultaneous Assignment
X, y = np.arange(10).reshape((5, 2)), list(range(5))

print (type(X))
print (type(y))

print (X)
print (y)


# train_test_split splits arrays or matrices into random train and test subsets. 
# That means that everytime you run it without specifying random_state, 
# you will get a different result, this is expected behavior. 



#from sklearn.cross_validation import train_test_split
#Deprecated since version 0.18: This module will be removed in 0.20. 
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

print (X_train)
print (X_test)

print (y_train)
print (y_test)



# If you use random_state=some_number, 
# then you can guarantee that your split will be always the same. 
# This is useful if you want reproducible results, 
# I would say, set the random_state to some fixed number while you test stuff, 
# but then remove it in production if you need a random (and not a fixed) split.



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print (X_train)
print (X_test)

print (y_train)
print (y_test)


# This result would be different from last one, but if you run it again and again it will be same

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100)

print (X_train)
print (X_test)

print (y_train)
print (y_test)





"""
Steps in Data Preprocessing

Step 1 : Import the libraries
Step 2 : Import the data-set
Step 3 : Check out the missing values - imputation using sklearn, pandas
Step 4 : Label encoding - categorical data using LabelEncoder, cat.code (category)
Step 5 : order issue - onehotencoding (dummy encoding) - OneHotEncoder, get_dummies
Step 6 : Splitting the data-set into Training and Test Set
Step 7 : Feature Scaling

"""

#Now before we move to modeling of the data, 
#we need to split the dataset into train data and test data.

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('data/Data.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)




"""
HandsOn
#Import the local file cars.csv and split the data set equally into test set and training set.
#Print it and save both data sets  into two new .csv file.

"""



import pandas as pd
import numpy as np


# Importing the dataset
dataset = pd.read_csv('data/cars.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values.reshape(-1,1)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)
print (X_train,X_test,y_train, y_test)


# Write code to save in the csv file

# Combining the features and labels in both train and test data
train_data = np.concatenate([X_train, y_train],axis=1)
test_data = np.concatenate([X_test, y_test], axis=1)

# Fetching all the columns name from the original dataset
head = list(dataset.columns)

# Framing the test and train dataframe
train_df, test_df = pd.DataFrame(), pd.DataFrame()

for var in range(0,12):
    train_df[head[var]] = train_data[:, var]
    test_df[head[var]] = test_data[:, var]

# Creating seperate train and test csv files
train_df.to_csv("data/cars_train.csv")
test_df.to_csv("data/cars_test.csv")

# Printing the train and test dataframes
print("train_data:", train_df)
print("test_data:", test_df)

