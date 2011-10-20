#!/usr/bin/env python

# EULER 67
# 
# PROBLEM:
# 
# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is 23.

#     3
#    7 4
#   2 4 6
#  8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

""""See euler67.txt file"""

# AUTHOR: jo
# DATE:   20-OCT-2011

import copy

f = open('euler67.txt','rU')
g = copy.copy(f.readlines())
f.close()
h = []
triangle = []

for i in g:
	i = i.strip('\n')
	h.append(i)

for i in h:
	i = i.split()
	triangle.append(i)

for y in range(len(triangle)):
	for x in range(len(triangle[y])):
		triangle[y][x] = int(triangle[y][x])

# Returns last row number of any array.
triangleLength = len(triangle[-1]) - 1

# Sets the initial condition for the dictionary.
dict = { (0,0) : triangle[0][0] }

# Placeholders for the max value, and its location.
maxInLastRow = 0
max_Y = 0
max_X = 0

# The function doing the heavy lifting.
def getAnswer(y, x):
	global dict
	if dict.has_key((y,x)) == True:
		return dict[(y,x)]
	else: 
		if x == 0:		# First element of each row(y).
			dict[(y,x)] = triangle[y][x] + getAnswer(y-1, x)
		elif x == y:	# Last element of each row(y).
			dict[(y,x)] = triangle[y][x] + getAnswer(y-1, x-1)
		else:			# Remaining non-outer edge cases
			dict[(y,x)] = triangle[y][x] + max(getAnswer(y-1, x-1), getAnswer(y-1, x))
	return dict[(y,x)]

# This loop sets the range to iterate over all elements in the last row.
for i in range(len(triangle[-1])):
	getAnswer(triangleLength, i)

# Iterates through the last row to find the max, and its location.
for i in range(len(triangle[-1])-1):
	if dict[(triangleLength,i)] > maxInLastRow:
		maxInLastRow = dict[(triangleLength,i)]
		max_Y = triangleLength
		max_X = i

print "The maximum in the last row is %(maxInLastRow)i \
at location (%(max_Y)i,%(max_X)i)." % \
	{"maxInLastRow": maxInLastRow, "max_Y": max_Y, "max_X": max_X}

# ans: 7273

#notes: Used same method from #18.