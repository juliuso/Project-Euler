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
# https://projecteuler.net/problem=17
# AUTHOR: jo
# DATE:   20-SEP-2011

if __name__ == '__main__':

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
        print(i)
        letterCount += len(i)
        print(letterCount)

    # teens (e.g. 10, 11, 12 ... 19)
    for i in b:
        print(i)
        letterCount += len(i)
        print(letterCount)

    # 10 interval only (e.g. 10, 20, 30 ... 90)
    for i in c:
        print(i)
        letterCount += len(i)
        print(letterCount)
    
    # c + a (21, 22, 23 ... 99)
    for i in range(len(c)):
        for j in range(len(a)):
            print(c[i] + a[j])
            letterCount += len(c[i] + a[j])
            print(letterCount)

    # 100 interval only (e.g. 100, 200, 300 ... 900)
    for i in a:
        print(i + d[0])
        letterCount += len(i + d[0])
        print(letterCount)

    # calculate the end range, 1000 (e.g. OneThousand)
    for i in e:
        print(a[0] + e[0])
        letterCount += len(a[0] + e[0])
        print(letterCount)

    # a + d + f + a (e.g. x01, x02, x03, x04 ... x09)
    for i in range(len(a)):
        for j in range(len(d)):
                for k in range(len(a)):
                    print(a[i] + d[j] + f[0] + a[k])
                    letterCount += len(a[i] + d[j] + f[0] + a[k])
                    print(letterCount)

    # a + d + f + b (e.g. x10, x11, x12 ... x19)
    for i in range(len(a)):
        for j in range(len(d)):
                for k in range(len(b)):
                    print(a[i] + d[j] + f[0] + b[k])
                    letterCount += len(a[i] + d[j] + f[0] + b[k])
                    print(letterCount)

    # a + d + f + c (e.g. x20, x30, x40 ... x90)
    for i in range(len(a)):
        for j in range(len(d)):
                for k in range(len(c)):
                    print(a[i] + d[j] + f[0] + c[k])
                    letterCount += len(a[i] + d[j] + f[0] + c[k])
                    print(letterCount)

    # a + d + f + c + a (e.g. 121, 122, 123 ... 999)
    for i in range(len(a)):
        for j in range(len(d)):
            for k in range(len(c)):
                for l in range(len(a)):
                    print(a[i] + d[j] + f[0] + c[k] + a[l])
                    letterCount += len(a[i] + d[j] + f[0] + c[k] + a[l])
                    print(letterCount)

    print("The answer is: %i" % letterCount)
