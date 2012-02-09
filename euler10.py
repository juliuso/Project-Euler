#!/usr/bin/python

# EULER 10
# 
# PROBLEM:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

# AUTHOR: jo
# DATE:   01-JUN-2011

# NOTE: Based on sample Sieve of Erathosthenes Python implementation:
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#
# Solution adapted from EULER 7.

import math

maxValue = 2000000
sourceList = list(range(maxValue+1))
maxMultiple = int(math.sqrt(maxValue))
primes = []

for i in xrange(2, maxMultiple):
    if sourceList[i]:
        sourceList[2*i::i] = [None] * (maxValue//i - 1)

for i in sourceList:
    if i != None:
        primes.append(i)

print primes

print sum(primes)-1

#answer: 142913828922