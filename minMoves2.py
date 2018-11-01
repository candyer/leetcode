# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/


# 462. Minimum Moves to Equal Array Elements II

# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, 
# where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

# You may assume the array's length is at most 10,000.

# Example:

# Input:
# [1,2,3]

# Output:
# 2

# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):

# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]



def minMoves2(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	n = len(nums)
	nums.sort()
	median = nums[n / 2]
	res = 0
	for num in nums:
		res += abs(num - median)
	return res

assert minMoves2([1,2,3]) == 2
assert minMoves2([2,4,7]) == 5
assert minMoves2([2, 6, 9, 12]) == 13
assert minMoves2([5, 5, 5, 5, 10]) == 5