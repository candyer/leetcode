# https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3446/

# Contains Duplicate III

# Given an array of integers, find out whether there are two distinct indices i and j in the array such that 
# the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.


# Example 1:
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true

# Example 3:
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false

#########################################################################
# Time complexity: O(nk)
# Space complexity: O(1)
from typing import List
def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
	n = len(nums)
	if t == 0 and len(set(nums)) == n:
		return False
	for i in range(n):
		for j in range(i + 1, min(i + k + 1, n)):
			if abs(nums[i] - nums[j]) <= t:
				return True
	return False	



#########################################################################
# Time complexity: O(n)
# Space complexity: O(bucket size)
from typing import List
def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
	'''
	i <= k <= j
	nums[i] <= t <= nums[j]
	'''
	if t < 0 or not nums or k <= 0:
		return False
	buckets = {}
	width = t + 1 # aviod 'ZeroDivisionError'

	for i, num in enumerate(nums):
		idx = num // width
		if idx in buckets:
			return True
		else:
			# check the left bucket
			if idx - 1 in buckets and num - buckets[idx - 1] <= t:
				return True
			# check the right bucket
			if idx + 1 in buckets and buckets[idx + 1] - num <= t:
				return True
			buckets[idx] = num
			if i >= k:
				buckets.pop(nums[i - k] // width)
	return False


assert(containsNearbyAlmostDuplicate([38, 28, 21, 15, 10, 6, 3, 1], 4, 2) == True)
assert(containsNearbyAlmostDuplicate([11, 20, 5, 30, 8], 3, 5))
assert(containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) == True)
assert(containsNearbyAlmostDuplicate([1,0,1,1], 1, 2) == True)
assert(containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) == False)
assert(containsNearbyAlmostDuplicate([2, 2], 3, 0) == True)
assert(containsNearbyAlmostDuplicate([0, 0], 0, 0) == False)





