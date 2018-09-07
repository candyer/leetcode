# https://leetcode.com/problems/product-of-array-except-self/description/

# 238. Product of Array Except Self


# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)




def productExceptSelf(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	n = len(nums)
	res = []
	tmp = 1
	for i in range(n):
		res.append(tmp)
		tmp *= nums[i]
	tmp = 1
	for i in range(n - 1, -1, -1):
		res[i] *= tmp
		tmp *= nums[i]
	return res

assert productExceptSelf([1,2,3,4]) == [24, 12, 8, 6]
