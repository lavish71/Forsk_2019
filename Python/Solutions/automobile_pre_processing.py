"""
Import the Automobile.csv file.

Now perform the following:

Print the data types.

Build a new dataframe containing only the object columns using select_dtypes 
function.

Find the NaN values in any column and clean them up with the most occurring 
value of that column.

The ” body_style” column contains 5 different values. Perform Label Encoding 
like shown below format

Label Encoding format:
        convertible -> 0
        hardtop -> 1
        hatchback -> 2
        sedan -> 3
        wagon -> 4

Perform OneHotEncoding on “drive_wheels” column where we have values of 4wd , 
fwd or rwd

Perform OneHotEncoding on ”body_style” column

file_name - "automobile_pre_processing.py"

"""

import pandas as pd

data = pd.read_csv('Automobile.csv')
#x = data.iloc[:,:].values
#x=pd.DataFrame(x)

for i in data.columns:
    data[i] = data[i].fillna(data[i].value_counts().index[0])

'''
# Optional Method
from sklearn.preprocessing import Imputer

imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)   
x[:,[0,1,9,10,11,12,13,16,18,19,20,21,22,23,24,25]] = imp.fit_transform(x[:,[0,1,9,10,11,12,13,16,18,19,20,21,22,23,24,25]])
'''

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

obj = LabelEncoder()
data['body_style'] = obj.fit_transform(data['body_style'])
data['drive_wheels'] = obj.fit_transform(data['drive_wheels'])
data_drive_wheels = pd.get_dummies(data['drive_wheels'])

x = data.iloc[:,6:8].values

oht = OneHotEncoder(categorical_features = [0])

data_body_style = oht.fit_transform(x[:,:-1]).toarray()