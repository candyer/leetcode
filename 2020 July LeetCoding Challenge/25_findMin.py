# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3401/

# Find Minimum in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# The array may contain duplicates.

# Example 1:
# Input: [1,3,5]
# Output: 1

# Example 2:
# Input: [2,2,2,0,1]
# Output: 0

# Note:
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?

from typing import List
def findMin(nums: List[int]) -> int:
	left = 0
	right = len(nums)-1
	while left < right:
		mid = (left + right) // 2
		if nums[mid] > nums[right]:
			left = mid + 1
		elif nums[mid] < nums[right]:
			right = mid
		else:
			right -= 1
	return nums[right]


assert(findMin([4,5,6,7,8,1,2]) == 1)
assert(findMin([2,2,2,0,1,1]) == 0)
assert(findMin([1,3,5]) == 1)



