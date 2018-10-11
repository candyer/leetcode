# https://leetcode.com/problems/binary-search/description/

# 704. Binary Search


# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
# If target exists, then return its index, otherwise return -1.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Note:
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].



###############
##solution 1###
###############
def search(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	res = -1
	for i, num in enumerate(nums):
		if target == num:
			res = i
			break
	return res

################
###solution 2###
################
def search(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	low, high = 0, len(nums) - 1
	while low <= high:
		mid = (low + high) / 2
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			high = mid - 1
		else:
			low = mid + 1
	return -1

assert search([-1,0,3,5,9,12], 9) == 4
assert search([-1,0,3,5,9,12], 12) == 5
assert search([-1,0,3,5,9,12], 2) == -1


