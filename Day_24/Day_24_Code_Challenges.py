"""
Q1. (Create a program that fulfills the following specification.)

Import Crime.csv File.

    Perform dimension reduction and group the cities using k-means based on Rape, Murder and assault predictors.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('crime_data.csv')
features = dataset.drop(['UrbanPop','State'],axis=1)

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
#**************************************************************************

from sklearn.cluster import KMeans

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

"""# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features = sc.fit_transform(features)
"""


plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'High crime')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Medium')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Low crime')
#center a/c to column 0 & 1

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')

plt.title('Clusters of datapoints')
plt.xlabel('P1 feature')
plt.ylabel('P2 feature')
plt.legend()
plt.show()


"""
Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).



    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.
"""
from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
iris = pca.fit_transform(iris)
#**************************************************************************

from sklearn.cluster import KMeans

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(iris)


import matplotlib.pyplot as plt

plt.scatter(iris[pred_cluster == 0, 0], iris[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(iris[pred_cluster == 1, 0], iris[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(iris[pred_cluster == 2, 0], iris[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
#center a/c to column 0 & 1

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')

plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()




"""
Q3. Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""
import pandas as pd
dataset = pd.read_csv("data.csv")

country = dataset['Country'].dropna().value_counts()
print(country)

classification = dataset['Classification'].dropna().value_counts()
print(classification.head(2))

artist = dataset['Artist Role'].dropna().value_counts()
print(artist)


culture = dataset['Culture'].dropna().value_counts()
print(culture.head(2))



