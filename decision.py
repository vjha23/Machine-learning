from sklearn.tree import DecisionTreeClassifier
import numpy as np
# 0 for apple,1 for orrannge
features=[[100,0],[120,0],[130,1],[150,1]]
label=['apple','apple','orange','orange']
#calling decision tree classifier
clf=DecisionTreeClassifier()
#training the data
trained=clf.fit(features,label)
predict=trained.predict([[100,1]])
print(predict)