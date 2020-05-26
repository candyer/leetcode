# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3341/

# Contiguous Array

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

from typing import List
def findMaxLength(nums: List[int]) -> int:
	res = 0
	tmp = 0
	d = {0:-1}
	for i in range(len(nums)):
		if nums[i] == 1:
			tmp += 1
		else:
			tmp -= 1
		if tmp in d:
			res = max(res, i - d[tmp])
		else:
			d[tmp] = i
	return res


assert(findMaxLength([0,1]) == 2)
assert(findMaxLength([0,1,0]) == 2)
assert(findMaxLength([0, 0]) == 0)
assert(findMaxLength([0, 0, 0, 0, 1]) == 2)
assert(findMaxLength([1, 1, 0, 1, 0, 0, 1, 1, 1]) == 6)




