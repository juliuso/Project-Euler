#!/usr/bin/env python

# EULER 9
# 
# PROBLEM:
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
#     a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# AUTHOR: jo
# DATE:   31-MAY-2011

sum = 1000

for a in xrange(sum):

	for b in xrange(sum):

		for c in xrange(sum):

			if (a**2) + (b**2) == (c**2):

				if a > 0:
					if b > 0:
						if c > 0:
							if a + b + c == 1000:
								print "The triangle sides are: %i, %i, %i" % a, b, c
								print a*b*c
								break

# ans: 31875000
# Additional conditions should be added to prevent returning
# identical solutions, but in a different order.
# (ex. a, b, c == c, b, a)