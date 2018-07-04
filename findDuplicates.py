# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

# 442. Find All Duplicates in an Array

# Given an array of integers, 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]


#####################
### solution one ####
#####################

from collections import Counter as c
def findDuplicates(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	d = c(nums)
	res = []
	for key, val in d.items():
		if val == 2:
			res.append(key)
	return res


#####################
### solution two ####
#####################

from collections import Counter as c
def findDuplicates(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	res = []
	for n in nums:
		pos = abs(n) - 1
		if nums[pos] < 0:
			res.append(pos + 1)
		nums[pos] *= -1
	return res


assert findDuplicates([4,3,2,7,8,2,3,1]) == [2, 3]
assert findDuplicates([7, 1, 2, 4, 5, 5, 7, 2]) == [5, 7, 2]









