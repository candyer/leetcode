# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3748/

# Minimum Moves to Equal Array Elements II


# Given an integer array nums of size n, 
# return the minimum number of moves required to make all array elements equal.
# In one move, you can increment or decrement an element of the array by 1.


# Example 1:
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

# Example 2:
# Input: nums = [1,10,2,9]
# Output: 16


# Constraints:
# n == nums.length
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9


from typing import List
def minMoves2(nums: List[int]) -> int:
	res = 0
	median = nums[len(nums) // 2]
	for num in nums:
		res += abs(median - num)
	return res

assert(minMoves2([1,2,3]) == 2)
assert(minMoves2([1,10,2,9]) == 16)
