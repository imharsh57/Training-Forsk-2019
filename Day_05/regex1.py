# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:46:21 2019

@author: Harsh Anand
"""

"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
import re
i=0
while i<4:
    float1=input("Enter number :")
    i+=1
    result=re.findall(r'[+-.]?\d\.\d',float1)
    if result:
        print("True")
    else:
        print("False")