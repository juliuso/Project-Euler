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
# https://projecteuler.net/problem=22
# AUTHOR: jo
# DATE:   14-FEB-2012

import csv

if __name__ == '__main__':

    f = open('euler22.txt', 'r')
    reader = csv.reader(f, delimiter=',')
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

    #print(total_sum)
    print(sum(total_sum))

