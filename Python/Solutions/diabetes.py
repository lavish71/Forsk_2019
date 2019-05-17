"""
Download the dataset: 
    https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes

Perform both Multinomial and Gaussian Naive Bayes classification after taking 
care of NA values (maybe replaced with zero in dataset)

Calculate accuracy for both Naive Bayes classification model.

file_name - "diabetes.py"

"""
import pandas as pd
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
DataDiabetes = pd.read_csv("pima-indians-diabetes.csv", header=None, names=col_names)
DataDiabetes.describe()
DataDiabetes.head()
X = DataDiabetes[['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']]
y = DataDiabetes['label']

import matplotlib.pyplot as plt
counter = 0
for i in ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']:
    plt.figure(i)
    plt.hist(DataDiabetes[i])
    plt.xlabel(i)
    plt.show()

# bhmv = before handling missing values    
from sklearn.cross_validation import train_test_split
X_train_bhmv, X_test_bhmv, y_train_bhmv, y_test_bhmv = train_test_split(X, y, test_size = .25)
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import metrics

# testing accuracy of Multinomial Naive Bayes
mnb = MultinomialNB()
mnb.fit(X_train_bhmv, y_train_bhmv)
y_pred_class_bhmv_multi = mnb.predict(X_test_bhmv)

# testing accuracy of Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train_bhmv, y_train_bhmv)
y_pred_class_bhmv_gauss = gnb.predict(X_test_bhmv)

#NA=0 DROP
DataDiabetes.drop(DataDiabetes.index[DataDiabetes.glucose == 0], inplace = True)
DataDiabetes.drop(DataDiabetes.index[DataDiabetes.skin == 0], inplace = True)
DataDiabetes.drop(DataDiabetes.index[DataDiabetes.bmi == 0], inplace = True)
DataDiabetes.drop(DataDiabetes.index[DataDiabetes.insulin == 0], inplace = True)

# ahmv = after handling missing values
from sklearn.cross_validation import train_test_split
X_train_ahmv, X_test_ahmv, y_train_ahmv, y_test_ahmv = train_test_split(X, y, test_size = .25)
mnb = MultinomialNB()
mnb.fit(X_train_ahmv, y_train_ahmv)
y_pred_class_ahmv_multi = mnb.predict(X_test_ahmv)

gnb = GaussianNB()
gnb.fit(X_train_ahmv, y_train_ahmv)
y_pred_class_ahmv_gauss = gnb.predict(X_test_ahmv)

counter = 0
for i in ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']:
    plt.figure(i)
    plt.hist(DataDiabetes[i])
    plt.xlabel(i)
    plt.show()
    
print("Testing accuracy of Multinomial Naive Bayes before handling missing values  : "+str(round(metrics.accuracy_score(y_test_bhmv, y_pred_class_bhmv_multi)*100,2))+"%")
print ("\n")
print("Testing accuracy of Gaussian Naive Bayes before handling missing values  : "+str(round(metrics.accuracy_score(y_test_bhmv, y_pred_class_bhmv_gauss)*100,2))+"%")
print ("\n")
print("Testing accuracy of Multinomial Naive Bayes after handling missing values  : "+str(round(metrics.accuracy_score(y_test_ahmv, y_pred_class_ahmv_multi)*100,2))+"%")
print ("\n")
print("Testing accuracy of Gaussian Naive Bayes after handling missing values  : "+str(round(metrics.accuracy_score(y_test_ahmv, y_pred_class_ahmv_gauss)*100,2))+"%")
