#!/usr/bin/python

numbers = []
palindromeTxt = []
palindromeInt = []

x = 0

for n1 in xrange(1000,1,-1):
	for n2 in xrange(n1,100,-1):
		x = n1 * n2
		numbers.append(x)

for i in numbers:
	palindromeTxt.append(str(i))

for i in palindromeTxt:
	if i == i[::-1]:
		palindromeInt.append(int(i))
	
print "The maximum 3-digit palindrome is %i" % max(palindromeInt) 
