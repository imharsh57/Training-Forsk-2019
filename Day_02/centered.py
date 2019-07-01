# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:57:05 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""
num=list(map(int,input("enter number should be more than three :").split(",")))
num.sort()
num.pop(0)
num.pop(-1)
print(num)
summ=0
for item in num:
    summ=summ+item
avg=summ//len(num)
print(avg)