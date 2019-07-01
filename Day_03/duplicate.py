# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:08:06 2019

@author: Harsh Anand
"""


"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""
list1 = [12,24,35,24,88,120,155,88,120,155]
list2=[]
for item in list1:
    if item not in list2:
        list2.append(item)
print(list2)