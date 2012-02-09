#!/usr/bin/env python

# EULER 15
# 
# PROBLEM:
# 
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without
# backtracking) to the bottom right corner.

# How many routes are there through a 20x20 grid?
#
# http://projecteuler.net/index.php?section=problems&id=15

# AUTHOR: jo
# DATE:   20-SEP-2011

steps = 4

grid = [[1,1,1],\
        [1,1,1],\
        [1,1,1]]

paths = 0

def getRoutes(xTerm, yTerm):
    path = []
    
    while len(path) < 4:
        for x in grid:
            
    xTerm, YTerm-1
    xTerm-1, YTerm


"""
[x][y]    [x+1][y]    [x+1][y+1]    [x+2][y+1]    [x+2][y+2]
[x][y]    [x+1][y]    [x+1][y+1]    [x+1][y+2]    [x+2][y+2]
[x][y]    [x+1][y]    [x+2][y]    [x+2][y+1]    [x+2][y+2]

[x][y]    [x][y+1]    [x+1][y+1]    [x+2][y+1]    [x+2][y+2]
[x][y]    [x][y+1]    [x+1][y+1]    [x+1][y+2]    [x+2][y+2]
[x][y]    [x][y+1]    [x][y+2]    [x+1][y+2]    [x+2][y+2]
"""


# ans. 137846528820