# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3494/


# House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
# All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if 
# two adjacent houses were broken into on the same night.

# Given a list of non-negative integers nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.


# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [0]
# Output: 0
 

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000


from typing import List
def rob_house(self, n: int, nums: List[int]):
	dp = [0] * n
	for i in range(n):
		dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
	return dp[-1]

def rob(self, nums: List[int]) -> int:
	n = len(nums)
	if n <= 2:
		return max(nums)
	return max(self.rob_house(n - 1, nums[:-1]), self.rob_house(n - 1, nums[1:]))


assert(rob([2, 3, 4, 5, 6, 8, 10]) == 20)
assert(rob([7, 3, 1, 5, 4, 1, 2]) == 13)
assert(rob([2,3,4,5]) == 8)
assert(rob([2,3,2]) == 3)
assert(rob([1,2,3,1]) == 4)
assert(rob([0]) == 0)
assert(rob([10, 2]) == 10)





