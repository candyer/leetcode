# https://leetcode.com/problems/largest-time-for-given-digits/description/


# 949. Largest Time for Given Digits


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



from itertools import permutations as p
def largestTimeFromDigits(A):
	"""
	:type A: List[int]
	:rtype: str
	"""
	time = (0, 0)
	flag = False
	for a, b, c, d in list(p(A)):
		hour = a * 10 + b
		minute = c * 10 + d
		if hour < 24 and minute < 60:
			time = max(time, (hour, minute))
			flag = True
	if flag:
		h, m = time
		res = []
		if h < 10:
			res.append('0')
		res.append(str(h))
		res.append(':')
		if m < 10:
			res.append('0')
		res.append(str(m))
		return ''.join(map(str, res))
	else:
		return ''
	

assert largestTimeFromDigits([0,6,6,6]) == ''
assert largestTimeFromDigits([0,5,6,6]) == '06:56'
assert largestTimeFromDigits([2,3,4,5]) == '23:54'
assert largestTimeFromDigits([0,5,5,9]) == '09:55'
assert largestTimeFromDigits([0,1,3,9]) == '19:30'
assert largestTimeFromDigits([1,1,3,4]) == '14:31'
assert largestTimeFromDigits([1,2,3,4]) == '23:41'
assert largestTimeFromDigits([2,2,3,3]) == '23:32'
assert largestTimeFromDigits([1,2,2,9]) == '22:19'
assert largestTimeFromDigits([1,2,2,2]) == '22:21'
assert largestTimeFromDigits([0,1,2,2]) == '22:10'
assert largestTimeFromDigits([0,0,0,0]) == '00:00'
assert largestTimeFromDigits([2,3,9,5]) == '23:59'
assert largestTimeFromDigits([1,2,3,4]) == '23:41'
assert largestTimeFromDigits([2,2,3,5]) == '23:52'
assert largestTimeFromDigits([0,9,9,9]) == ''
assert largestTimeFromDigits([5,5,5,5]) == ''
assert largestTimeFromDigits([2,4,4,5]) == ''







