# https://leetcode.com/problems/house-robber-ii/#/description


# After robbing those houses on that street, the thief has found himself a new place 
# for his thievery so that he will not get too much attention. This time, all houses 
# at this place are arranged in a circle. That means the first house is the neighbor 
# of the last one. Meanwhile, the security system for these houses remain the same as 
# for those in the previous street.

# Given a list of non-negative integers representing the amount of money of each house, 
# determine the maximum amount of money you can rob tonight without alerting the police.


def rob(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	n = len(nums)
	dp1 = [0] * (n + 1)
	dp2 = [0] * (n + 1)
	if n == 0: return 0
	elif n == 1: return nums[0]
	dp1[1] = nums[0]
	for i in range(2, n):
		dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i - 1])
		dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i - 1])
	dp1[-1] = dp1[-2]
	dp2[-1] = max(dp2[-2], dp2[-3] + nums[-1])
	return max(dp1[-1], dp2[-1])


print rob([7,4,1,3,6,5]) #15
print rob([7, 2]) #7
print rob([2, 1, 1, 2])

