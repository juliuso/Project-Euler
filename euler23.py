#!/usr/bin/env python

# EULER 23
# 
# PROBLEM: 
"""
A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number. For example, the sum
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper
divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be
shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the
sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be
written as the sum of two abundant numbers.

http://projecteuler.net/problem=23
"""

# AUTHOR: jo
# DATE:   03-MAR-2012

start       = 1
end         = 28123
abundant    = []
number_line = range(start, end + 1)

def findDivisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def intAndSum(n):
    divisors = findDivisors(n)
    if sum(divisors) > n:
        abundant.append(n)

def main(argv=None):
    for i in range(start, end + 1):
        intAndSum(i)
    
    for i in abundant:
        try:
            number_line.pop(i)
            number_line.pop(i+i)
        except IndexError:
            continue
    
    for number in range(0, len(abundant)):
        try:
            for base in range(0, len(abundant)):
                number_line.pop(abundant[number] + abundant[base])
        except IndexError:
            continue
    
    print sum(number_line)

main()

#ans. 
