# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:51:34 2019

@author: Harsh Anand
"""

#******************* mokevita************* Q1
li=[]
li_1=[]
lii=[]
rlist=[]
rlist1=[]
rlist2=[]
result = []

str1=input("enter string")
n=int(input("enter times"))
r=input("enter rotation and frequency")

for i in r: #split the r
    rlist.append(i)
    
for x in rlist: #seperate the integer value and string value
    try:
        val=int(x)
        rlist1.append(val)
    except ValueError:
        rlist2.append(x)
        
for i in str1:  #seperate the input string  #or  li(str1)
    li.append(i)
a=0  #initialize the rotation variable  

for i in range(len(rlist1)): #rlist1-->rotation value
    if rlist2[i]=="L":
        a=a+rlist1[i]  #if left rotation then added
        print("1 :",a)
        b=li[a]
        result.append(b) #varialbe at rotated index store in list
    elif rlist2[i]=="R":
        a=a-rlist1[i] #if right rotation then subtracted
        print("2 :",a)
        b=li[a]
        result.append(b)
        
join = ''.join(result)   #join the list ini single variable
     
        
li_1.append(str1)   #for check anagram we pass n string after soring in list of list
li_1.append(join)  


def anagram(li_1):
    counter=0
    for i in li_1[0]:
        lii.append(i)
    lii.sort()
    print(lii)
    list1=[]
    for item in li_1:
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
anagram(li_1)

#***************************** q2 codevita *******************************************
print(int_to_en(1649))
def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + ' ' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))