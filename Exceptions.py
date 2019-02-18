# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 22:56:16 2019

@author: student
"""
# Exceptions
import sys
while is_exception = True:
    try:
        value = 10/0
        number = int(input("Enter a number: "))
        is_exception = False
        print(number)
    except ZeroDivisionError:
        print("Error cannot divide by zero")
    except ValueError:
        print("Invalid input")
    except:
        print("Unexpected error")


try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Error cannot divide by zero")
except ValueError:
    print("Invalid input")
except:
    print("Unexpected error:", sys.exc_info()[0])
    

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
