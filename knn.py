#loading iris datasets
from sklearn.datasets import load_iris
#loading into variable
iris_data=load_iris()
#describing iris data interally
print(dir(iris_data))
#target output values
category=iris_data.target_names
print(category)
#now attribute of feautures data
feautures=iris_data.feature_names
print(feautures)
#data with attribute
iris_features=iris_data.data
print(iris_features)
label=iris_data.target # extracting label as per attribute
#separate data into training and testing
from sklearn.model_selection import train_test_split
#help(train_test_spilt)
train_data,test_data,train_label,test_label=train_test_split(iris_features,label,test_size=0.2)
#importing KNN classifier
from sklearn.neighbors import KNeighborsClassifier
kclf=KNeighborsClassifier(n_neighbors=5) # tnis is by default value of k
#now applying training data
ktrained=kclf.fit(train_data,train_label)
#now time for prediction
predict_output=ktrained.predict(test_data)
print(predict_output)
print(test_label)
#calculating accuracy score
from sklearn.metrics import  accuracy_score
acc_knn=accuracy_score(test_label,predict_output)
print(acc_knn)
#calling decision tree clasifier
from sklearn.tree import DecisionTreeClassifier
dclf=DecisionTreeClassifier()
dtrained=dclf.fit(train_data,train_label)
#now predicting
dprediction=dtrained.predict(test_data)
#now accuracy to decsion
dacr=accuracy_score(test_label,dprediction)
print(dacr)
#compare decision and knn



