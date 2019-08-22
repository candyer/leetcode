# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/description/

# 1144. Decrease Elements To Make Array Zigzag

# Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

# An array A is a zigzag array if either:

# Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
# OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
# Return the minimum number of moves to transform the given array nums into a zigzag array.

# Example 1:
# Input: nums = [1,2,3]
# Output: 2
# Explanation: We can decrease 2 to 0 or 3 to 1.

# Example 2:
# Input: nums = [9,6,1,6,2]
# Output: 4

# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000


def even(n, nums):
	'''count how many moves needed if even position is smaller than odd position'''
	count = 0
	for i in range(n - 1):
		if i % 2 == 0 and nums[i] >= nums[i + 1]:
			count += nums[i] - nums[i + 1] + 1
			nums[i] = nums[i + 1] - 1
		if i % 2 != 0 and nums[i] <= nums[i + 1]:
			count += nums[i + 1] - nums[i] + 1
			nums[i + 1] = nums[i] - 1 
	return count


def odd(n, nums):
	'''count how many moves needed if odd position is smaller than even position'''
	count = 0
	for i in range(n - 1):
		if i % 2 != 0 and nums[i] >= nums[i + 1]:
			count += nums[i] - nums[i + 1] + 1
			nums[i] = nums[i + 1] - 1

		if i % 2 == 0 and nums[i] <= nums[i + 1]:
			count += nums[i + 1] - nums[i] + 1
			nums[i + 1] = nums[i] - 1
	return count


def movesToMakeZigzag(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	n = len(nums)
	return min(even(n, nums[:]), odd(n, nums[:]))


assert movesToMakeZigzag([1,2,3]) == 2
assert movesToMakeZigzag([9,6,1,6,2]) == 4
assert movesToMakeZigzag([1, 2, 3, 4]) == 2
assert movesToMakeZigzag([5, 5, 5, 5, 5]) == 2













