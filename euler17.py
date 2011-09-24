#!/usr/bin/env python

# EULER 17
# 
# PROBLEM:
# 
# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
# and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in	
# compliance with British usage.
#
# http://projecteuler.net/index.php?section=problems&id=17

# AUTHOR: jo
# DATE:   20-SEP-2011

a = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

b = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',\
	'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

c = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',\
	'Eighty', 'Ninety']
	
d = ['Hundred']

e = ['Thousand']

f = ['and']

# this will hold the letter count as ranges are iterated and calculated.
letterCount = 0

# singles (e.g. 1, 2, 3 ... 9)
for i in a:
	print i
	letterCount += len(i)
	print letterCount

# teens (e.g. 10, 11, 12 ... 19)
for i in b:
	print i
	letterCount += len(i)
	print letterCount

# 10 interval only (e.g. 10, 20, 30 ... 90)
for i in c:
	print i
	letterCount += len(i)
	print letterCount
	
# c + a (21, 22, 23 ... 99)
for i in xrange(len(c)):
	for j in xrange(len(a)):
		print c[i] + a[j]
		letterCount += len(c[i] + a[j])
		print letterCount

# 100 interval only (e.g. 100, 200, 300 ... 900)
for i in a:
	print i + d[0]
	letterCount += len(i + d[0])
	print letterCount

# calculate the end range, 1000 (e.g. OneThousand)
for i in e:
	print a[0] + e[0]
	letterCount += len(a[0] + e[0])
	print letterCount

# a + d + f + a (e.g. x01, x02, x03, x04 ... x09)
for i in xrange(len(a)):
	for j in xrange(len(d)):
		for k in xrange(len(a)):
			print a[i] + d[j] + f[0] + a[k]
			letterCount += len(a[i] + d[j] + f[0] + a[k])
			print letterCount

# a + d + f + b (e.g. x10, x11, x12 ... x19)
for i in xrange(len(a)):
	for j in xrange(len(d)):
		for k in xrange(len(b)):
			print a[i] + d[j] + f[0] + b[k]
			letterCount += len(a[i] + d[j] + f[0] + b[k])
			print letterCount

# a + d + f + c (e.g. x20, x30, x40 ... x90)
for i in xrange(len(a)):
	for j in xrange(len(d)):
		for k in xrange(len(c)):
			print a[i] + d[j] + f[0] + c[k]
			letterCount += len(a[i] + d[j] + f[0] + c[k])
			print letterCount

# a + d + f + c + a (e.g. 121, 122, 123 ... 999)
for i in xrange(len(a)):
	for j in xrange(len(d)):
		for k in xrange(len(c)):
			for l in xrange(len(a)):
				print a[i] + d[j] + f[0] + c[k] + a[l]
				letterCount += len(a[i] + d[j] + f[0] + c[k] + a[l])
				print letterCount

print '\n'
print "The answer is: %i" % letterCount
# ans. 21124