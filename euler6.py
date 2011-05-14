#!/usr/bin/python

# EULER 6
# 
# PROBLEM:
# The sum of the squares of the first ten natural numbers is, 
# 	1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#	(1 + 2 + ... + 10)^2 = 55^2  = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

# AUTHOR: jo
# DATE:   14-MAY-2011

import math

squares = []
squareOfSum = []

for i in xrange(1, 101):
	squares.append(i**2)
	squareOfSum.append(i)

print sum(squareOfSum[:])**2 - sum(squares[:])