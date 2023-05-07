import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier


data=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data',sep= ',', header = None)
data.head()

print ("Dataset Length: ", len(data))
print ("Dataset Shape: ", data.shape)

X = data.values[:, 1:5] #features
Y = data.values[:, 0] #target
print(Y)

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

clf_gini = DecisionTreeClassifier(criterion = "gini",random_state = 100,max_depth=3, min_samples_leaf=5) #criterion="entropy"
#for pruning ccp_alpha=0.015
clf_gini.fit(X_train, y_train)
y_pred = clf_gini.predict(X_test)
print("Predicted values:")
print(y_pred)

print("Confusion Matrix: ",confusion_matrix(y_test, y_pred))
print ("Accuracy : ",accuracy_score(y_test,y_pred)*100)
print("Report : ",classification_report(y_test, y_pred))
