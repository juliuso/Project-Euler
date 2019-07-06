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
# https://projecteuler.net/problem=18
# AUTHOR: jo
# DATE:   17-OCT-2011

if __name__ == '__main__':

    triangle = [
                [75],\
                [95, 64],\
                [17, 47, 82],\
                [18, 35, 87, 10],\
                [20, 4, 82, 47, 65],\
                [19, 1, 23, 75, 3, 34],\
                [88, 2, 77, 73, 7, 63, 67],\
                [99, 65, 4, 28, 6, 16, 70, 92],\
                [41, 41, 26, 56, 83, 40, 80, 70, 33],\
                [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],\
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],\
                [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],\
                [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],\
                [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],\
                [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
                ]

    # Returns last row number of any array.
    triangleLength = len(triangle[-1]) - 1

    # Sets the initial condition for the dictionary.
    dict = { (0,0) : triangle[0][0] }

    # Placeholders for the max value, and its location.
    maxInLastRow = 0
    max_Y = 0
    max_X = 0

    # The function doing the heavy lifting.
    def getAnswer(y, x):
        global dict
        if (y,x) in dict:
            return dict[(y,x)]
        else: 
            if x == 0:        # First element of each row(y).
                dict[(y,x)] = triangle[y][x] + getAnswer(y-1, x)
            elif x == y:    # Last element of each row(y).
                dict[(y,x)] = triangle[y][x] + getAnswer(y-1, x-1)
            else:            # Remaining non-outer edge cases
                dict[(y,x)] = triangle[y][x] + max(getAnswer(y-1, x-1), getAnswer(y-1, x))
        return dict[(y,x)]

    # This loop sets the range to iterate over all elements in the last row.
    for i in range(len(triangle[-1])):
        getAnswer(triangleLength, i)

    # Iterates through the last row to find the max, and its location.
    for i in range(len(triangle[-1])-1):
        if dict[(triangleLength,i)] > maxInLastRow:
            maxInLastRow = dict[(triangleLength,i)]
            max_Y = triangleLength
            max_X = i

    print("The maximum in the last row is %(maxInLastRow)i \
    at location (%(max_Y)i,%(max_X)i)." % \
        {"maxInLastRow": maxInLastRow, "max_Y": max_Y, "max_X": max_X})

    #notes: First time use of dictionary data structure, and recursion.