# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356/


# Search Insert Position

# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.


# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

######################################################
from typing import List
def searchInsert(nums: List[int], target: int) -> int:
	left, right = 0, len(nums) - 1
	while left <= right:
		mid = (left + right) // 2
		if target == nums[mid]:
			return mid
		elif target < nums[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return left


######################################################
from typing import List
from bisect import bisect_left
def searchInsert(nums: List[int], target: int) -> int:
	return bisect_left(nums, target)

	

assert(searchInsert([1,3,5,6], 5) == 2)
assert(searchInsert([1,3,5,6], 2) == 1)
assert(searchInsert([1,3,5,6], 7) == 4)
assert(searchInsert([1,3,5,6], 0) == 0)
assert(searchInsert([1,3,5,6], 1) == 0)
assert(searchInsert([1,3], 2) == 1)


