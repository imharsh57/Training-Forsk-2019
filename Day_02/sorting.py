# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:12:34 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Sorting
  Filename: 
    sorting.py
  Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score
  Input: 
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
  Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
"""

def tuple_sort(li):
    return sorted(li)
li=[]
for i in range(0,5):
    inputdetail=tuple(map(str,input("Enter name,age,score").split(",")))
    li.append(inputdetail)
print(li)
print(tuple_sort(li))

