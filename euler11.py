#!/usr/bin/env python
'''
MIT License

Copyright (c) 2011 Julius O

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
# https://projecteuler.net/problem=11
# AUTHOR: jo
# DATE:   09-JUL-2011

import copy
import os

if __name__ == '__main__':

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
                print(j[y][x], x, y)

    print(largestProduct)