
# https://leetcode.com/problems/maximum-subarray/description/
# 53. Maximum Subarray

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

def max_subArray(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""

	## brute force, too slow
	n = len(nums)
	if n == 0: return 0
	res = float('-inf')
	for i in range(n):
		for j in range(i + 1, n + 1):
			res = max(res, sum(nums[i: j]))
	return res

	##
	n = len(nums)
	if n == 0: return 0
	for i in range(1, n):
		if nums[i - 1] > 0:
			nums[i] += nums[i - 1]
	return max(nums)

	### DP
	n = len(nums)
	if n == 0: return 0
	current_sum = res = nums[0]
	for num in nums[1:]:
		current_sum = max(num, current_sum + num)
		res = max(res, current_sum)
	return res

assert max_subArray([2,1,3,-4,1,-2,1,5,-4]) == 7
assert max_subArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert max_subArray([]) == 0
assert max_subArray([-9, 8, -2, 10, -5]) == 16
assert max_subArray([-9, -8, -2, -1, -5]) == -1
