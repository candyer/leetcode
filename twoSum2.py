# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# 167. Two Sum II - Input array is sorted


# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up 
# to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 
# must be less than index2.

# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


def twoSum(numbers, target):
	"""
	:type numbers: List[int]
	:type target: int
	:rtype: List[int]
	"""
	n = len(numbers)
	low, high = 0, n - 1
	while low < high:
		if numbers[low] + numbers[high] == target:
			return [low + 1, high + 1]
		elif numbers[low] + numbers[high] < target:
			low += 1
		else:
			high -= 1


assert twoSum([2,7,11,15], 9) == [1, 2]
assert twoSum([2,7,11,15], 17) == [1, 4]
assert twoSum([0,0,3,4], 0) == [1, 2]
assert twoSum([1,2,3,4,5,6,7,8,9], 12) == [3, 9]





