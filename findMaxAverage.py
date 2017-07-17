# https://leetcode.com/contest/leetcode-weekly-contest-41/problems/maximum-average-subarray-i/


# 643. Maximum Average Subarray I
# Given an array consisting of n integers, find the contiguous subarray of given length k that has the 
# maximum average value. And you need to output the maximum average value.

# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4       Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

# Note:
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].


def findMaxAverage(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: float
	"""
	maxi = last = sum(nums[:k])
	for i in range(k, len(nums)):
		last = last - nums[i - k] + nums[i]
		maxi = max(maxi, last)
	return maxi / float(k)


print findMaxAverage([1,12,-5,-6,50,3], 1) #50.00000
print findMaxAverage([1,12,-5,-6,50,3], 2) #26.50000
print findMaxAverage([1,12,-5,-6,50,3], 3) #15.66667
print findMaxAverage([1,12,-5,-6,50,3], 4) #12.75000
