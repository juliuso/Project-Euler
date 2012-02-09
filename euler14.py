#!/usr/bin/env python

# EULER 14
# 
# PROBLEM:
# 
# The following iterative sequence is defined for the set of positive
# integers:

# n ->  n/2 (n is even)
# n ->  3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following
# sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# http://projecteuler.net/index.php?section=problems&id=14

# AUTHOR: jo
# DATE:   25-JUL-2011


def chainer(n):
    chain = [n]
    while chain[-1] != 1:
        if chain[-1] == 1:
            break
        elif chain[-1] % 2 == 0:
            chain.append(chain[-1]/2)
        elif chain[-1] % 2 != 0:
            chain.append(chain[-1] * 3 + 1)
    return chain

canChain = []
chainLength = 0

for i in xrange(1,1000000):
    if len(chainer(i)) > chainLength:
        canChain = chainer(i)
        chainLength = len(chainer(i))

print "The highest starting number is: %i" % canChain[0]
print "The chain is: %s" % canChain
print "The chain is %i digits long." % chainLength

#ans: 837799