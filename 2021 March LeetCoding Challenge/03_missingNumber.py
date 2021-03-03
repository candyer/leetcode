# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659/

# Missing Number


# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

 
# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
# 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
# 8 is the missing number in the range since it does not appear in nums.

# Example 4:
# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 
# 1 is the missing number in the range since it does not appear in nums.
 
# Constraints:
# n == nums.length
# 1 <= n <= 10^4
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

from typing import List

def missingNumber(nums: List[int]) -> int:
    '''
    Time Complexiy: O(n^2)
    space Complexiy: O(1)
    '''
    n = len(nums)
    for i in range(n + 1):
        if i not in nums:
            return i



def missingNumber(nums: List[int]) -> int:
    '''
    Time Complexiy: O(n)
    space Complexiy: O(n)
    '''
    n = len(nums)
    nums = set(nums)
    for i in range(n + 1):
        if i not in nums:
            return i



def missingNumber(nums: List[int]) -> int:
    '''
    Time Complexiy: O(n)
    space Complexiy: O(1)
    '''
    n = len(nums)
    return sum(range(n + 1)) - sum(nums)
    return n * (n + 1) // 2 - sum(nums)



assert(missingNumber([3,0,1]) == 2)
assert(missingNumber([0,1]) == 2)
assert(missingNumber([9,6,4,2,3,5,7,0,1]) == 8)
assert(missingNumber([0]) == 1)
        

