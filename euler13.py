#!/usr/bin/env python

# EULER 13
# 
# PROBLEM:
# 
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.

# (see euler13.txt)
# http://projecteuler.net/index.php?section=problems&id=13

# AUTHOR: jo
# DATE:   18-JUL-2011

import copy
import os

f = open('euler13.txt')
g = copy.copy(f.readlines())
f.close()
h = []
j = []
for i in g:
	i = i.rstrip('\n')
	i = int(i)
	h.append(i)


total = 0L
for i in h:
	i += 1
	total += i

j.append(total)

print j[0:10]

# Don't think it's possible to slice a long.

#ans: 5537376230