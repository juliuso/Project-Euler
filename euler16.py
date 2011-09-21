#!/usr/bin/env python

# EULER 16
# 
# PROBLEM:
# 
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?
#
# http://projecteuler.net/index.php?section=problems&id=16

# AUTHOR: jo
# DATE:   20-SEP-2011

value = 2**1000
stringValue = str(value)
valueSum = 0

for i in range(len(stringValue)):
	valueSum += int(stringValue[i])

print "The sum of %(value)d is: \n\n%(valueSum)s" % \
		{"value": value, "valueSum": valueSum}

# ans. 1366