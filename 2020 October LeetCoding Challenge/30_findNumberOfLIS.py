# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3513/


# Number of Longest Increasing Subsequence


# Given an integer array nums, return the number of longest increasing subsequences.

# Example 1:
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

# Example 2:
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, 
# and there are 5 subsequences' length is 1, so output 5.
 

# Constraints:
# 0 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6


from typing import List
def findNumberOfLIS(nums: List[int]) -> int:
	n = len(nums)
	if n <= 1: 
		return n
	length = [1] * n
	count = [1] * n
	for right in range(n):
		for left in range(right):
			if nums[left] < nums[right]:
				if length[left] >= length[right]:
					length[right] = length[left] + 1
					count[right] = count[left]
				elif length[left] + 1 == length[right]:
					count[right] += count[left]

	longest = max(length)
	res = 0
	for l, c in zip(length, count):
		if l == longest:
			res += c
	return res


assert(findNumberOfLIS([1,2,4,3,5,4,7,2]) == 3)
assert(findNumberOfLIS([1,1,1,2,2,2,3,3,3]) == 27)
assert(findNumberOfLIS([]) == 0)
assert(findNumberOfLIS([1]) == 1)
assert(findNumberOfLIS([1,3,5,4,7]) == 2)
assert(findNumberOfLIS([2,2,2,2,2]) == 5)
assert(findNumberOfLIS([5,4,3,2,10]) == 4)
assert(findNumberOfLIS([5,4,3,2,10]) == 4)
assert(findNumberOfLIS([2, 5, 8, 7, 10, 9]) == 4)
assert(findNumberOfLIS([2, 5, 8, 7, 10, 9, 1, 2, 3, 4]) == 5)
assert(findNumberOfLIS([1, 2, 3, 1, 1, 1]) == 1)






