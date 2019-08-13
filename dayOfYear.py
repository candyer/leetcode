# https://leetcode.com/problems/day-of-the-year/description/

# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, 
# return the day number of the year.


# Example 1:
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.

# Example 2:
# Input: date = "2019-02-10"
# Output: 41

# Example 3:
# Input: date = "2003-03-01"
# Output: 60

# Example 4:
# Input: date = "2004-03-01"
# Output: 61
 

# Constraints:

# date.length == 10
# date[4] == date[7] == '-', and all other date[i]'s are digits
# date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.


# def dayOfYear(date):
# 	"""
# 	:type date: str
# 	:rtype: int
# 	"""
# 	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 	running_days = [31]
# 	for d in days[1:]:
# 		running_days.append(running_days[-1] + d)
# 	print running_days
# 	year, month, day = map(int, date.split('-'))
# 	res = 0
# 	if month > 1:
# 		res += running_days[month - 2]
# 	if month > 2 and year % 4 == 0:
# 		res += 1
# 	res += day
# 	return res


def is_leap_year(year):
	return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def dayOfYear(date):
	"""
	:type date: str
	:rtype: int
	"""
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	year, month, day = map(int, date.split('-'))
	res = 0
	for m in range(month - 1):
		res += days[m]
	res += day
	if is_leap_year(year) and month > 2:
		res += 1
	return res

assert dayOfYear("1900-03-25") == 84
assert dayOfYear("2016-02-29") == 60
assert dayOfYear("2018-03-01") == 60
assert dayOfYear("2019-01-09") == 9
assert dayOfYear("2019-02-10") == 41
assert dayOfYear("2003-03-01") == 60
assert dayOfYear("2004-03-01") == 61
assert dayOfYear("2019-08-11") == 223






