# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3603/


# Minimum Operations to Reduce X to Zero


# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost 
# or the rightmost element from the array nums and subtract its value from x. 
# Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.



# Example 1:
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

# Example 2:
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1

# Example 3:
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= x <= 10^9

from typing import List
def minOperations(nums: List[int], x: int) -> int:
    n = len(nums)
    target = sum(nums) - x
    if target == 0:
        return n
    elif target < 0:
        return -1
    l = r = range_sum = range_len = 0
    while l <= r < n:
        range_sum += nums[r]
        r += 1
        while range_sum >= target:
            if range_sum == target:
                range_len = max(range_len, r - l)
            range_sum -= nums[l]
            l += 1
    if not range_len:
        return -1
    else:
        return n - range_len

assert(minOperations([1,1,4,2,3], 5) == 2)
assert(minOperations([5,6,7,8,9], 4) == -1)
assert(minOperations([3,2,20,1,1,3], 10) == 5)
assert(minOperations([3,2,20,1,1,3], 30) == 6)
assert(minOperations([3,2,20,1,1,3], 31) == -1)


