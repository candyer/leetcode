# https://leetcode.com/problems/longest-harmonious-subsequence/description/

# 594. Longest Harmonious Subsequence

# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.


from collections import Counter as c
def findLHS(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	d = c(nums)
	keys = sorted(d.keys())
	n = len(keys)
	if n <= 1:
		return 0
	res = 0
	for i in range(n - 1):
		if keys[i] + 1 ==  keys[i + 1]:
			res = max(res, d[keys[i]] + d[keys[i + 1]])
	return res




assert findLHS([1,3,2,2,5,2,3,7]) == 5
assert findLHS([]) == 0
assert findLHS([1]) == 0
assert findLHS([1, 1, 1, 1]) == 0
assert findLHS([1, 3]) == 0
assert findLHS([1, 2]) == 2



