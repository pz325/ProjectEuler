'''
Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


171
'''

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    is_leap = (0 == year%100 and 0 == year%400) or (not 0 == year%100 and 0 == year%4)
    return is_leap

def solution():
    '''
    problem solution
    '''
    year = 1900
    date_on_month_begin = 1
    count = 0
    while year < 2001:
        for month in xrange(1, 13):
            day_to_add = DAYS_IN_MONTH[month-1]
            if is_leap(year) and month == 2:
                day_to_add += 1
            date_on_month_begin += day_to_add % 7
            date_on_month_begin = date_on_month_begin % 7
            if year > 1900 and date_on_month_begin == 0:
                count += 1
        year += 1

    return count


if __name__ == '__main__':
    result = solution()
    print('Result: ', result)
