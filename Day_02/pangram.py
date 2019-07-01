# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:38:25 2019

@author: Harsh Anand
"""


"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""

list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str1=input("Enter the string")
print(str1)
str2=[]
str2=str1.split()
print(str2)
li=[]
for item in str2:
    for i in item.lower():
        li.append(i)
li.sort()
li1=[]
for i in li:
    if i not in li1:
        li1.append(i)
print(li1)
print(len(li1))
print(len(list1))
if len(li1)==len(list1):
    print("Pangram")
else:
    print("NOT Pangram")
    
    
'''
li=['a','z','h','b']
li.sort()
print(li)
'''