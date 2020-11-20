# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3537/

# Search in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

# Follow up:
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?


from typing import List
def search(nums: List[int], target: int) -> bool:
	n = len(nums)
	left, right = 0, n - 1
	while left <= right:
		mid = (left + right) // 2

		if target == nums[mid]:
			return True

		while nums[left] == nums[mid] and left < mid:
			left += 1

		if nums[left] <= nums[mid]:  #nums[left:mid] is ordered
			if nums[left] <= target < nums[mid]: #target in nums[left:mid]
				right = mid - 1
			else: #target in nums[mid:right]
				left = mid + 1

		else: #nums[mid:] is ordered
			if nums[mid] < target <= nums[right]: #target in nums[mid:right]
				left = mid + 1
			else: #target in nums[left:mid]
				right = mid - 1

	return False

assert(search([1, 3, 1, 1, 1], 3) == True)
assert(search([2,5,6,0,0,1,2], 0) == True)
assert(search([2,5,6,0,0,1,2], 3) == False)
assert(search([2,5,6,0,0,1,2], 5) == True)






