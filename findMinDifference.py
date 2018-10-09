# https://leetcode.com/problems/minimum-time-difference/description/

# 539. Minimum Time Difference


# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.



def findMinDifference(timePoints):
	"""
	:type timePoints: List[str]
	:rtype: int
	"""
	minutes = []
	for time in timePoints:
		hour, minute = map(int, time.split(':'))
		minutes.append(hour * 60 + minute)
	minutes.sort()
	mini = 1440
	for i in range(1, len(minutes)):
		mini = min(minutes[i] - minutes[i - 1], mini)
	return min(mini, 1440 +minutes[0] - minutes[-1])

assert findMinDifference(["23:59", "00:00", "17:42", "07:56"]) == 1
assert findMinDifference(["03:39", "17:42", "07:56"]) == 257
assert findMinDifference(["03:39", "17:42", "12:56"]) == 286
assert findMinDifference(["00:50", "23:00"]) == 110
assert findMinDifference(["00:20", "23:00"]) == 80



