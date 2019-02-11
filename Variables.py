# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 21:24:22 2019

@author: student
"""
# Variables
print("There was once a man named John")
print("He was 35 years old")
print("This man liked being clled John")
print("But he hated being 35")
# Variable substitution 

character_name1 = "John"
character_age = "35"
print("There was once a man named " +character_name1+ ",")
print("he was "+character_age+" years old.")
print("This man liked being called "+character_name1+".")
print("But he hated being " +character_age+ ".")

# other datatypes numbers, boolean, and strings
character_name2 = "Tom"
Tom_age = "50.50"
isMale = True

# Tell a story with Tom


# Working with Strings
print("Giraffe \nAcademy")
print("")
print("\"Can't believe it smells this good\"\n-Tom Ford")
# String functions

phrase = "Giraffe Academy"
print(phrase)
print(phrase+" concatenation")
print(phrase.lower().islower())
print(phrase.upper())

# Length of Strings and indexing
print(len(phrase))
print(phrase[4])
print(phrase.index("e"))
print(phrase.index("Acad"))
# output: print(phrase.index("X")) is ValueError: substring not found
phrase.replace("Giraffe","Gorilla")
print(phrase)
# hence doesnt change the value of phrase in memory
print(phrase.replace("Giraffe","Gorilla")
)