"""
Import the local file cars.csv and split the data set equally into test set 
and training set. 
(don't forget to consider dependent and independent variables).

Print it and save all the datasets  into separate '.csv' files.

file_name - "cars.py"

"""


import pandas as pd

# Importing the dataset
dataset = pd.read_csv('cars.csv')
X = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values
column_names = list(dataset)

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 0)
print X_train,X_test,y_train, y_test

X_train = pd.DataFrame(X_train, columns=column_names[1:])
X_test  = pd.DataFrame(X_test,columns=column_names[1:])

y_train = pd.DataFrame(y_train, columns=[column_names[0]])
y_test  = pd.DataFrame(y_test, columns=[column_names[0]])

X_train.to_csv('Cars_X_Train.csv', index=False)
X_test.to_csv('Cars_X_Test.csv', index=False)
y_train.to_csv('Cars_y_Train.csv', index=False)
y_test.to_csv('Cars_y_Test.csv', index=False)