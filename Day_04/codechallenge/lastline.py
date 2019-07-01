# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:00:42 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""
name=str(input("Enter name of file with extension :"))
with open(name,mode='rt') as fp:
    print(fp.readlines()[-1])
    

