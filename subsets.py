# https://leetcode.com/problems/subsets/description/


# 78. Subsets

# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

def subsets(nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	res = [[]]
	def rec(nums, tmp):
		for i, num in enumerate(nums):
			res.append(tmp + [num])
			rec(nums[i + 1:], tmp + [num])
	rec(nums, [])
	return res


assert subsets([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
assert subsets([]) == [[]]



