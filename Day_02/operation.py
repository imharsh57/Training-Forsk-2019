# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:56:31 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""
def add(li):
    summ=0
    for i in li:
        summ=summ+i
    return summ
def mult(li):
    multiply=1
    for i in li:
        multiply=multiply*i
    return multiply
def largest(li):
    return max(li)
def smallest(li):
    return min(li)
def remove_duplicates(li):
    li1=[]
    for item in li:
        if item not in li1:
            li1.append(item)
    li1.sort()
    return li1
def sortelement(li):
    li= sorted(li)
    return li
def final(li):
    print("Sum = ",add(li))
    print("Multiply = ",mult(li))
    print("largest = ",largest(li))
    print("smallest = ",smallest(li))
    print("Sorted = ",sortelement(li))
    print("Without Duplicates = ",remove_duplicates(li))

li=list(map(int,input("Enter number").split()))
print(final(li))
