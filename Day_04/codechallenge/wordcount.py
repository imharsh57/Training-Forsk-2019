# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:20:04 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
filename=str(input("enter filename with format :"))
char_count=0
unique_count=0
character=['a','b','c','d','e','f','g','h','i','j','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0]
with open(filename,"rt") as fp:
    fp_read=fp.readlines()
    #print(fp_read)
    li=[]
    lii=[]
    li=fp_read
    #print(li)
print("number of lines :",len(li))
for item in li:
    for char in item:
        char_count+=1
        if char not in character:
            unique_count+=1
        
for item in li:
    #print(item)
    for char in item.split(" "):
        #print(char)
        char=char.replace('\n','')           
        lii.append(char)

                        
lii=''.join(lii)
#print("lii",lii)       
print("Total no of words included by whitespace :",char_count)
print("Total no of words seperated by whitespace :",len(lii))
print("Total no of unique words :",unique_count)