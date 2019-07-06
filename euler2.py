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
# https://projecteuler.net/problem=2
# AUTHOR: jo
# DATE:   10-MAY-2011

if __name__ == '__main__':

    # set variable to store cumulative sum of even value modulus test.
    total = 0

    # create empty list that will store fibonacci numbers to upper bound. 
    f=[]

    # define variables a & b with initial condition for fibonacci sequence 0 and 1.
    a, b = 0, 1

    # while loop generates fibonacci sequence to upper bound 4,000,000.
    while b<4000000:
        # each value including initial conditions added to the list.
        f.append(b)
        # continues looping by adding the previous two numbers to generate the next value.
        a, b = b, a+b  

    # prints the list.
    print(f)

    # performs the mod2 test, if the remainder after division is zero, than it's even.
    for i in f:
        if(i%2==0):
            # if it's even, cumulatively add that value to var total.
            total += i

    # print the result.
    print("The Total is: %r" % total)
