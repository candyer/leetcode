# https://leetcode.com/problems/maximum-product-of-three-numbers/#/description

# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:  Input: [1,2,3]     Output: 6
# Example 2:  Input: [1,2,3,4]   Output: 24
# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


def maximumProduct(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	nums.sort()
	return max(nums[-1] * nums[0] * nums[1], nums[-1] * nums[-2] * nums[-3])


print maximumProduct([-7, -6, -4, 9, 10]) #420
print maximumProduct([-7, -6, -4, 9]) #378
print maximumProduct([-7, -2, 6, 9]) #126
print maximumProduct([-1, 2, 3, 9]) #54
print maximumProduct([-1, 2, 3, 9, 12]) #324
