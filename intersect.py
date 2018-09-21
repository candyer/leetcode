# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

# 350. Intersection of Two Arrays II

# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


from collections import Counter as c
def intersect(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""
	d1, d2 = c(nums1), c(nums2)
	res = []
	for k, v in d1.items():
		if k in d2:
			res.extend([k] * min(v, d2[k]))
	return res


assert intersect([1,2,2,1], [2,2]) == [2, 2]
assert intersect([4,9,5], [9,4,9,8,4]) == [9, 4]
assert intersect([2,1,2,2,1], [2,2,3,2,1]) == [1, 2, 2, 2]
assert intersect([], [1,1,1]) == []






