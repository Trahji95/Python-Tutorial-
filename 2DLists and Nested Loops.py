# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:19:11 2019

@author: student
"""


number_list = [1,2,3,4,5,6,7,8,9,0]
number_grid = [[1,2,3],[4,5,6],[7,8,9],[0]]
nList1 = [1,2,3]
nList2 = [4,5,6]
nList3 = [7,8,9]
nList4 = [0]
number_grid = [nList1,nList2,nList3,nList4]
print(number_grid[0][2])

for row in number_grid:
    print(row)
    
for row in number_grid:
    for element in row:
        print(element)

