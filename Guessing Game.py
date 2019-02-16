# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 11:18:30 2019

@author: student
"""

# Guessing Game
from random import randint
user_guess=int(0)
guesses_left=int(5)
out_of_guesses = False   # boolean to determine if the game can be continued for whatever reason
my_rand = randint(1,100) # random number between 1 and 100

def check(): # function checks to see if user_guess is equal to my_rand
    if user_guess == my_rand:
        out_of_guesses=True
    else:
        guesses_left-=1

while out_of_guesses== False:
    user_guess=input("Enter a guess between 1 and 100: ")
    if (user_guess<my_rand):
        check()
        print("Your guess is too low you have" + guesses_left + "guesses left.")
    elif (user_guess>my_rand):
        check()
        print("Your guess is too high you have" + guesses_left + "guesses left.")
    else:
        check()
        print("Great job you did it, and in " + guesses_left + "guesses, maybe " + guesses_left + " and " + my_rand + "are your lucky numbers.")

