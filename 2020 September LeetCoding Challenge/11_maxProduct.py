# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3456/

# Maximum Product Subarray

# Given an integer array nums, find the contiguous subarray within an array 
# (containing at least one number) which has the largest product.

# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


from typing import List
def maxProduct(nums: List[int]) -> int:
	'''
	max product:
	- previous maxi * curr
	- previous mini * curr
	- curr (> previous res)
	'''
	maxi = mini = res = nums[0]
	for num in nums[1:]:
		candidates = [maxi * num, mini * num, num]
		maxi, mini = max(candidates), min(candidates)
		res = max(res, maxi)
	return res

assert(maxProduct([2,3,-2,4]) == 6)
assert(maxProduct([-2,0,-1]) == 0)
assert(maxProduct([0, 0, 2, 3, -1, 2, 0, 5, 0]) == 6)






