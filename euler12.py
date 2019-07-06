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
# https://projecteuler.net/problem=12
# AUTHOR: jo
# DATE:   20-OCT-2011

if __name__ == '__main__':

    numberOfDivisors = 500
    initial = 0
    while 1 > 0:
        divisorCount = 0
        initial += 1
        triangle = sum(range(initial))

        for i in range(1, int((triangle+1)**0.5)):
            if triangle% i == 0:
                divisorCount += 2
            else:
                continue

        if divisorCount < numberOfDivisors:
            print(divisorCount)
            continue
        else:
            if divisorCount >= numberOfDivisors:
                print("The triangle number is: %i" % triangle)
                print("It has %i divisors\n" % divisorCount)

                break

#notes: The key is to limit the upper-bround range of the for loop
#to the square-root of the triangle number. Because factors come in pairs,
#we test the lower half of the range. Values that divide without remainder
#are counted twice to account for the corresponding pair value.