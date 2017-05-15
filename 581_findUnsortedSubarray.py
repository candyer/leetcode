# https://leetcode.com/contest/leetcode-weekly-contest-32/problems/shortest-unsorted-continuous-subarray/

# Given an integer array, you need to find one continuous subarray that if you only sort this subarray 
# in ascending order, then the whole array will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

def findUnsortedSubarray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	sortedNums = sorted(nums)
	n = len(nums)
	for i in range(n):
		if nums[i] != sortedNums[i]:
			break
	if i == n - 1: 
		return 0
	for j in range(n - 1, 0, -1):
		if nums[j] != sortedNums[j]:
			break
	return j + 1 - i


assert findUnsortedSubarray([1]) == 0
assert findUnsortedSubarray([2, 1]) == 2
assert findUnsortedSubarray([2, 1, 3]) == 2
assert findUnsortedSubarray([1,1,2,1,1]) == 3
assert findUnsortedSubarray([3, 2, 1]) == 3
assert findUnsortedSubarray([2, 6, 4, 3, 7, 12, 11]) == 6
assert findUnsortedSubarray([6, 4, 3, 2, 7, 12, 11]) == 7
assert findUnsortedSubarray([2, 6, 6, 7, 8]) == 0
assert findUnsortedSubarray([9,8,7,1,11,1]) == 6
