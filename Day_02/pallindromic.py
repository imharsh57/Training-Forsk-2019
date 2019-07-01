# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:05:52 2019

@author: Harsh Anand
"""
"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

def palin(n):
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev

num=list(map(int,input("Eneter number").split()))
print(num)
count=0
'''for i in num:
    print(palin(i))'''
for item in num:
    print(item)
    if item > 0:
        if item==palin(item): 
            count+=1
        
    else:
        count=0
if count>0:
    print("True")
else:
    print("False")