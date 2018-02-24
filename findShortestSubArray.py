# https://leetcode.com/problems/degree-of-an-array/description/

# 697. Degree of an Array

# Given a non-empty array of non-negative integers nums, the degree of this array is defined 
# as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
# that has the same degree as nums.

# Example 1:   Input: [1, 2, 2, 3, 1]   Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:   Input: [1,2,2,3,1,4,2]   Output: 6

# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.



from collections import Counter as c, defaultdict 
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d1 = c(nums)
        d2 = defaultdict(list)
        n = len(nums)
        for i in range(n):
            d2[nums[i]].append(i)
        degree = max(d1.values())
        res = float('inf')
        for k, v in d1.items():
            if v == degree:
                res = min(res, d2[k][-1] - d2[k][0] + 1)
        return res




        