# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3357/

# Sort Colors

# Given an array with n objects colored red, white or blue, sort them in-place so that 
# objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with 
# total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?


from typing import List
def sortColors(nums: List[int]) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	Three pointers
	"""
	n = len(nums)
	i, j, k = 0, 0, n - 1
	while j <= k:
		if nums[j] == 0:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
			j += 1
		elif nums[j] == 1:
			j += 1
		else:
			nums[j], nums[k] = nums[k], nums[j]
			k -= 1
	return nums


# print(sortColors([2,0,2,1,1,0]))
# print(sortColors([2, 0, 1, 2, 2, 1]))
# print(sortColors([1, 0, 2, 0, 0, 1]))
# print(sortColors([2, 1, 2, 1, 0, 1]))
# print(sortColors([1, 2, 0, 0, 1]))


