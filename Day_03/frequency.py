# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:04:09 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
'''str1=input("enter string")
dict1={}
for item in str1:
    dict1[item]=dict1.get(item,0)+1
print(dict1)'''

str1=input("enter string")
dict1={}
for item in str1:
    if item in dict1:
        dict1[item]+=1
    else:
        dict1[item]=1      #dict[key]=value

print(dict1)