
# https://leetcode.com/problems/partition-equal-subset-sum/description/

# Given a non-empty array containing only positive integers, find if the array can be partitioned 
# into two subsets such that the sum of elements in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.

# Example 1:  Input: [1, 5, 11, 5]   Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:  Input: [1, 2, 3, 5]   Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

def can_partition(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	total = sum(nums)
	if total & 1: 
		return False	
	
	half = total / 2
	n = len(nums)
	dp = [False] * (half + 1)
	dp[0] = True

	for num in nums:
		for i in range(half, num - 1, -1):
			if dp[i - num]:
				dp[i] = True
	return dp[half]


assert can_partition([]) ==  True
assert can_partition([1,3,7,10,17]) ==  False
assert can_partition([1, 5, 11, 5]) ==  True
assert can_partition([1, 2, 3, 5]) ==  False
assert can_partition([3,3,3,4,5]) ==  True
assert can_partition([1,1,1,2,5,1,1]) ==  True
assert can_partition([22,8,19,30,86,46,66,74,93,66,73,58,6,3,44,10,21,4,76,100,65,11,30,87,50,39,53,51,97,60,1,2,25,66,67,87,89,13,64,63,81,80,94,5,20,75,74,80,56,32,54,75,19,28,80,25,59,96,1,12,100,81,49,33,90,13,83,31,77,41,58,64,39,62,100,42,49,43,73,90,85,72,21,79,75,79,43,88,33,98,5,27,45,24,83,53,65,65,63,100]) == True

