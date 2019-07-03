import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#importing the datasets
datasets=pd.read_csv('info.csv')
#print(datasets)
#making this into metric forms and separate dependent and independent columns
X=datasets.iloc[:, :-1].values
print(X)
Y=datasets.iloc[:,3].values
print(Y)
# taking care of missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(X[:,1:3]) # fiting only those who have missing data
X[:,1:3]=imputer.transform(X[:,1:3])
#print(X)
#Time for catgorical data
from sklearn.preprocessing import LabelEncoder
labelencoder_X=LabelEncoder()
X[:, 0]=labelencoder_X.fit_transform(X[:, 0]) # for changing countries name into int
print(X) #now using dummy method in this
from sklearn.preprocessing import OneHotEncoder
onehoten_X = OneHotEncoder(categorical_features=[0]) #specifying 0 index column
X = onehoten_X.fit_transform(X).toarray()
print(X)
labelencoder_Y=LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)
print(Y)
#onehoten_Y = OneHotEncoder(categorical_features=[3])
#Y = onehoten_Y.fit_transform(Y).toarray()
#print(Y)
# splitting the data sets into testing and training
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)
#Feauture scalling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)