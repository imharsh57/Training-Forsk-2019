# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:51:16 2019

@author: Harsh Anand
"""



"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
dataset = pd.read_csv('Foodtruck.csv')  

features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 

dataset.plot(x='Population', y='Profit', style='o')  
plt.title('Population vs Profit')  
plt.xlabel('Population')  
plt.ylabel('Profit')  
plt.show()

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

x=3.073
x = np.array(x)
x = x.reshape(1,1)
print (regressor.predict(x))



"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
#1st method
import pandas as pd  
import numpy as np  
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  

features = dataset.iloc[:, :-2].values  
labels_bahubali = dataset.iloc[:, 1].values 
labels_dangal = dataset.iloc[:, -1].values 

from sklearn.linear_model import LinearRegression  
regressor_bahubali = LinearRegression()  
regressor_bahubali.fit(features, labels_bahubali) 

 
regressor_dangal = LinearRegression()  
regressor_dangal.fit(features, labels_dangal) 

x=10
x = np.array(x)
x = x.reshape(1,1)
print ("Bahubali collection on 10th day :",regressor_bahubali.predict(x))
print ("Dangal collection on 10th day :",regressor_dangal.predict(x))

#2nd method

import pandas as pd  
import numpy as np  
dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')  

features = dataset.iloc[:, :-2].values  
labels = dataset.iloc[:, 1:].values 


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

 

x=10
x = np.array(x)
x = x.reshape(1,1)
print ("Bahubali & Dangal collection on 10th day :",regressor.predict(x))

