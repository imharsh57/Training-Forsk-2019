# Hangman Letter Game App

"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # import external libraries
    # make a list of word

    # pick a random word

    # draw  spaces
    # take guess
    # draw guessed letters, spaces and strikes
    # print out win / lose

"""
import random
li=['apple','banana','orange','potato','tomato']
guess_c=random.choice(li)
print(guess_c)
guess=input("Guess elelment from list :['apple','banana','orange','potato','tomato'] -->")
if guess==guess_c:
    print(" you guesses the right number You wins and computer lose.")
else:
    print(" you guesses the wrong number You lose and computer wins.")



"""
Challenge 2
    Screen is messy and rolls ups
    Convert the code into function 

    MAJOR REFACTORING OF THE CODE
"""
import random
def random1(li,guess):
    guess_c=random.choice(li)
    print(guess_c)
    if guess==guess_c:
        print(" you guesses the right You wins and computer lose.")
    else:
        print(" you guesses the wrong You lose and computer wins.")
li=['apple','banana','orange','potato','tomato']
guess=input("Guess elelment from list :['apple','banana','orange','potato','tomato'] -->")
random1(li,guess)

"""
Challenge 3
Read the words from a file

"""
with open("mailing.txt","rt") as fp:
    read_files=fp.readlines()
    print(read_files)

"""
Challenge 4
    Get the list of Internet after web scrapping
"""
