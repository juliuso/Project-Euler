#!/usr/bin/python

# EULER 3
# 
# PROBLEM:
# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number: 600 851 475 143?
#
# AUTHOR: jo
# DATE:   10-MAY-2011

factor = 600851475143
n = 600851475143
i = 2

while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
	
print ("The largest prime number of " + str(factor) + str(" is ")
	+ str(n))