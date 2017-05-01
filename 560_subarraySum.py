# https://leetcode.com/contest/leetcode-weekly-contest-30/problems/subarray-sum-equals-k/

# Given an array of integers and an integer k, you need to find the total number of 
# continuous subarrays whose sum equals to k.

# Example 1:   Input:nums = [1,1,1], k = 2    Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

import collections
def subarraySum(nums, k):
	count = collections.Counter()
	count[0] = 1
	res = tmp = 0
	for num in nums:
		tmp += num
		res += count[tmp-k]
		count[tmp] += 1
	return res

# print subarraySum([-815,388,230,365,-106,284,-222,-884,240,422,599,-315,-281,-14,29,-812,-55,106,-858,
# 		-581,-725,382,730,780,785,576,440,-378,529,-467,816,-754,983,-921,-616,-668,-6,-140,-795,-448,-96,-146,
# 		-435,141,951,933,566,821,-996,-380,542,810,-384,912,-442],62) #10
# print subarraySum([0,0,0,0,0,0,0,0,0,0], 0) #55
# print subarraySum([-3,13,3,1,2,4,0,7,10,5,5,0,10,0], 10) #10
# print subarraySum([28,54,7,-70,22,65,-6], 100) #1
# print subarraySum([1,1,1], 2) #2
# print subarraySum([-3,13,3,1,2,4,7,10,5,5,10], 10) #5
