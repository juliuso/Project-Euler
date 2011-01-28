#!/usr/bin/python

# set variable to store cumulative sum of even value modulus test.
total = 0

# create empty list that will store fibonacci numbers to upper bound. 
f=[]

# define variables a & b with initial condition for fibonacci sequence 0 and 1.
a, b = 0, 1

# while loop generates fibonacci sequence to upper bound 4,000,000.
while b<4000000:
	# each value including initial conditions added to the list.
    f.append(b)
    # continues looping by adding the previous two numbers to generate the next value.
    a, b = b, a+b  

# prints the list.
print f

# performs the mod2 test, if the remainder after division is zero, than it's even.
for i in f:
    if(i%2==0):
    	# if it's even, cumulatively add that value to var total.
		total += i

# print the result.
print "The Total is: %r" % total