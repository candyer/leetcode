
# https://leetcode.com/problems/intersection-of-two-arrays/description/
# Leetcode 349 -- Intersection of Two Arrays

# Given two arrays, write a function to compute their intersection.
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

# Note:
# Each element in the result must be unique.
# The result can be in any order.

def intersection(nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""
	res = []
	for num in nums1:
		if num in nums2 and num not in res:
			res.append(num)
	return res



# print intersection([], [1]) #[]
print intersection([1,2,1,2,3,3,3], [1,2,3,3,3]) #[1,2]
