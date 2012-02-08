#!/usr/bin/env python

# EULER 21
# 
# PROBLEM: 
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n). If d(a) = b and d(b) = a,
where a != b, then a and b are an amicable pair and each of a and b are
called amicable numbers.

For example, the proper divisors of 220 are:

1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.

The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

http://projecteuler.net/problem=21
"""

# AUTHOR: jo
# DATE:   08-FEB-2012

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
    
    print a, aTotal, b, bTotal, '\n'

    if i == bTotal and i != aTotal:
        if i not in amicable and aTotal not in amicable:
            amicable.append(i)
            amicable.append(aTotal)

print amicable
print sum(amicable)

#ans. 31626