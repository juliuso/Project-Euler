#!/usr/bin/python

# EULER 5
# 
# PROBLEM:
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?
#
# AUTHOR: jo
# DATE:   10-MAY-2011

import math

factors =[]

maxBound = 20

#for i in xrange(start, stop):
#	numbers.append(++i)

for i in xrange(1,math.factorial(maxBound)+1,1):
	if (i%20==0
		and i%19==0
		and i%18==0
		and i%17==0
		and i%16==0
		and i%15==0
		and i%14==0
		and i%13==0
		and i%12==0
		and i%11==0
		and i%10==0
		and i%9==0
		and i%8==0
		and i%7==0
		and i%6==0
		and i%5==0
		and i%4==0
		and i%3==0
		and i%2==0
		and i%1==0):
			factors.append(i)
			break
		
print "The factor is: " + str(factors[0])

#answer: 232792560