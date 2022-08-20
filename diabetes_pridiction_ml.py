# -*- coding: utf-8 -*-
"""Diabetes pridiction ML

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m8ZOooJVqT7IlwMtFaEAWgiHXYIYUBjf

Importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection """

dataset = pd.read_csv('/content/diabetes.csv')

"""Seprating data sets"""

X = dataset.drop(columns = 'Outcome', axis = 1)
Y = dataset['Outcome']

"""Standardinsing and Transforming Data"""

scaler = StandardScaler()
scaler.fit(X)
standard_data = scaler.transform(X)
X = standard_data

"""Splitting Training and Test Data"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,stratify = Y,random_state = 2)

"""Training The Model"""

classifier = svm.SVC(kernel='linear')
classifier.fit(X_train,Y_train)

"""Accuracy Check"""

X_test_prediction = classifier.predict(X_test)
accuracyT = accuracy_score(X_test_prediction,Y_test)
print(accuracyT)

"""Predictive System"""

input_data = (8,99,84,0,0,35.4,0.388,50)

input_data_as_np = np.asarray(input_data)
reshaped_data = input_data_as_np.reshape(1,-1)
std_data = scaler.transform(reshaped_data)
pred = classifier.predict(std_data)
if(pred == 0):
  print("Person is diabetic")
else:
  print("Person is not diabetic")