# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:26:55 2019

@author: Harsh Anand
"""

str1="SRESTART"

loc=str1.find("R")
str2=str1[loc+1:]
print(str1[:loc+1]+str2.replace("R","$"))
    

