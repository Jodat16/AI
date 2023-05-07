'''Refer to the advertising dataset on Kaggle. You are supposed to run a linear regression with Sales as the dependent
variable and TV as independent variable. You are required to perform a train/test split of 70-30 and run
the linear regression through the stats-model library.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#linear regression gies continous output . not used for classifying problem.s Can use for prediction like house price prediction
advert = pd.read_csv('advertising.csv')
advert.head()

X=advert.values[:,1].reshape(-1,1) #X should always be 2d array. so we do reshape if only one X feature
y=advert.values[:,4]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
lm=LinearRegression()
lm.fit(X_train,y_train)

y_pred=lm.predict(X_test)
print(y_pred)

print("Accuracy of model is: ",lm.score(X_test,y_test)*100,"%")

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)
