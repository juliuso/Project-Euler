#!/usr/bin/python

# EULER 7
# 
# PROBLEM:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10001st prime number?

# AUTHOR: jo
# DATE:   23-MAY-2011

# NOTE: Based on sample Sieve of Erathosthenes Python implementation:
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math

maxValue = 2000000
sourceList = list(range(maxValue+1))
maxMultiple = int(math.sqrt(maxValue))
primes = []

for i in xrange(2, maxMultiple+1):
    if sourceList[i]:
        sourceList[2*i::i] = [None] * (maxValue//i - 1)

for i in sourceList:
    if i != None:
        primes.append(i)

print "Length of primes list: %i" % len(primes)
print primes[10001 + 1]

#answer: 104743