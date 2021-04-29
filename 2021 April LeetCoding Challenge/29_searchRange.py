# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3725/

# Find First and Last Position of Element in Sorted Array


# Given an array of integers nums sorted in ascending order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# Follow up: Could you write an algorithm with O(log n) runtime complexity?
 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
 
# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9


from typing import List

def find_starting_pos(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)  
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return right #right is the beginning of the target block

def searchRange(nums: List[int], target: int) -> List[int]:
    start = find_starting_pos(nums, target)
    print(start, find_starting_pos(nums, target + 1))
    if start == len(nums) or nums[start] != target:
        return [-1, -1]
    return [start, find_starting_pos(nums, target + 1) - 1]
    
assert(searchRange([5,7,7,8,8,10], 8) == [3, 4])
assert(searchRange([5,7,7,8,8,10], 6) == [-1, -1])
assert(searchRange([], 0) == [-1, -1])
assert(searchRange([3,3,3,3,4], 3) == [0, 3])            







