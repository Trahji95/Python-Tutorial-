# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:46:00 2019

@author: student
"""

# Dictionaries in Python
# Jan->January

monthConversions = {"Jan": "January",
                    "Feb": "Febuary",
                    "Mar": "March",
                    "Apr": "April",
                    "Ma": "May",
                    "Jun": "June",
                    "Jly": "July",
                    "Aug": "August",
                    "Set": "September",
                    "Oct": "October",
                    "Nov": "November",
                    "Dec": "December",
                    "year": 2019,}
print(monthConversions["Jan"])
print(monthConversions["year"])
print(monthConversions.get("Jan","Not a valid key"))
print(monthConversions.get("Hezu","Not a valid key"))

# Quicker reference can be done if the dictionaries are done with integers

monthConversions_numbers = {0: "January",
                    1: "Febuary",
                    2: "March",
                    3: "April",
                    4: "May",
                    5: "June",
                    6: "July",
                    7: "August",
                    8: "September",
                    9: "October",
                    10: "November",
                    11: "December",
                    "year": 2019,}