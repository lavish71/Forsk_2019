"""
Suppose you are the manager of a bank and you have the problem of 
discriminating between genuine and counterfeit banknotes. You are measuring 
several distances on the banknote and the width and height of it.

Measuring these values of about 100 genuine and 100 counterfeit banknotes, 
Use the data set to set up a logical regression and is capable of 
discriminating between genuine and counterfeit money classification. 
(Import banknotes.csv)

(this data set contains data on Swiss francs currency; it has been obtained 
courtesy of H. Riedwyl )

Check the accuracy of your model using confusion matrix.

Then use k-fold cross validation to find actual mean accuracy of your model.

file_name - "banknotes.py"

"""

# LDA

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('banknotes.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# Fitting XGBoost to the Training set
from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print ("confusion matrix : "+str(cm))

# Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print ("mean accuracy is : "+str(round(accuracies.mean()*100,2))+"%")
print ("standard deviation : "+str(accuracies.std()))
