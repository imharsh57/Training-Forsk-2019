# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:21:16 2019

@author: Harsh Anand
"""


"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
'''
romeo.txt
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
'''
dict1={}
with open('E:\\Forsk\\Day_04\\romeo.txt', mode='rt') as file :
   file_contents = file.read()
   print (file_contents)
   li=list(map(str,file_contents.split(" ")))
   for item in li:
       item=item.replace('\n','')
       
       if item in dict1:
           dict1[item]+=1
       else:
           dict1[item]=1  

print(dict1)