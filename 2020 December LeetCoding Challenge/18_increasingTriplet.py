# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3570/

# Increasing Triplet Subsequence


# Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
# such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 
# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

# Constraints:
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
 
# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?


from typing import List
def increasingTriplet(nums: List[int]) -> bool:
        n = len(nums)
        left, right = 0, n - 1
        while left < right and nums[right] - nums[left] < 2:
            right -= 1
        if right - left < 2:
            right = n - 1
            while left < right and nums[right] - nums[left] < 2:
                left += 1          
        i = left + 1
        while i < right and left < right:
            if nums[left] < nums[i] < nums[right]:
                return True
            elif nums[i] <= nums[left]:
                left = i
            i += 1
        return False



#################################################################
def increasingTriplet(nums: List[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

assert(increasingTriplet([1,2,3,4,5]) == True)
assert(increasingTriplet([5,4,3,2,1]) == False)
assert(increasingTriplet([2,1,5,0,4,6]) == True)
assert(increasingTriplet([6,5,4,3,4,5]) == True)
assert(increasingTriplet([1,2,3,4,5,6,2,1]) == True)
assert(increasingTriplet([9,8,7,6,5,6,7]) == True)
assert(increasingTriplet([1,3,3,3,2]) == False)
assert(increasingTriplet([2,1,5,0,3,4]) == True)











