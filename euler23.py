#!/usr/bin/env python

# EULER 23
# 
# PROBLEM: 
"""
A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number. For example, the sum
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper
divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be
shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the
sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be
written as the sum of two abundant numbers.

http://projecteuler.net/problem=23
"""

# AUTHOR: jo
# DATE:   26-APR-2012

MAX_RANGE = 28123
abundants = []
interval = range(1, MAX_RANGE + 1)

# If number is abundant, return True.
def isAbundant(n):
   properDivisors = []
   for i in xrange(1,n):
       if n % i == 0:
           properDivisors.append(i)
   if n < sum(properDivisors):
       return True

# If abundant, add the number to abundants[].
def classifyInt():
   for i in xrange(1, MAX_RANGE + 1):
       if isAbundant(i) == True:
           abundants.append(i)
   return 0

# Sum each combination in abundants[], and remove from interval[].
def sumAndRemove():
   for i in xrange(len(abundants)):
       for j in xrange(len(abundants)):
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
print sum(interval)

#ans. 4179871