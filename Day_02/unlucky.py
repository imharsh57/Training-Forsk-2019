# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:23:22 2019

@author: Harsh Anand
"""


"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""
num=list(map(int,input("Enter number :").split(",")))
print(num)
li=[]
for i in range(0,len(num)):
    if num[i]!=13:
        if num[i-1]!=13:
            li.append(num[i])
print(li)
summ=0
for item in li:
    summ=summ+item
print(summ)     
