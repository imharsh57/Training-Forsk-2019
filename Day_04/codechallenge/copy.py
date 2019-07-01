# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:50:06 2019

@author: Harsh Anand
"""
"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""
with open("E:\\Forsk\\Day_04\\new.txt") as f:
    with open("out(copy of new.txt).txt", "w") as f1:
        for line in f:
            f1.write(line)