# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3359/


# Largest Divisible Subset

# Given a set of distinct positive integers, find the largest subset 
# such that every pair (Si, Sj) of elements in this subset satisfies:

# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)

# Example 2:
# Input: [1,2,4,8]
# Output: [1,2,4,8]


from typing import List
def largestDivisibleSubset(nums: List[int]) -> List[int]:
	if nums == []:
		return []
	nums.sort()
	dp = [[num] for num in nums]
	for i in range(1, len(nums)):
		tmp = []
		for j in range(i):
			if nums[i] % nums[j] == 0 and len(dp[j])  > len(tmp):
				tmp = dp[j]
			dp[i] = tmp + [nums[i]]
	return max(dp, key=len)


assert(largestDivisibleSubset([]) == [])
assert(largestDivisibleSubset([1,2,3]) == [1, 2])
assert(largestDivisibleSubset([1,2,4,8]) == [1, 2, 4, 8])
assert(largestDivisibleSubset([1, 3, 4, 6, 9, 27]) == [1, 3, 9, 27])
assert(largestDivisibleSubset([1, 2, 3, 5, 6, 10, 25, 50]) == [1, 2, 10, 50])
assert(largestDivisibleSubset([4,8,10,240]) == [4, 8, 240])




