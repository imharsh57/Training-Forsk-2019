# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:52:48 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

def translate(str1):
    consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    li=[]
    for item in str1:
        if item in consonant:
            li.append(item+"o"+item)
        else:
            li.append(item)
    return li
str1=input("enter string :")
a=translate(str1)
b=''.join(a)
print(b)