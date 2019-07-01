"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and
 the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    
    Perform K-means clustering again to further distinguish speeding drivers from
    those who follow speed limits, in addition to the rural vs. urban division.
    
    Label accordingly for the 4 groups.
"""
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("deliveryfleet.csv")

features = dataset.iloc[:, [1, 2]].values

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1-->Rural')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2-->urban')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance features')
plt.ylabel('Speeding features')
plt.legend()
plt.show()


#****************************************************************************
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Rural ')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Rural overspeeding')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'black', label = 'Urban')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'green', label = 'urban overspeeding')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance features')
plt.ylabel('Speeding features')
plt.legend()
plt.show()





"""
Q2. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.
"""
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("tshirts.csv")

features = dataset.iloc[:, [1, 2]].values
plt.scatter(features[:,0], features[:,1])
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)

# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Large')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Medium')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'black', label = 'Small')


plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
#centroid is used to provide size of specific small,medium,large
plt.title('Clusters of datapoints')
plt.xlabel('Heights')
plt.ylabel('Weights')
plt.legend()
plt.show()






"""
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
"""
import pandas as pd
import matplotlib.pyplot as plt
import re
dataset = pd.read_csv("monster_com-job_sample.csv")
dataset = dataset.iloc[:,[8,9,11,12]]


#drop complete row of which nan is present in organization column
dataset = dataset.dropna(subset = ['organization','sector'])


dataset = dataset.reset_index()
#reset index is created in new column so drop old index column
dataset = dataset.drop('index',axis=1)

#check the organization for loaction if available then swap
def check_location(value):
    if re.search(r', [A-Z]{2}',value):
        return True
    else:
        return False
    
for i in range(len(dataset)):
    if check_location(dataset.iloc[i,1]):
        temp = dataset.iloc[i,0]
        dataset.iloc[i,0] = dataset.iloc[i,1]
        dataset.iloc[i,1] = temp


#*****************************************************************************  
        #drop length or waste details
fakedetails = []
for i in range(len(dataset)):
    if len(dataset.iloc[i,0])>40:
        fakedetails.append(i)
    if len(dataset.iloc[i,1])>40:
        fakedetails.append(i)
    if len(dataset.iloc[i,3])>40:
        fakedetails.append(i)

dataset.drop(labels=fakedetails,axis=0,inplace=True) 
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
dataset = dataset.reset_index()
dataset = dataset.drop('index',axis=1)

#*****************************************************************************
    #drop pincode
def pin_code(value):
    if re.search(r'\d',value):
        return True
    else:
        return False

for i in range(len(dataset)):
    if pin_code(dataset.iloc[i,0]):
        dataset.iloc[i,0] = dataset.iloc[i,0][:-6]

#removing blank address which are created after previous processes ********************
nolocation = []
for i in range(len(dataset)):
    if len(dataset.iloc[i,0])==0:
        nolocation.append(i)
dataset.drop(labels=nolocation,axis=0,inplace=True) 
dataset = dataset.reset_index()
dataset = dataset.drop('index',axis=1)

#*******************************************************************************
 '''which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?'''
 
print("Sector :",dataset['sector'].value_counts())

'''  ########### or  #############
from collections import Counter
Counter(dataset.sector).most_common()'''

print("organization :",dataset['organization'].value_counts())
print("Location :",dataset['location'].value_counts())

#####################################################################################
dataset1 = dataset[dataset['salary'].notnull()]
#************* or **********************************************
dataset1 = dataset.dropna(subset = ['salary'])
salary = dataset1['salary'].tolist()  # or dataset1.salary.tolist() --> store the salary in list

dataset1 = dataset1.reset_index()
dataset1 = dataset1.drop('index',axis=1)

year = []
month = []
not_salary = []
for i in range(len(dataset1)):
    try:
        