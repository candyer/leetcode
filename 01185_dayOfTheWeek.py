# https://leetcode.com/problems/day-of-the-week/description/

# 1185. Day of the Week

# Given a date, return the corresponding day of the week for that date.
# The input is given as three integers representing the day, month and year respectively.
# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 
# Example 1:
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"

# Example 2:
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"

# Example 3:
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
 
# Constraints:
# The given dates are valid dates between the years 1971 and 2100.


# solution 1
############################################################
def is_leap(year):
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		return True
	return False

def dayOfTheWeek(day, month, year):
	"""
	:type day: int
	:type month: int
	:type year: int
	:rtype: str
	"""
	weekdays = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
	days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	leap_year_count = sum([is_leap(y) for y in range(1971, year)])

	total = (year - 1971) * 365 + leap_year_count
	total += sum(days_in_months[:month - 1])
	total += day

	if is_leap(year) and month > 2:
		total += 1
	
	return weekdays[total % 7]




# solution 2
############################################################
from calendar import isleap
def dayOfTheWeek(day, month, year):
	"""
	:type day: int
	:type month: int
	:type year: int
	:rtype: str
	"""
	weekdays = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
	days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	leap_year_count = sum([isleap(y) for y in range(1971, year)])

	total = (year - 1971) * 365 + leap_year_count
	total += sum(days_in_months[:month - 1])
	total += day

	if isleap(year) and month > 2:
		total += 1
	
	return weekdays[total % 7]



# solution 3
############################################################
from datetime import date
def dayOfTheWeek(day, month, year):
	"""
	:type day: int
	:type month: int
	:type year: int
	:rtype: str
	"""
	return date(year, month, day).strftime('%A')



# solution 4
############################################################
from datetime import date
from calendar import day_name
def dayOfTheWeek(day, month, year):
	"""
	:type day: int
	:type month: int
	:type year: int
	:rtype: str
	"""
	return day_name[date(year, month, day).weekday()]


assert dayOfTheWeek(31, 8, 2019) == 'Saturday'
assert dayOfTheWeek(18, 7, 1999) == 'Sunday'
assert dayOfTheWeek(15, 8, 1993) == 'Sunday'
assert dayOfTheWeek(29, 2, 2016) == 'Monday'
