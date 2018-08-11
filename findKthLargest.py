# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# 215. Kth Largest Element in an Array

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.


# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4

# Note: 
# You may assume k is always valid, 1 <= k <= array's length.


def findKthLargest(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	return sorted(nums, reverse=True)[k - 1]

assert findKthLargest([3,2,1,5,6,4], 2) == 5
assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4