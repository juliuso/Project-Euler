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
# https://projecteuler.net/problem=5
# AUTHOR: jo
# DATE:   10-MAY-2011

import math

if __name__ == '__main__':

    factors = []

    maxBound = 20

    for i in range(1,math.factorial(maxBound)+1,1):
        if (i%20==0
            and i%19==0
            and i%18==0
            and i%17==0
            and i%16==0
            and i%15==0
            and i%14==0
            and i%13==0
            and i%12==0
            and i%11==0
            and i%10==0
            and i%9==0
            and i%8==0
            and i%7==0
            and i%6==0
            and i%5==0
            and i%4==0
            and i%3==0
            and i%2==0
            and i%1==0):
                factors.append(i)
                break
            
    print("The factor is: " + str(factors[0]))

