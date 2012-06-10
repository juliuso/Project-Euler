#!/usr/bin/env python

# EULER 25
# 
# PROBLEM: 
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

http://projecteuler.net/problem=25
"""

# AUTHOR: jo
# DATE:   08-JUN-2012

import string

a = 0
b = 1
LENGTH = 1000
fib_term = 1

while 1 > 0:
    if len(str(b)) == LENGTH:
        break
    elif len(str(b)) <= LENGTH:
        a, b = b, a+b
        fib_term += 1

print "FIB COUNT: ", fib_term

#ans. 4782