# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:25:31 2019

@author: student
"""

# Building a basic calculator
arithmetic_type = input("Enter M for multiply D for divide A for add or S for subtract: ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

# control flow
if arithmetic_type=="S" or "s": 
        answer=num1-num2
        a_t = "minus"
    
if arithmetic_type=="A" or "a": 
        answer=num1+num2
        a_t = "plus"  
    
if arithmetic_type=="D" or "d": 
        answer=num1/num2
        a_t = "divide" 
    
if arithmetic_type=="M" or "m": 
        answer=num1*num2
        a_t = "times"

print("\n"+str(num1) + " " + a_t +" "+str(num2)+ " is "+str(answer)+".")