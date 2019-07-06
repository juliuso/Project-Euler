#!/usr/bin/env python
'''
MIT License

Copyright (c) 2012 Julius O

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
# https://projecteuler.net/problem=67
# AUTHOR: jo
# DATE:   20-OCT-2011

import copy

if __name__ == '__main__':

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
		if (y,x) in dict:
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

	print("The maximum in the last row is %(maxInLastRow)i \
			at location (%(max_Y)i,%(max_X)i)." % \
			{"maxInLastRow": maxInLastRow, "max_Y": max_Y, "max_X": max_X})


#notes: Used same method from #18.