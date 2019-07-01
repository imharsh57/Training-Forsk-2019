# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:48:29 2019

@author: Harsh Anand
"""

for i in range(1,101):
    if i%5==0 and i%3==0:
        print("FizzBuzz")
        
    elif i%3==0:
        print("Fizz")
        
    elif i%5==0:
        print("Buzz")
        
    
    else:
        print(i)
    