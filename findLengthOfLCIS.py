# https://leetcode.com/contest/leetcode-weekly-contest-49/problems/longest-continuous-increasing-subsequence/


# 674. Longest Continuous Increasing Subsequence My SubmissionsBack to Contest

# Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

# Example 1:   Input: [1,3,5,4,7]     Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, 
# it's not a continuous one where 5 and 7 are separated by 4. 

# Example 2:   Input: [2,2,2,2,2]     Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
# Note: Length of the array will not exceed 10,000.


def findLengthOfLCIS(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	n = len(nums)
	if n < 2: return n
	i, j = 0, 1
	res = 1
	while j < n:
		if nums[j - 1] < nums[j]:
			res = max(res, j - i + 1)
		else:
			i = j
		j += 1
	return res

print findLengthOfLCIS([]) #0
print findLengthOfLCIS([1, 3, 5, 4, 7]) #3
print findLengthOfLCIS([1, 3, 5, 4, 7, 2, 3, 4, 5]) #4
print findLengthOfLCIS([2, 2, 2, 2, 1, 2]) #2
print findLengthOfLCIS([2, 2, 2, 2, 2]) #1


