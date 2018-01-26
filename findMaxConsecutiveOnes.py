# https://leetcode.com/problems/max-consecutive-ones/description/
# 485. Max Consecutive Ones

# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:   Input: [1,1,0,1,1,1]   Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.

# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000


def findMaxConsecutiveOnes(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	
	n = len(nums)
	if not 0 in nums:
		return n
	res = count = 0
	index_0 = nums.index(0)

	for i in range(index_0, n):
		if nums[i] == 0:
			count = i - index_0 - 1
			res = max(res, count)
			index_0 = i
	return max(res, nums.index(0), n - index_0 - 1)


def findMaxConsecutiveOnes(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	
	n = len(nums)
	index_0 = []
	for i in range(n):
		if nums[i] == 0:
			index_0.append(i)
	res = 0
	if len(index_0) == 0:
		return n
	res = index_0[0]
	for j in range(1, len(index_0)):
		res = max(res, index_0[j] - index_0[j - 1] - 1)
	return max(res, n - index_0[-1] - 1)


assert findMaxConsecutiveOnes([0,0,0,0,0,0]) == 0
assert findMaxConsecutiveOnes([1,1,1,1,1,1]) == 6
assert findMaxConsecutiveOnes([0,1,1,1,1,1]) == 5
assert findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
assert findMaxConsecutiveOnes([1,1,0,1,1,1,0]) == 3
assert findMaxConsecutiveOnes([1,1,0,1,1,0,1,1,0,1,1,1,1,0]) == 4

