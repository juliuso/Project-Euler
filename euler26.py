#!/usr/bin/env python
#NOT WORKING
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
# https://projecteuler.net/problem=26
# AUTHOR: jo
# DATE:   10-JUN-2012

if __name__ == '__main__':

    num = 1
    denom = 6
    number  = []

    # number.append(0)

    def fracLength(num, denom):
        #print num, d  # Verifying num and denom are passed in.
        count = 1
        
        initial_num = 10
        new_num = initial_num % denom * 10
        remainder = initial_num % denom
        
        #count += 1
        
        while (initial_num != new_num):
            
            if (remainder == 0):
                #count += 1
                new_num = initial_num
            
            else:
                new_num  = new_num % denom * 10
                remainder = new_num % denom
                count+=1
                
        number.append(count)
        print(number)

    fracLength(num, denom)
        
