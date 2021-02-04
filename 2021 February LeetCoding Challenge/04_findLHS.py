# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/



# Longest Harmonious Subsequence

# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
# A subsequence of array is a sequence that can be derived from the array by deleting some or 
# no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 2

# Example 3:
# Input: nums = [1,1,1,1]
# Output: 0
 

# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -10^9 <= nums[i] <= 10^9


# from typing import List
# from collections import Counter
# def findLHS(nums: List[int]) -> int:
#     d = Counter(nums)
#     res = 0
#     keys = sorted(d.keys())
#     for i in range(len(keys) - 1):
#         if keys[i] + 1 == keys[i + 1]:
#             res = max(res, d[keys[i]] + d[keys[i + 1]])
#     return res

from typing import List
from collections import Counter
def findLHS(nums: List[int]) -> int:
    d = Counter(nums)
    res = 0
    for key, val in d.items():
        if key + 1 in d:
            res = max(res, val + d[key + 1])
    return res


assert(findLHS([1,3,2,2,5,2,3,7]) == 5)
assert(findLHS([1,2,3,4]) == 2)
assert(findLHS([1,1,1,1]) == 0)
