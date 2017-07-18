# https://leetcode.com/problems/contains-duplicate-ii/#/description
# leetcode 219 - Contains Duplicate II

# Given an array of integers and an integer k, 
# find out whether there are two distinct indices i and j in the array 
# such that nums[i] = nums[j] and the difference between i and j is at most k.

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    d = {}
    for i in xrange(len(nums)):
        index = d.get(nums[i])
        if index >= 0 and i - index <= k:
            return True
        d[nums[i]] = i 
    return False

# print containsNearbyDuplicate([1,1,3,3,5,2,6],4) # True
# print containsNearbyDuplicate([1,1,3,2,3,5,2,6],1) # True
# print containsNearbyDuplicate([1,7,3,8,7,10,2,1],3) # True
# print containsNearbyDuplicate([1,7,3,8,7,10,2,1],2) #False
# print containsNearbyDuplicate([],2) #False
# print containsNearbyDuplicate([1,0,1,1],1) #True
