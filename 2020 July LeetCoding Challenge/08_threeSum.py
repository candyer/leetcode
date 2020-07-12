# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3384/

# 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums such that 
# a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]



from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
	res = []
	nums.sort()
	n = len(nums)
	for a in range(n - 2):
		if nums[a] > 0: 
			break
		if a > 0 and nums[a] == nums[a-1]: 
			continue

		b, c = a + 1, n - 1
		while b < c:
			total = nums[a] + nums[b] + nums[c]
			if total < 0:
				b += 1
			elif total>0:
				c -= 1
			else:
				res.append([nums[a], nums[b], nums[c]])
				while b < c and nums[b] == nums[b + 1]:
					b += 1
				while b < c and nums[c] == nums[c - 1]:
					c -= 1
				b += 1
				c -= 1
	return res

assert(threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
assert(threeSum([-2, 1, 1]) == [[-2, 1, 1]])
assert(threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
assert(threeSum([-1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == [[-1, 0, 1], [0, 0, 0]])

