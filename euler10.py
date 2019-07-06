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
# https://projecteuler.net/problem=10
# AUTHOR: jo
# DATE:   01-JUN-2011

# NOTE: Based on sample Sieve of Erathosthenes Python implementation:
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#
# Solution adapted from EULER 7.

import math

if __name__ == '__main__':

    maxValue = 2000000
    sourceList = list(range(maxValue+1))
    maxMultiple = int(math.sqrt(maxValue))
    primes = []

    for i in range(2, maxMultiple):
        if sourceList[i]:
            sourceList[2*i::i] = [None] * (maxValue//i - 1)

    for i in sourceList:
        if i != None:
            primes.append(i)

    print(primes)

    print(sum(primes)-1)

