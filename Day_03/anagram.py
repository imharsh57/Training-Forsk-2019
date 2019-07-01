# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:26:02 2019

@author: Harsh Anand
"""

"""
Two words are anagrams if you can rearrange the letters of one to spell the second.  
For example, the following words are anagrams:

 ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']

Hint: How can you tell quickly if two words are anagrams?  
Dictionaries allow you to find a key quickly.  

"""
li=[]
lii=[]
counter=0
while True:
    str1=input("enter string")
    if not str1:
        break
    li.append(str1)

for i in li[0]:
    lii.append(i)
lii.sort()
print(lii)
list1=[]
for item in li:
    for j in item:
        list1.append(j)
    list1.sort()
    #print(list1)
    if list1==lii:
        counter+=1
    else:
        counter=0
    list1.clear()
if counter>0:
    print("anagrams")
else:
    print("NO anagrams")
    

