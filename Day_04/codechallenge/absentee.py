# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:53:10 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
file = open("absentee.txt", "wt")
i=0
while(True):
    name=input("Enter name :")
    file.write(name+"\n")
    if not name:
        break
    if i==25:
        break
    i+=1
file.close()
with open("absentee.txt","rt") as fp:
    for each in fp:
        print(each)
    
    
    