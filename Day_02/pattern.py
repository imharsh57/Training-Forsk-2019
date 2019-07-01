# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:56:02 2019

@author: Harsh Anand
"""
"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
n=int(input("enter number for pattern"))

j=n-1
for i in range(n+1):
   print("*"*i) 
for j in range(n,0,-1):  
    print("*"*j)
    
'''
n=int(input("enter number for pattern"))

j=n-1
for i in range(n+1):
   print("*"*i) 
while (j>0):
    print("*"*j)
    j-=1
'''