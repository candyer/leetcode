# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3387/
# https://potatomatooo.blogspot.com/2020/07/leetcode-78-subsets-python.html

# Subsets

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



# Time complexity: O(n * pow(2, n))
# Space complexity: O(n * pow(2, n))

from typing import List
def subsets(nums: List[int]) -> List[List[int]]:
	n = len(nums)
	res = []
	for i in range(pow(2, n), pow(2, n + 1)):
		b = bin(i)[3:]
		tmp = []
		for j in range(n):
			if b[j] == '1':
				tmp.append(nums[j])
		res.append(tmp)
	return res

assert(subsets([1, 2, 3]) == [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]])

