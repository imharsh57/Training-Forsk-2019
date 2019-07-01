# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:43:03 2019

@author: Harsh Anand
"""

"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 

"""
li=[]
for i in range(0,21):
    li.append(i)
print(li)
print(li[0::2])
print(li[1::2])



"""
# Make a function to find whether a year is a leap year or no, return True or False 

"""
def leap(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        print("True")
    else:
        print("False")
year = int(input("Enter year"))
leap(year)


"""
# Make a function days_in_month to return the number of days in a specific month of a year
"""
def month(year,m):
    list1=["January","March","May","July","August","October","December"]
    list2=["April","June","September","November"]
    
    if m in list1:
        print("31 days")
    elif m in list2:
        print("30 days")
    else:
        if(year%4==0 and year%100!=0 or year%400==0):
            print("29 days")
        else:
            print("28 days")
year = int(input("Enter year"))

m =input("enter month")
month(year,m)


