# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

# 448. Find All Numbers Disappeared in an Array

# Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear 
# twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned 
# list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


def findDisappearedNumbers(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	n = len(nums)
	i = 0
	while i < n:
		j = nums[i] - 1
		if nums[i] != nums[j]:
			nums[i], nums[j] = nums[j], nums[i]
		else:
			i += 1

	res = []
	for idx, num in enumerate(nums):
		if idx + 1 != num:
			res.append(idx + 1)
	return res



assert findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]
assert findDisappearedNumbers([5, 1, 4, 1, 5]) == [2, 3]



