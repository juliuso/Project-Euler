#!/usr/bin/env python

# EULER 11
# 
# PROBLEM:
# 
# In the 20x20 grid below, four numbers along a diagonal line have been marked in red.
# (see euler11.txt)
# http://projecteuler.net/index.php?section=problems&id=11
# The product of these numbers is 26  63  78  14 = 1788696.

# What is the greatest product of four adjacent numbers in any direction (up,
# down, left, right, or diagonally) in the 2020 grid?

# AUTHOR: jo
# DATE:   09-JUL-2011

#import string
import copy
import os

f = open('euler11.txt')
g = copy.copy(f.readlines())
f.close()
h = []
j = []

for i in g:
    i = i.rstrip('\n')
    h.append(i)

for i in h:
    i = i.split()
    j.append(i)

for k in range(20):
    for l in range(20):
        j[k][l] = int(j[k][l])

def maxProduct(x,y):

    position = ''

    # calculate left
    if x >= 3 and x <= 16:
        left = j[y][x] * j[y][x-1] * j[y][x-2] * j[y][x-3]
    else:
        left = 0
    
    # calculate right
    if x >= 3 and x <= 16:
        right = j[y][x] * j[y][x+1] * j[y][x+2] * j[y][x+3]
    else:
        right = 0
    
    # calculate up
    if y >= 3 and y <= 16:
        up = j[y][x] * j[y-1][x] * j[y-2][x] * j[y-3][x]
    else:
        up = 0
    
    # calculate down
    if y >= 3 and y <= 16:
        down = j[y][x] * j[y+1][x] * j[y+2][x] * j[y+3][x]
    else:
        down = 0
    
    # calculate diagNE
    if y >= 3 and x <= 16:
        diagNE = j[y][x] * j[y-1][x+1] * j[y-2][x+2] * j[y-3][x+3]
    else:
        diagNE = 0
    
    # calculate diagSE
    if y <= 16 and x <= 16:
        diagSE = j[y][x] * j[y+1][x+1] * j[y+2][x+2] * j[y+3][x+3]
    else:
        diagSE = 0
    
    # calculate diagNW
    if y >= 3 and x >= 3:
        diagNW = j[y][x] * j[y-1][x-1] * j[y-2][x-2] * j[y-3][x-3]
    else:
        diagNW = 0
    
    # calculate diagSW
    if x >= 3 and y <= 16:
        diagSW = j[y][x] * j[y+1][x-1] * j[y+2][x-2] * j[y+3][x-3]
    else:
        diagSW = 0

    return max(left, right, up, down, diagNE, diagSE, diagNW, diagSW)
    
largestProduct = 0
position = [[]]
for x in range(20):
    for y in range(20):
        z = maxProduct(x,y)
        if z > largestProduct:
            largestProduct = z
            print j[y][x], x, y

print largestProduct

# ans: 70600674