#!/usr/bin/env python
#INCOMPLETE SOLUTION. CODE MISSING.
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
# https://projecteuler.net/problem=15
# AUTHOR: jo
# DATE:   20-SEP-2011

if __name__ == '__main__':

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
[x][y]    [x+1][y]    [x+2][y]      [x+2][y+1]    [x+2][y+2]

[x][y]    [x][y+1]    [x+1][y+1]    [x+2][y+1]    [x+2][y+2]
[x][y]    [x][y+1]    [x+1][y+1]    [x+1][y+2]    [x+2][y+2]
[x][y]    [x][y+1]    [x][y+2]      [x+1][y+2]    [x+2][y+2]
"""
