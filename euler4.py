#!/usr/bin/python

numbers = []

x = 0

# n1 is the first set of number 1-99 going from 99 down to 1
for n1 in xrange(999,1,-1):
	# n2 is the second set of numbers pulling in the results of n1 going from n1 down to 1. adding n1 instead of 99 returned a matched result of 9009.
	for n2 in xrange(n1,100,-1):
		# multiply the two numbers to find the palindrone
		x = n1 * n2
		# place those into a list
		numbers.append(x)

# print the list of all multiplied numbers
print str(numbers)

# need to isolate palindrome numbers

# once isolated, find the greatest number in the list