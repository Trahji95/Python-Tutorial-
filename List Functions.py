# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:25:40 2019

@author: student
"""
# List Functions
friends = ["Sasuke","Obito","Kakashi","Rin","Blue Beast","Lord 3rd"]
random_list = ["Hashirama", 5.0 , True , 'A']
lucky_numbers  = [3,6,9,27,19,10,81,90,91,95,99]

friends.extend(lucky_numbers)
print(friends)

friends.append("Assasins Creed")
print(friends)

friends.insert(4,"My Will")
print(friends)

friends.remove(99)
print(friends)

friends.pop() # removes last value in the list by default
friends.clear() # clears the list

friends.index("Sasuke") #returns the position of this element in the list if its there

my_list = [1,1,3,4,5,6,1,3,34]
print(my_list.count(1)) # counts the number of times 1 appears in list
print(my_list.sort())
print(my_list.reverse())

mysecond_list = my_list.copy() # stores value of one list into a new variable




"""
append adds its argument as a single element to the end of a list.
The length of the list itself will increase by one. 
extend iterates over its argument adding each element to the list, extending the list.
The length of the list will increase by however many elements were in the iterable argument.
example: a.extend([4,5,6]) extended a = [1,2,3,4,5,6]
example: a.append([4,5,6]) appended a = [1,2,3,[4,5,6]]
"""