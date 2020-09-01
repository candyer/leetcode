# https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3445/

# Largest Time for Given Digits

# Given an array of 4 digits, return the largest 24 hour time that can be made.

# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, 
# a time is larger if more time has elapsed since midnight.

# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.


# Example 1:
# Input: [1,2,3,4]
# Output: "23:41"

# Example 2:
# Input: [5,5,5,5]
# Output: ""
 
# Note:
# A.length == 4
# 0 <= A[i] <= 9



from typing import List
from itertools import permutations

def largestTimeFromDigits(A: List[int]) -> str:
	max_time = -1
	for h, i, j, k in set(permutations(A, 4)):
		hour = h * 10 + i
		minute = j * 10 + k
		if hour < 24 and minute < 60:
			max_time = max(max_time, hour * 60 + minute)
	if max_time == -1:
		return ""
	else:
		return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)

assert(largestTimeFromDigits([1,2,3,4]) == "23:41")
assert(largestTimeFromDigits([2,5,5,5]) == "")
assert(largestTimeFromDigits([2,1,5,5]) == "21:55")
assert(largestTimeFromDigits([0,0,8,0]) == "08:00")
assert(largestTimeFromDigits([5,5,5,5]) == "")
assert(largestTimeFromDigits([2,3,9,9]) == "")
assert(largestTimeFromDigits([0,0,0,0]) == "00:00")
assert(largestTimeFromDigits([2,0,7,6]) == '07:26')




