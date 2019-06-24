from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
#loading iris data
iris=load_iris()
#print(dir(iris)) #exploring variables of iris
#print(iris.DESCR) # description of iris
#print(iris.feature_names) # feautres or attribute of iris
#print(iris.target_names) # labels (outputs)
features=iris.data #actaul data with outputs
#print(features)
#print(features.shape)#total no of elements (rows and columns rows=150,column=4)
#print(type(features))#to see data type
label=iris.target # now time for no of label data that is exactly same as feature data
print(label.shape) # total no of elements
#SL=features[0:,0] #sepal length
#print(SL)
#SW=features[0:,1]#sepal width
#print(SW)
#plt.xlabel("sepal lenghth") # labelling x axis
#lt.ylabel("sepal widhth") # labelling y axis
#plt.scatter(SL,SW,label="Sepal_data") # ploting graph of data using scattered dots of sepal
#plt.scatter(features[0:,2],features[0:,3],label="petal data",marker='x')#ploting data graph using scatted x for petal
#plt.legend()
#plt.show()
train_data,test_data,label_train,label_test =  train_test_split(features,label,test_size=0.1)
"""" now time for separting data into two category 1-Training data
2-Testing data or questioning data, 0-1 means 0 to 100% ,where 0.1 means 10%                                      """
from sklearn.tree import DecisionTreeClassifier # for classification
clf=DecisionTreeClassifier() #calling decision tree classifier
trained=clf.fit(train_data,label_train)
predicted_flowers=trained.predict(test_data) # predicting answers
print(label_test) # actual data
#acc=accuracy_score(label_test,predicted_flowers)#to find the accuracy score
#print(acc)