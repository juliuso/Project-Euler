#!/usr/bin/env python
'''
MIT License

Copyright (c) 2019 Julius O

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
# https://projecteuler.net/problem=28
# AUTHOR: jo
# DATE:   06-JUL-2019

import os

#Formula: (i**2) + ((i**2)-(i-1)) + ((i**2)-2*(i-1)) + ((i**2)-3*(i-1))
#Simplified: 4*(i**2) - (6*i) + 6
def spiralNumbers(n):
    answer = 0
    for i in range(1,n):
        if i == 1:
            answer += i
        elif i%2 != 0:
            sumOfCorners = 4*i**2 - 6*i + 6
            answer += sumOfCorners
    return answer

if __name__ == '__main__':
    os.system('clear')
    print(spiralNumbers(1002))
