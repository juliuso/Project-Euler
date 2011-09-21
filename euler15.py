#!/usr/bin/env python

# EULER 15
# 
# PROBLEM:
# 
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without
# backtracking) to the bottom right corner.

# How many routes are there through a 20x20 grid?
#
# http://projecteuler.net/index.php?section=problems&id=15

# I'll solve this problem through the Combinatorics approach of 40-Choose-20, hence:
# n! / (n-r)!r!

import math

m = math

print "The answer is: %s" % str(m.factorial(40) / ((m.factorial(40-20) * m.factorial(20))))

raw_input('Press any key to continue.')

# AUTHOR: jo
# DATE:   20-SEP-2011
		
# ans. 137846528820