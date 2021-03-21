# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3676/


# Wiggle Subsequence


# Given an integer array nums, return the length of the longest wiggle sequence.
# A wiggle sequence is a sequence where the differences between successive numbers strictly alternate 
# between positive and negative. The first difference (if one exists) may be either positive or negative. 
# A sequence with fewer than two elements is trivially a wiggle sequence.

# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, 
# the first because its first two differences are positive and the second because its last difference is zero.
# A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, 
# leaving the remaining elements in their original order.


# Example 1:
# Input: nums = [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.

# Example 2:
# Input: nums = [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

# Example 3:
# Input: nums = [1,2,3,4,5,6,7,8,9]
# Output: 2
 

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
 

# Follow up: Could you solve this in O(n) time?

from typing import List

def wiggleMaxLength(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return n
    up, down = [1] * n, [1] * n
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] == nums[i - 1]:
            down[i] = down[i - 1]
            up[i] = up[i - 1]
        else:
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]
    return max(down[-1], up[-1])


assert(wiggleMaxLength([1,7,4,9,2,5]) == 6)
assert(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7)
assert(wiggleMaxLength([1,2,3,4,5,6,7,8,9]) == 2)
assert(wiggleMaxLength([1]) == 1)
assert(wiggleMaxLength([1,2]) == 2)
assert(wiggleMaxLength([1, 1]) == 1)



