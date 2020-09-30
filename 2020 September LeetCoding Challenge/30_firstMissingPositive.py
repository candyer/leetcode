# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/558/week-5-september-29th-september-30th/3478/


# First Missing Positive

# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:
# Input: [1,2,0]
# Output: 3

# Example 2:
# Input: [3,4,-1,1]
# Output: 2

# Example 3:
# Input: [7,8,9,11,12]
# Output: 1

# Follow up:
# Your algorithm should run in O(n) time and uses constant extra space.


from typing import List
def firstMissingPositive(nums: List[int]) -> int:
	n = len(nums)
	for i in range(n):
		while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
			nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
	for i in range(n):
		if i + 1 != nums[i]:
			return i + 1
	return n + 1


assert(firstMissingPositive([]) == 1)
assert(firstMissingPositive([1, 1]) == 2)
assert(firstMissingPositive([100, 3, 1, 2]) == 4)
assert(firstMissingPositive([1,2,0]) == 3)
assert(firstMissingPositive([3,4,-1,1]) == 2)
assert(firstMissingPositive([7,8,9,11,12]) == 1)
assert(firstMissingPositive([3, 1, 2, -1]) == 4)
