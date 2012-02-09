#!/usr/bin/python

# EULER 4
# 
# PROBLEM:
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91  99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# AUTHOR: jo
# DATE:   10-MAY-2011

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
    
print "The maximum palindrome from 3-digit products is:  %i" % max(palindromeInt)
