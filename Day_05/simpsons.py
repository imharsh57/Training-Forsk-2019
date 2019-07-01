# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:00:27 2019

@author: Harsh Anand
"""

"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement: (simpsons_phone_book.txt)
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
"""
'''
import re
li=[]
with open("simpsons_phone_book.txt","rt") as fp:
    file_read=fp.readlines()
    li=file_read
#print(li)
for index,item in enumerate(li):
    #print(item)
    if item[0]=='J':
        #print(item[0])
        #print(index)
        #print(li[index])
'''
import re
li=[]
with open("simpsons_phone_book.txt","rt") as fp:
    file_read=fp.readlines()
    li=file_read
#print(li)
for index,item in enumerate(li):      
        result=re.findall(r'^[J][a-z]+\s+Neu\s+\d+\-+\d+',item)        
        if result:
            print(index,result)
       