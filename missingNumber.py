#https://leetcode.com/problems/missing-number/#/description
# leetcode 268 -- Missing Number  Difficulty: Medium

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.

# Note:
# Your algorithm should run in linear runtime complexity. 
#Could you implement it using only constant extra space complexity?

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    # solution 1, O(nlogn) running time
    if nums == []: return 0
    nums.sort()
    for index, num in enumerate(nums):
        if index != num:
            return index
    return index + 1


    # solution 2, O(n) running time
    if nums == []: return 0
    return ((len(nums))**2 + (len(nums)))/2 - sum(nums)

print missingNumber([]) #0
print missingNumber([0]) #1
print missingNumber([0,1,2,4,5,6]) #3
print missingNumber([4,3,1,5,6,7,0]) #2
print missingNumber([0,1]) #2
