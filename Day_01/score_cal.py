# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:55:26 2019

@author: Harsh Anand
"""
assign1=int(input("enter masrks of first assignmnt :"))
assign2=int(input("enter masrks of second assignmnt :"))
assign3=int(input("enter masrks of third assignmnt :"))
exam1=int(input("enter masrks of first exam :"))
exam2=int(input("enter masrks of second exam :"))
weighted_score=(assign1+assign2+assign3) * 0.1 +(exam1+exam2)*0.35
print(weighted_score)