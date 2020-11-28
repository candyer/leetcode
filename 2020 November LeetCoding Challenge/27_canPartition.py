# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/567/week-4-november-22nd-november-28th/3545/

# Partition Equal Subset Sum


# Given a non-empty array nums containing only positive integers, 
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

from typing import List
def canPartition(nums: List[int]) -> bool:
	total = sum(nums)
	if total % 2:
		return False
	n = len(nums)
	half = total // 2
	dp = [False] * (half + 1)
	dp[0] = True 
	for num in nums:
		for i in range(half, num - 1, -1):
			if dp[i - num]:
				dp[i] = True
	return dp[-1]


assert(canPartition([1,5,11,5]) == True)
assert(canPartition([1,2,3,6]) == True)
assert(canPartition([1,2,8,9]) == True)
assert(canPartition([1, 3,4,8]) == True)
assert(canPartition([10]) == False)
assert(canPartition([3,7,8]) == False)
assert(canPartition([1,2,3,5]) == False)






