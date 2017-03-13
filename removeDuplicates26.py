# Leetcode 26 -- Remove Duplicates from Sorted Array

# Given a sorted array, remove the duplicates in place such that each element appear only once 
# and return the new length.Do not allocate extra space for another array, you must do this in place 
# with constant memory.  For example, Given input array nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
# It doesn't matter what you leave beyond the new length.

def removeDuplicates26(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #solution 1 O(n^2), won't pass the test
    n = len(nums)
    for i in range(n - 1, -1, -1):
        if nums[i] in nums[:i]:
            nums.remove(nums[i])
            n -= 1
    return n

    #solution 2 O(n)
    if nums == []: return 0
    n = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[n]:
            nums[i], nums[n+1] = nums[n+1], nums[i]
            n = n + 1
    return n+1

print removeDuplicates26([3,3,4,4,5,5,6]) #4
print removeDuplicates26([]) #0
