# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3652/


# Shortest Unsorted Continuous Subarray


# Given an integer array nums, you need to find one continuous subarray that if you only sort 
# this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

 
# Example 1:
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 0

# Example 3:
# Input: nums = [1]
# Output: 0
 

# Constraints:
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5

# Follow up: Can you solve it in O(n) time complexity?


from typing import List
def findUnsortedSubarray(nums: List[int]) -> int:
    arr = sorted(nums)
    n = len(nums)
    if n == 1:
        return 0
    if arr == nums:
        return 0
    left, right = 0, n - 1
    
    while left < right:
        if nums[left] != arr[left] and nums[right] != arr[right]:
            return right - left + 1
        if nums[left] == arr[left]:
            left += 1
        if nums[right] == arr[right]:
            right -= 1
    return right - left + 1

assert(findUnsortedSubarray([2,6,4,8,10,9,15]) == 5)
assert(findUnsortedSubarray([1,2,3,4]) == 0)
assert(findUnsortedSubarray([1]) == 0)






