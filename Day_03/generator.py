# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:09:57 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
num=list(map(int,input("enter number").split(",")))
print(num)
print(tuple(num))