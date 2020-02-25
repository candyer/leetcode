# https://leetcode.com/problems/number-of-days-between-two-dates/description/


# 1360. Number of Days Between Two Dates

# Write a program to count the number of days between two dates.
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

# Example 1:
# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1

# Example 2:
# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15

# Constraints:
# The given dates are valid dates between the years 1971 and 2100.


###############################
######## solution 1 ###########
###############################
def isLeap(year: int) -> bool:
	return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

def days_from_1971(date: str) -> int:
	year, month, day = map(int, date.split('-'))
	days = 0
	for y in range(1971, year):
		if isLeap(y):
			days += 366
		else:
			days += 365
		
	days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	for m in range(month - 1):
		days += days_of_month[m]
	if month > 2 and isLeap(year):
		days += 1
	return days + day

def daysBetweenDates(date1: str, date2: str) -> int:
	return abs(days_from_1971(date1) - days_from_1971(date2))


###############################
######## solution 2 ###########
###############################
from datetime import datetime
def daysBetweenDates(date1, date2):
	date_format = "%Y-%m-%d"
	first = datetime.strptime(date1, date_format)
	second = datetime.strptime(date2, date_format)
	return abs((second - first).days)
	

assert(daysBetweenDates("2019-06-29", "2019-06-30") == 1)
assert(daysBetweenDates("2020-01-15", "2019-12-31") == 15)
assert(daysBetweenDates("2099-06-30", "1971-01-29") == 46904)
assert(daysBetweenDates("2017-01-29", "2020-06-30") == 1248)


