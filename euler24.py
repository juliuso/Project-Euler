#!/usr/bin/env python
#NOT WORKING
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
# https://projecteuler.net/problem=24
# AUTHOR: jo
# DATE:   30-APR-2012

# REVISIT THIS PROBLEM, MAY NOT BE FINISHING.

if __name__ == '__main__':

    def ithPermutation(n, i):
        j = 0
        k = 0
        fact = [None]
        perm = [None]
        
        # compute factorial numbers
        fact[k] = 1
        while (k + 1 < n):
            fact[k] = fact[k - 1] * k
        
        # compute factorial code
        for i in range(0, k + 1):
            if k < n:
                perm[k] = i / fact[n - 1 - k]
                i = i % fact[n - 1 - k]
        
        # readjust values to obtain the permutation
        # start from the end and check if preceding values are lower
        for k in range(n - 1, k - 1):
            if k > 0:
                for j in range(k - 1, j - 1):
                    if j >= 0:
                        if perm[j] <= perm[k]:
                            perm[k] += 1

        # print permutation
        for k in range(0, k + 1):
            if k < n:
                print(perm[k])

    ithPermutation(10, 1000000)