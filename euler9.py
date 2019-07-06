#!/usr/bin/env python
'''
MIT License

Copyright (c) 2011 Julius O

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
# https://projecteuler.net/problem=9
# AUTHOR: jo
# DATE:   31-MAY-2011

def run():
    sum = 1000
    for a in range(sum):
        for b in range(sum):
            for c in range(sum):
                if (a**2) + (b**2) == (c**2):
                    if a > 0:
                        if b > 0:
                            if c > 0:
                                if a + b + c == 1000:
                                    print('The triangle sides are: {}, {}, {}'.format(a,b,c))
                                    print(a*b*c)
                                    return
    
if __name__ == '__main__':
    run()

# Additional conditions should be added to prevent returning
# identical solutions, but in a different order.
# (ex. a, b, c == c, b, a)
