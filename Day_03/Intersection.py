# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:05:20 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""
list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
l1=set(list1)
l2=set(list2)
list3=l1.intersection(l2)
print(list3)