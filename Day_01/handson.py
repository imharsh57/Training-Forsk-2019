# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:10:31 2019

@author: Harsh Anand
"""
# Print all the numbers from 1 to 10 using condition in while loop

i=1
while(i<11):
    print(i)
    i+=1

#Print all the numbers from 1 to 10 using while True loop

x=1
while(True):
    print(x)
    x+=1
    if x==11:
        break

#Print all the even numbers from 1 to 10 using condition in while loop

i=2
while(i<11):
    if(i%2==0):
        print("Even number",i)
    i+=1

#Print all the even numbers from 1 to 10 using while True loop

i=2
while(True):
    if(i%2==0):
        print("Even number",i)
    if i==11:
        break
    i+=1

#Print all the odd numbers from 1 to 10 using condition in while loop

i=1
while(i<11):
    if(i%2!=0):
        print("odd number",i)
    i+=1

#Print all the odd numbers from 1 to 10 using while True loop

i=1
while(True):
    if i==11:
        break
    if(i%2!=0):
        print("odd number",i)
    
    i+=1
