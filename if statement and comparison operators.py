# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 09:38:33 2019

@author: student
"""

"""
Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y	

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

is 	Returns true if both variables are the same object	x is y	
is not	Returns true if both variables are not the same object	x is not y
"""
x=9
y=2

if(x is y):
    print("true")
else:
    print("false")
    
if(y>5 or x==9):
    print("Good Logic")