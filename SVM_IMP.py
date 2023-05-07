#supervised algorithm
#used for classification


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.svm import SVC

iris=load_iris()
#print(iris.target)
#print(iris.feature_names)
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['target']=iris.target
df['flower_name']=df['target'].apply(lambda x: iris.target_names[x])
#print(df.head())
X=df.values[:,0:4]
Y=df.values[:,5]
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)
model=SVC()#kernel='linear' kernel='linear' argument can be used or C=10 or any number
model.fit(X_train,y_train)
print(model.score(X_test,y_test))

y_pred=model.predict(X_test)

print(y_pred)
