# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:23:06 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

str1=input("enter string")
str2=str1[::-1]
print(str2)
'''
str1=input("enter string")
str2=""
for i in str1:
    str2=i+str2
print(str2)
'''