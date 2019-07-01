# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:15:28 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b=['1','2','3','4','5','6','7','8','9','0']
letter=0
digit=0
str1=input("enter string")
for item in str1.lower():
    if item in b:
        digit+=1
    elif item in a:
        letter+=1
print("Digit",digit)
print("Letter",letter)
    