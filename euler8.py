#!/usr/bin/env python

# EULER 8
# 
# PROBLEM:
# Find the greatest product of five consecutive digits
# in the 1000-digit number.
#

# AUTHOR: jo
# DATE:   28-MAY-2011

# mvx24 says large nubmers can be contained with """
# strings accessible the same as lists


import string

f = open('euler8.txt')
g = f.readline()
h = list(g)

answer = 0

for i in xrange(len(h)-4):
	currentProduct = int(h[i])*int(h[i+1])*int(h[i+2])*int(h[i+3])*int(h[i+4])
	
	if currentProduct > answer:
		answer = currentProduct
		
f.close()

print answer