# https://leetcode.com/problems/house-robber/#/description

# You are a professional robber planning to rob houses along a street. Each house has a 
# certain amount of money stashed, the only constraint stopping you from robbing each of them 
# is that adjacent houses have security system connected and it will automatically contact 
# the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, 
# determine the maximum amount of money you can rob tonight without alerting the police.

# Dynamic Programming  O(n) time,  O(n) space
def rob(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	n = len(nums)
	dp = [0] * (n + 1)
	if n > 0:
		dp[1] = nums[0]
	for i in range(2, n + 1):
		dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
	return dp[n]

print rob([1,3,5,6,7]) #13
print rob([]) #0
