#!/usr/bin/env python

# EULER 20
# 
# PROBLEM: 
"""
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

http://projecteuler.net/problem=20
"""

# AUTHOR: jo
# DATE:   05-FEB-2012

# NOTE: Will calculate factorial with for loop instead of using
# math.factorial()

answer = 1
tally = 0

for i in range(100, 0, -1):
    answer *= i

answer = str(answer)

for i in answer:
    tally += int(i)

print tally

#ans. 648