# Leetcode 283 -- Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    x = 0
    for y in range(len(nums)):
        if nums[y]:
            nums[y], nums[x] = nums[x], nums[y]
            x += 1


##########################################################################
def moveZeroes(nums):
	"""
	Do not return anything, modify nums in-place instead.
	"""
	n = len(nums)
	not_zero = 0
	for i in range(n):
		if nums[i] != 0:
			nums[not_zero] = nums[i]
			not_zero += 1
	for i in range(not_zero, n):
		nums[i] = 0
	return nums

assert(moveZeroes([1, 1, 1]) == [1, 1, 1])
assert(moveZeroes([0,1,0,3,12]) == [1, 3, 12, 0, 0])
assert(moveZeroes([0,1,0,3,12,4,0]) == [1, 3, 12, 4, 0, 0, 0])
assert(moveZeroes([1,0,3,12,4,0]) == [1, 3, 12, 4, 0, 0])
assert(moveZeroes([0,0,0,0,0]) == [0, 0, 0, 0, 0])
