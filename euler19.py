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
# https://projecteuler.net/problem=19
# AUTHOR: jo
# DATE:   31-JAN-2012

if __name__ == '__main__':

    jan = 31
    feb = 28
    feb_leap = 29
    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    sep = 30
    oct = 31
    nov = 30
    dec = 31


    standard_year_months = [jan, feb, mar, apr, may, jun, jul, aug, sep,\
                            oct, nov, dec]

    standard_year_days = []

    leap_year_months = [jan, feb_leap, mar, apr, may, jun, jul, aug, sep,\
                            oct, nov, dec]

    leap_year_days = []

    calendar = {}
    calendar_days = []
    calendar_days_in_weeks = []
    numberOfFirsts = 0

    def isLeapYear(year):
        if year%100 == 0 and year%400 == 0:
            return True
        elif year%4 == 0:
            return True
        else:
            return False

    def numberOfFirstsInNineteenHundred(n):
        # calculate number of firsts on sunday in 1900.
        nineteen_hundred = calendar[1900]
        nineteen_hundred_week = nineteen_hundred[6::7]

        first_on_sunday_in_nineteen_hundred = 0
        for week in nineteen_hundred_week:
            if week == 1:
                first_on_sunday_in_nineteen_hundred += 1
        return first_on_sunday_in_nineteen_hundred
            
    for year in range(1900, 2000 + 1):
        if isLeapYear(year) is True:
            calendar[year] = leap_year_days
        else:
            calendar[year] = standard_year_days

    for month in standard_year_months:
        standard_year_days.extend(range(1, month + 1))

    for month in leap_year_months:
        leap_year_days.extend(range(1, month + 1))

    for year in calendar:
        calendar_days.extend(calendar[year])

    calendar_days_in_weeks.extend(calendar_days[6::7])

    for i in calendar_days_in_weeks:
        if i == 1:
            numberOfFirsts += 1

    print(numberOfFirsts - numberOfFirstsInNineteenHundred(1900))
