# https://leetcode.com/problems/maximum-width-ramp/description/


# 962. Maximum Width Ramp
# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

# Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

# Example 1:
# Input: [6,0,8,2,1,5]
# Output: 4
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.

# Example 2:
# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
 
# Note:
# 2 <= A.length <= 50000
# 0 <= A[i] <= 50000


def maxWidthRamp(A):
	"""
	:type A: List[int]
	:rtype: int
	"""
	res = 0
	tmp = float('inf')
	for i in sorted(range(len(A)), key=A.__getitem__):
		res = max(res, i - tmp)
		tmp = min(tmp, i)
	return res

assert maxWidthRamp([9, 8, 7, 6, 5]) == 0
assert maxWidthRamp([1, 2, 3, 4, 5]) == 4
assert maxWidthRamp([6,0,8,2,1,5]) == 4
assert maxWidthRamp([9,8,1,0,1,9,4,0,4,1]) == 7



