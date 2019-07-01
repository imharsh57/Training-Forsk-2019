# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:21:11 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels=['a','e','i','o','u']
li=[]
for item in state_name:
    #print(item)
    state=""
    for i in item.lower():
        if i not in vowels:
            state=state+i
    li.append(state)
print(li)