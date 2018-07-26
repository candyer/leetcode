# https://leetcode.com/problems/minimum-size-subarray-sum/description/

# 209. Minimum Size Subarray Sum

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which 
# the sum >= s. If there isn't one, return 0 instead.

# Example: 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 



#############################
### binary search O(nlogn) ##
#############################
def minSubArrayLen(s, nums):
	"""
	:type s: int
	:type nums: List[int]
	:rtype: int
	"""
	n = len(nums)
	sums = [0]
	for num in nums:
		sums.append(sums[-1] + num)
	if sums[-1] < s:
		return 0

	min_lens = n    
	for i in range(n):
		left, right = i, n - 1
		while left <= right:
			mid = (left + right) / 2
			if sums[mid + 1] - sums[i] >= s:
				min_lens = min(min_lens, mid - i + 1)
				right = mid - 1
			else:
				left = mid + 1

	return min_lens


#############################
###    two pointer  O(n)  ###
#############################
def minSubArrayLen(s, nums):
	"""
	:type s: int
	:type nums: List[int]
	:rtype: int
	"""
	if s > sum(nums):
		return 0
	n = len(nums)
	min_lens = n
	start = end = curr_sum = 0
	while end < n:
		while curr_sum < s and end < n:
			curr_sum += nums[end]
			end += 1
		while curr_sum >= s and start < n:
			if end - start < min_lens:
				min_lens = end - start
			curr_sum -= nums[start]
			start += 1
	return min_lens


assert minSubArrayLen(0, []) == 0
assert minSubArrayLen(7, [2,3,1,2,4,3]) == 2
assert minSubArrayLen(6, [2,3,1,2,4,3]) == 2
assert minSubArrayLen(3, [2,3,1,2,4,3]) == 1
assert minSubArrayLen(14, [2,3,1,2,4,3]) == 6
assert minSubArrayLen(100, [2,3,1,2,4,3]) == 0
assert minSubArrayLen(10, [2,3,1,2,4,3]) == 4
assert minSubArrayLen(213,[12,28,83,4,25,26,25,2,25,25,25,12]) == 8

