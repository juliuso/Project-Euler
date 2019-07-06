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
# https://projecteuler.net/problem=14
# AUTHOR: jo
# DATE:   25-JUL-2011

if __name__ == '__main__':

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

    for i in range(1,1000000):
        if len(chainer(i)) > chainLength:
            canChain = chainer(i)
            chainLength = len(chainer(i))

    print("The highest starting number is: %i" % canChain[0])
    print("The chain is: %s" % canChain)
    print("The chain is %i digits long." % chainLength)