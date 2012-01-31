#!/usr/bin/env python

# EULER 19
# 
# PROBLEM:
# 
# You are given the following information, but you may prefer to do
# some research for yourself.

"""
1 Jan 1900 was a Monday.

Thirty days has September,

April, June and November.

All the rest have thirty-one,

Saving February alone,

Which has twenty-eight, rain or shine.

And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a
century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

# AUTHOR: jo
# DATE:   31-JAN-2012

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

print numberOfFirsts - numberOfFirstsInNineteenHundred(1900)

#ans. 171