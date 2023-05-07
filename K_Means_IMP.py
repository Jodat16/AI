#unsupervised learning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.cluster import KMeans

df=pd.read_csv("C:/Users/ab/Desktop/Ai final/Lab10/Wholesale customers data.csv")
#print(df.head())
X=df.values[:]

kmeans = KMeans(n_clusters=2, init='k-means++',n_init=10) #if kmeans++ otherwise only n_clusters argument

kmeans.fit(X)

#Inertia also called SSE. It calculates the sum of the distances of all points within a cluster from the centroid of the point.
print(kmeans.inertia_) #sum of squared error SSE plot it againts different number of clusters to use for elbow methoid

# The number of iterations required to converge
print(kmeans.n_iter_)

print(kmeans.cluster_centers_)

y_pred = kmeans.predict(X)
df.insert(8, "Clusters", y_pred) #adding a new columkn for cluster in dataset


#for viualization practise
# plt.subplot(1, 2, 1) makijg subplots of 1 row 2 columns and choosing the 1st index (1st subplot)
# colors = np.array(['red', 'green', 'blue'])
# plt.scatter(df['Channel'], df['Region'], c=colors[ df['Clusters'] ])
# plt.show()
