# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:34:57 2019

@author: Harsh Anand
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""
'''
dict1={}
i=0
while i<3:
    num=list(map(str,input("Enter").split(" ")))
    print(num)
    a=len(num)-1
    key=str(' '.join(num[:a]))
    value=int(num[-1])
    dict1[key]=value
    i+=1
    print("key:",key)
    print("value :", value)
print(dict1) 
'''   

from collections import OrderedDict


# make Object of OrderDict
od = OrderedDict()

while True:
    # take items from user as input
    user_input = input("Enter item with price : ")

    if not user_input:
        break
    
    # use split function to get item's price value
    temp = user_input.split()
    price = temp[-1]
    
    # join rest string which is item name
    item = " ".join(temp[:-1])
    
    # Adding and updating price of the item using orderdict function 
    od[item] = od.get(item,0) + int(price)

for key,value in od.items():
    print (key,value)
    