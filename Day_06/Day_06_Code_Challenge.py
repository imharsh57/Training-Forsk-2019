

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
'''
li=list(map(int,input("enter list with space seperated :").split(" ")))
count=0
for item in li:
    rev1=item
    rev=0
    while item>0:
        a=item%10
        rev=(rev*10)+a
        item=item//10
    #print(rev)
    if rev==rev1:
        count+=1
            
if count>0:
    print("True")
else:
    print("False")
'''
li=list(map(int,input("enter list with space seperated :").split(" ")))
count=0
lii=[]
for item in li:
    rev1=item
    
    rev=0
    while item>0:
        a=item%10
        rev=(rev*10)+a
        item=item//10
    #print(rev)
    if rev==rev1:
        lii.append(True)
    else:
        lii.append(False)
print(any(lii))

''' solution
user_input = input("Enter space seperated values :").split()

if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")
    '''





"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)

As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.


"""
import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
secret_names = list(map(lambda x: random.choice(code_names), names))
print(secret_names)


"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print (names)



(Hopefully, the secret agents will have good memories and won’t forget each other’s secret code names during the secret mission.)


Rewrite the above code using map.
    

"""
names = ['Mary', 'Isla', 'Sam']


secret_names = list(map(lambda x: hash(x), names))

print (secret_names)



"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""
from functools import reduce
li1=[]
def add(x,y):
    return x+y
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
li=list(filter(lambda x:'height' in x,people))
print(li)
for item in li:
    li1.append(item['height'])
height_total=reduce(add,li1)

print(height_total/len(li))

#solution
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

heights=list(map(lambda x:x['height'],filter(lambda x:'height' in x,people)))
if  (len(heights)>0):
    from operator import add
    avg_height=reduce(add,heights)/len(heights)

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
    
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

"""
def func(itemm):

    itemm=itemm.split()
    a=itemm[0]
    c=float(itemm[-2])*float(itemm[-1])
    if c<100.0:
        c+=10
    #print(c)
    return (a,c)
print("Order Number  Book Title  Author Quantity  Price per Item")
list1=[["34587 Learning Python, Mark Lutz  4 40.95"],["98762 Programming Python, Mark Lutz 5 56.80"],["77226 Head First Python, Paul Barry 3 32.95"],["88112 Einführung in Python3, Bernd Klein  3 24.99" ]]
#print(list1)
for item in list1:
    #print(item)
    for itemm in item:
        print(itemm)
        print(func(itemm))
        
#solution
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
min_order=100
order_summary=list(map(lambda x:(x[0],round(x[2]*x[3],2)),orders))
print(order_summary)
invoice=list(map(lambda x:x if x[1]>min_order else(x[0],x[1]+10),order_summary))
print(invoice)       
    


"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
   Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
      
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
"""
from collections import OrderedDict
dict1= OrderedDict()
invoice = []
orders = [ ['1', ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         ['2', ("5464", 9, 9.99), ("9744", 9, 44.95)],
         ['3', ("5464", 9, 9.99), ("88112", 11, 24.99)],
         ['4', ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
for item in orders:
    #print(item)
    order_no=item[0]
    info=item[1:]
    for element in info:
        #print(element)
        invoice.append([order_no,round(element[1]*element[2],2)])
for new in invoice:
    #print(new)
    dict1[new[0]]=dict1.get(new[0],0)+new[1]
print(dict1)
        
#2nd solution
from functools import reduce
orders = [ ['1', ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         ['2', ("5464", 9, 9.99), ("9744", 9, 44.95)],
         ['3', ("5464", 9, 9.99), ("88112", 11, 24.99)],
         ['4', ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
invoice=list(map(lambda x:[x[0]] + list(map(lambda y:y[1]*y[2],x[1:])),orders))
invoice_total=list(map(lambda x:[x[0]] + [round(reduce(lambda a,b: a+b ,x[1:]),2)],invoice))
    


"""
Code Challenge
  Name: 
    Population Counting
  Filename: 
    Population.py
  Problem Statement:
      
      The given input has a number of rows, each with four fields from a table, containing:

          Rank,City,Population,State or union territory
          1,Mumbai,"12,442,373",Maharashtra


    You are required to output:

        Country, State, Population of the state (obtained by summing up the population of each city in that state)  


    Sample Input

    1,Mumbai,"12,442,373",Maharashtra
    9,Pune,"3,124,458",Maharashtra
    13,Nagpur,"2,405,665",Maharashtra
    6,Chennai,"4,646,732",Tamil Nadu
    59,Salem,"831,038",Tamil Nadu


    Sample Output

    {"key":"India,Tamil Nadu","value":5477770}
    {"key":"India,Maharashtra","value":17972496}


    Explanation

    The population of India,Tamil Nadu is obtained by adding the population of 
    Chennai and Salem. 
    This process is repeated for India,Maharashtra and India,Maharashtra. 


    Refer to population.csv


"""
list1=["1,Mumbai,\"12,442,373\",Maharashtra"]
for item in list1:
    item=item.split()
    print(item)






"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""









