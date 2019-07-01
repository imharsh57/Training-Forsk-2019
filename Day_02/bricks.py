# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:08:34 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""

num=list(map(int,input("Enter 1st element--> small bricks,2nd element-->big bricks and 3rd element-->target. :").split()))
print(num)
tot1=1*num[0]
tot2=5*num[1]
tot=tot1+tot2
if tot>=num[2]:
    print("True")
else:
    print("False")