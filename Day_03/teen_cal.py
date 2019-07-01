# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:59:59 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
def funct(val,counter):
 
    if val in range(13,20):
            
        if val==15 or val==16:
            return (val,counter)
        else:
            counter+=1
            return (0,counter)
    else:
        return (val,counter)
          
            

dict1={}
li=[]
counter=0
summ=0
for i in range(6):
    key=input("Enter key :")
    value=int(input("Enter value :"))
    dict1[key]=value
print(dict1)
for value in dict1.values():
    print(value)
    if counter<3:
        x,counter=funct(value,counter)
        summ=summ+x
    else:
        summ=summ+value
print("sum :",summ)
