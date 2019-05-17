"""
Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                    ----> represented by column A.

Clump Thickness (1 – 10)                         ----> represented by column B.
Uniformity of Cell Size(1 - 10)                  ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                ----> represented by column D.
Marginal Adhesion (1 - 10)                       ----> represented by column E.
Single Epithelial Cell Size (1 - 10)             ----> represented by column F.
Bare Nuclei (1 - 10)                             ----> represented by column G.
Bland Chromatin (1 - 10)                         ----> represented by column H.
Normal Nucleoli (1 - 10)                         ----> represented by column I.
Mitoses (1 - 10)                                 ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)        ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is cancerous tumor.

Impute the missing values with the most frequent values.

Perform Classification on the given data-set to predict if the tumor is 
cancerous or not.

Check the accuracy of the model.

Predict whether a women has Benign tumor or Malignant tumor, if her Clump 
thickness is around 6, uniformity of cell size is 2, Uniformity of Cell Shape 
is 5, Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is 4, Bare Nuclei 
is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)

file_name - "breast_cancer.py"

"""

# Importing the libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split as tts
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

# Importing the dataset
data = pd.read_csv('breast_cancer.csv')
x = data.iloc[:,1:-1].values
y = data.iloc[:,-1].values

# Handling Missing Values
imp = Imputer(missing_values='NaN', strategy='most_frequent')
x = imp.fit_transform(x)

# Splitting the Dataset
x_train, x_test, y_train, y_test = tts(x,y,random_state=0, test_size=0.25)

# Building SVM model
classifier =  SVC(kernel='linear', random_state=0)
classifier.fit(x_train, y_train)

# Predicting the values
Pred = classifier.predict(x_test)

# Making the Confusion Matrix
cm = confusion_matrix(y_test, Pred)

# Model Score
score = classifier.score(x_test,y_test)

val = np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1)
val_Pred = classifier.predict(val)

print ("Accuracy of the Model : "+str(round(score*100,2))+"%")
print ("\n")

if (val_Pred==4):
    print ("Woman has Malignant Tumor")
else:
    print ("Woman has Benign Tumor")