# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 21:13:28 2019

@author: student
"""

# Building a translator

translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation=translation+"g"
        else:
            translation=translation+letter
    return translation
        