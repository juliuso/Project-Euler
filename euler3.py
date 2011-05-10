#!/usr/bin/python

# EULER 3
# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number: 600 851 475 143?

# A prime is a number that is only divisible by 1 and itself.
# While inefficient to start, the program should find all primes in
# the given range and place them in a list.

# Then, review each element in the list 

# Primes from 1-10: 1, 3, 5, 7

factor = 600851475143
n = 600851475143
i = 2

while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
	
print "The largest prime number of " + str(factor) + str(" is ") + str(n)