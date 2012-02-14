#!/usr/bin/env python

# EULER 22
# 
# PROBLEM: 
"""
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working 
out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

# AUTHOR: jo
# DATE:   14-FEB-2012

import csv

f = open('euler22.txt', 'rb')
reader = csv.reader(f)
names = []
alphabet = []
total_sum = []

for name in reader:
    names.extend(name)

f.close()

# Using Python's built-in sort function to do the job.
names = sorted(names)

# Processes each name in the names list.
# Records index position and all calculations.
def nameToNum(name):
    name_row = names.index(name)
    name_total = []
    for letter in name:
        name_total.append(alphabet.index(letter))
    total_sum.append(sum(name_total)*(name_row + 1))

# Creates the array that maps letters to integer values.
for i in range(65, 90 + 1):
    alphabet.extend(chr(i))
alphabet.insert(0, '*')

for name in names:
    nameToNum(name)

print total_sum
print sum(total_sum)

#ans. 871198282