# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:27:16 2019

@author: Harsh Anand
"""

"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""
import random
secret = random.randint(1,10)
guess = int(input("Guess the number"))
if secret==guess:
    print("player wins and computer lose.")
else:
    print("player lose and computer wins.")
    

#challenge 2 Print the secret number and guess number when Player loses using format function 
import random
secret = random.randint(1,10)
guess = int(input("Guess the number"))
if secret==guess:
    print("player wins and computer lose.")
else:
    print("player lose and computer wins.\n Secret no. is {} & guess no. is {} :".format(secret,guess))
 
    
#challenge 3   Print too HIGH or too LOW messages for bad guesses using elif. 
import random
secret = random.randint(1,10)
guess = int(input("Guess the number"))
if secret==guess:
    print("player wins and computer lose.")
elif guess<0 or guess>10:
    print("Badd Guesses")
else:
    print("player lose and computer wins.\n Secret no. is {} & guess no. is {} :".format(secret,guess))
    

"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""
import random
secret = random.randint(1,10)
print(secret)
guess = int(input("Guess the number"))
while(secret!=guess):
    print("player lose and computer wins.\n Secret no. is {} & guess no. is {} :".format(secret,guess))
    guess = int(input("Guess the number"))
if(secret==guess):    
    print("Correct Guess no. player wins and computer lose.")


"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""
import random
secret = random.randint(1,10)
print(secret)
guess = int(input("Guess the number"))
i=1
while(secret!=guess):
    print("player lose and computer wins.\n Secret no. is {} & guess no. is {} :".format(secret,guess))
    if(i==6):
        print("You have limit the max tries i.e 6")
        break
    i+=1
    guess = int(input("Guess the number"))
if(secret==guess):    
    print("Correct Guess no. player wins and computer lose.")


"""
Challenge 6
    Print the number of tries left 
"""
import random
secret = random.randint(1,10)
print(secret)
guess = int(input("Guess the number"))
i=6
while(secret!=guess):
    print("player lose and computer wins.\n Secret no. is {} & guess no. is {} :".format(secret,guess))
    if(i==1):
        print("You have limit the max tries i.e 6")
        break
    print("You have {} tries left".format(i-1))
    i-=1
    guess = int(input("Guess the number"))
if(secret==guess):    
    print("Correct Guess no. player wins and computer lose.")
    
    

"""
Challenge 7
    Lets give user the option to play again
"""
import random
secret = random.randint(1,10)
print(secret)
guess = int(input("Guess the number"))
i=6
while(secret!=guess):
    print("player lose and computer wins.\n Secret no. is {} & guess no. is {} :".format(secret,guess))
    if(i==1):
        r1=input("Do You want to play again ?? Yes/No:")
        if(r1=="Yes"):
            i=6
        else:
            print("You have limit the max tries i.e 6")
            break
    print("You have {} tries left".format(i-1))
    i-=1
    guess = int(input("Guess the number"))
if(secret==guess):    
    print("Correct Guess no. player wins and computer lose.")




"""
Challenge 8
    Catch when someone submits a non integer
"""
import random
choice = True
while choice:
    try:
        a = input('Enter number')
