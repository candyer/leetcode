# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3608/

# Max Number of K-Sum Pairs


# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

 
# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= 10^9

from typing import List
def maxOperations(nums: List[int], k: int) -> int:
    nums.sort()
    l, r, count= 0, len(nums) - 1, 0
    while l < r:
        pair_sum = nums[l] + nums[r]
        if pair_sum == k:
            count += 1
            l += 1
            r -= 1
        elif pair_sum < k:
            l += 1
        else:
            r -= 1
    return count





from collections import Counter
from typing import List
def maxOperations(nums: List[int], k: int) -> int:
    d = Counter(nums)
    count = 0
    for key, val in d.items():
        if key * 2 == k:
            count += val // 2
        elif key <= k // 2 and k - key in d:
            count += min(val, d[k - key])
    return count

assert(maxOperations([1,2,3,4], 5) == 2)
assert(maxOperations([3,1,3,4,3], 6) == 1)
assert(maxOperations([1,2,3,4,5,6,7,8,9], 9) == 4)







