# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:57:20 2019

@author: Harsh Anand
"""

"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

"""
import re
li=[]
while True:
    email=input("enter email address :")
    if not email:
        break
    else:
        result=re.findall(r'^\w+\_?\w+@+[a-z]+\.+[a-z]',email)
        if result:
            li.append(email)
li=sorted(li)
print(li)   