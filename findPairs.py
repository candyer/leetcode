# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

# 532. K-diff Pairs in an Array

# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
# Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their 
# absolute difference is k.


# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

# Note:
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].

from collections import Counter as c
def findPairs(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	if k < 0: return 0
	d = c(nums)
	keys = sorted(d.keys())
	count = 0
	if k == 0:
		for k, v in d.items():
			if v > 1:
				count += 1
		return count

	i, j, n = 0, 1, len(keys)
	while i < n and j < n:
		tmp = keys[j] - keys[i]
		if tmp == k:
			count += 1
			i += 1
			j += 1
		elif tmp < k:
			j += 1
		else:
			i += 1
	return count



from collections import Counter as c
def findPairs(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	if k < 0: return 0
	d = c(nums)
	count = 0
	for key, val in d.items():
		if k == 0:
			if val > 1:
				count += 1
		else:
			if key + k in d:
				count += 1
	return count



assert findPairs([1, 1, 1, 1, 1 ], 0) == 1
assert findPairs([1, 1, 1, 1, 1, 3, 3, -2, -2], 0) == 3
assert findPairs([3, 1, 4, 1, 5, 3], 2) == 2
assert findPairs([3, 1, 4, 1, 5], 2) == 2
assert findPairs([1, 2, 3, 4, 5], 1) == 4
assert findPairs([1, 3, 1, 5, 4], 0) == 1
assert findPairs([-8, -5, 3, 6, 9], 3) == 3
assert findPairs([1, 2, 3, 4, 5], -1) == 0








