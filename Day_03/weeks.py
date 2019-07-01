# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:15:13 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""
num=tuple(map(str,input("enter Days").split(",")))
num1=list(num)
print(num1)
tp1=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for index,item in enumerate(tp1):
    if item not in num1:
        num1.insert(index,item)
print(tuple(num1))

        