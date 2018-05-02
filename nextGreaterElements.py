# https://leetcode.com/problems/next-greater-element-ii/description/

# 503. Next Greater Element II


# Given a circular array (the next element of the last element is the first element of the array), 
# print the Next Greater Number for every element. The Next Greater Number of a number x is the first 
# greater number to its traversing-order next in the array, which means you could search circularly to 
# find its next greater number. If it doesn't exist, output -1 for this number.

# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.


def nextGreaterElements(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	if nums == []: return []

	n = len(nums)
	maxi = max(nums)
	start = nums.index(maxi)
	nums = nums[start + 1 : ] + nums[:start + 1]
	res = [-1] * n
	stack = []
	for i in range(n - 1, -1, -1):
		while stack and nums[i] >= stack[-1]:
			stack.pop()
		if stack:
			res[i] = stack[-1]
		stack.append(nums[i])
		
	return res[n - start - 1:] + res[: n - start - 1]

assert nextGreaterElements([1,2,1]) == [2, -1, 2]
assert nextGreaterElements([1,3,4,2]) == [3, 4, -1, 3]
assert nextGreaterElements([1,3,4,10,1,5,8]) == [3, 4, 10, -1, 5, 8, 10]
assert nextGreaterElements([1]) == [-1]
assert nextGreaterElements([]) == []


