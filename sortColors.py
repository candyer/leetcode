
# Leetcode 75 -- Sort Colors

# Given an array with n objects colored red, white or blue, sort them so that objects of the 
# same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library''s sort function for this problem.
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    vals = [0, 0, 0]
    for i in nums:
        vals[i] += 1

    for i, val in enumerate([0] * vals[0] + [1] * vals[1] + [2] * vals[2]):
        nums[i] = val


print sortColors([]) #[]
print sortColors([1,0])
print sortColors([2,1,0])
print sortColors([0,2,1,2,2,0,1]) #[0,0,1,1,2,2,2]
print sortColors([2,2,1,2,2,1,1]) #[1,1,1,2,2,2,2]
