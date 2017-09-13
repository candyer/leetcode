# https://leetcode.com/contest/leetcode-weekly-contest-47/problems/non-decreasing-array/

# Given an array with n integers, your task is to check if it could become non-decreasing by 
# modifying at most 1 element.
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

# Example 1:   Input: [4,2,3]   Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

# Example 2:   Input: [4,2,1]   Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].



def checkPossibility(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	count = 0
	for i in range(len(nums) - 1):
		if nums[i] > nums[i + 1]:
			count += 1
			if i == 0:
				nums[i] = nums[i + 1]
			elif nums[i - 1] <= nums[i + 1]:
				nums[i] = nums[i - 1]
			else:
				nums[i + 1] = nums[i]
		if count > 1:
			return False
	return True

print checkPossibility([4,2,3]) #True
print checkPossibility([4,2,1]) #False
print checkPossibility([]) #True
print checkPossibility([3, 4, 2, 3]) #False
print checkPossibility([5, 4, 2, 3]) #False
