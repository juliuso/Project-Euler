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
# https://projecteuler.net/problem=21
# AUTHOR: jo
# DATE:   08-FEB-2012

if __name__ == '__main__':

    amicable = []

    def findDivisors(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return divisors

    for i in range(1, 10000):
        a = findDivisors(i)
        aTotal = sum(a)
        b = findDivisors(aTotal)
        bTotal = sum(b)
        
        print(a, aTotal, b, bTotal, '\n')

        if i == bTotal and i != aTotal:
            if i not in amicable and aTotal not in amicable:
                amicable.append(i)
                amicable.append(aTotal)

    print(amicable)
    print(sum(amicable))
