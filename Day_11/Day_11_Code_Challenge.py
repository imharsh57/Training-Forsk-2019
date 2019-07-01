
# Code Challenge 

# Find the mean, median, mode, and range for the following list of values:
# 13, 18, 13, 14, 13, 16, 14, 21, 13
list1=[13, 18, 13, 14, 13, 16, 14, 21, 13]
import numpy as np
x=np.array(list1)  #convert list into nd array
print(np.mean(x))
print(np.median(x))

from scipy import stats
print(stats.mode(x)[0]) #count most occurence in array

x=np.sort(x)
range1=x[-1]-x[0]
print(range1)

#Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8



"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
import numpy as np
input1=np.array(list(map(int,input("Enter number :").split())))
print(input1.shape)
print(input1.reshape(3,3))



"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""
import random
def random1(start,end,total):
    randm=[]
    for i in range(0,total):
        randm.append(random.randint(start,end))
    return randm
start=int(input("enter starting number :"))
end=int(input("enter ending number :"))
total=40
randm1=random1(start,end,total)
from collections import Counter
frequency = Counter(randm1)
print (frequency)
max1=0
for key,value in dict(frequency).items():
    #print (key,value)
    if max1<=value:
        max1=value
for key,value in dict(frequency).items():
    #print (key,value)
    if value==max1:
        print(key)       
        

import numpy as np 
#random.random(shape) – creates arrays with random floats over the interval [0,1].
x = np.random.randint(5,15,size=40)
print (x)
 
counts = np.bincount(x)
"""
x.sort()

x
Out[66]: 
array([ 5,  5,  5,  5,  5,  6,  7,  7,  7,  8,  8,  8,  8,  9, 10, 10, 11,
       11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13,
       14, 14, 14, 14, 14, 14])
counts
Out[67]: array([0, 0, 0, 0, 0, 5, 1, 3, 4, 1, 2, 8, 3, 7, 6], dtype=int64)
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14]
"""
print (np.argmax(counts))   



"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""



import numpy as np
import matplotlib.pyplot as plt
                          #mean, sd, total
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)
print(np.mean(incomes))
print(np.median(incomes))
plt.hist(incomes, normed=True, bins=50)



"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""
import numpy as np
import matplotlib.pyplot as plt
                          #mean, sd, total
incomes = np.random.normal(150, 20, 1000)
print (incomes)
print(np.mean(incomes))
print(np.median(incomes))
print(np.std(incomes))  #standard deviation
print(np.var(incomes))   #variance
plt.hist(incomes, normed=True, bins=100)




