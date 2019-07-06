#!/usr/bin/env python
'''
MIT License

Copyright (c) 2012 Julius O

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
# https://projecteuler.net/problem=23
# AUTHOR: jo
# DATE:   26-APR-2012

if __name__ == '__main__':

    MAX_RANGE = 28123
    abundants = []
    interval = range(1, MAX_RANGE + 1)

    # If number is abundant, return True.
    def isAbundant(n):
        properDivisors = []
        for i in range(1,n):
            if n % i == 0:
                properDivisors.append(i)
        if n < sum(properDivisors):
            return True

    # If abundant, add the number to abundants[].
    def classifyInt():
        for i in range(1, MAX_RANGE + 1):
            if isAbundant(i) == True:
                abundants.append(i)
        return 0

    # Sum each combination in abundants[], and remove from interval[].
    def sumAndRemove():
        for i in range(len(abundants)):
            for j in range(len(abundants)):
                k = abundants[i] + abundants[j]
                if k <= MAX_RANGE:
                    try:
                        interval.remove(k)
                    except:
                        continue
                else:
                    break
        return 0

    classifyInt()
    sumAndRemove()
    print(sum(interval))

