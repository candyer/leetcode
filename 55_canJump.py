# Leetcode 55 -- Jump Game

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# For example:
# A = [2,3,1,1,4], return true.   A = [3,2,1,0,4], return false.

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    step = nums[0]
    n = len(nums)
    for i in range(1, n):
        if step > 0:
            step -= 1
            step = max(step, nums[i])
        else:
            return False
    return True

print canJump([1,5,4,4,3,0,0,0,1]) #False
print canJump([7,5,7,5,5,7,4,6,1,6]) #True
print canJump([1,5,7,5,5,7,0,0,1,6]) #True
import random
a = [random.randrange(5) for _ in range(10)]
print a 
print canJump(a)
