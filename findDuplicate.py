#Leetcode 287 --- Find the Duplicate Number

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
# prove that at least one duplicate number must exist. 
# Assume that there is only one duplicate number, find the duplicate one.

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.


def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    # too slow!
    # if nums == []: return 0
    # start = 0
    # while start < len(nums):
    #     for num in nums[start+1:]:
    #         if nums[start] == num:
    #             return num
    #     start += 1

    ## too slow!  O(1) space, O(n^2) running time
    # if nums == []:
    #     return 0
    # for i in nums:
    #     if nums.count(i) > 1:
    #         return i

    ### too slow! O(1) space, O(n^2) running time
    # if nums == []:
    #     return 0
    # for i in range(len(nums)):
    #     if nums[i] in nums[i+1:]:
    #         return nums[i]

    #### O(n) space, O(n) running time
    # if nums == []: return 0
    # d = {}
    # for num in nums:
    #     d[num] = d.get(num, 0) + 1
    # for key, count in d.items():
    #     if count > 1:
    #         return key


    ##### O(n) space, O(n) running time
    # if nums == []: return 0
    # d = set()
    # for num in nums:
    #     if num in d:
    #         return num
    #     d.add(num)

    ######  O(1) space, O(nlogn) runnig time.
    if nums == []: return 0
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return nums[i]


print findDuplicate([7,425,398,9,10,25,40,90,93,98,10000,98,75]) #98
print findDuplicate([1,16,5,3,4,6,6,8,9,8,2,10]) #6
print findDuplicate([]) #0
