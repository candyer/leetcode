# https://leetcode.com/problems/sum-of-subarray-minimums/description/

# 907. Sum of Subarray Minimums

# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
# Since the answer may be large, return the answer modulo 10^9 + 7.

 
# Example 1:
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
 

# Note:
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000


def left_min(n, array):
	left = [-1] * n
	stack = [0]
	for i in range(1, n):
		if array[i] > array[stack[-1]]:
			left[i] = stack[-1]
		else:
			while stack and array[i] <= array[stack[-1]]:
				stack.pop()
			if stack:
				left[i] = stack[-1]
		stack.append(i)
	return left

def right_min(n, array):
	right = [n] * n
	stack = [n - 1]
	for i in range(n - 2, -1, -1):
		if array[i] > array[stack[-1]]:
			right[i] = stack[-1]
		else:
			while stack and array[i] < array[stack[-1]]:
				stack.pop()
			if stack:
				right[i] = stack[-1]
		stack.append(i)
	return right

def sumSubarrayMins(A):
	"""
	:type A: List[int]
	:rtype: int
	"""
	mod = 10**9 + 7
	res = 0
	n = len(A)
	left = left_min(n, A)
	right = right_min(n, A)
	for i in range(n):
		res += A[i] * (i - left[i]) * (right[i] - i)
		res %= mod
	return res

assert sumSubarrayMins([3,1,2,4]) == 17
assert sumSubarrayMins([4,3,6,4,8,1,5,2]) == 85
assert sumSubarrayMins([10, 5, 3, 7, 0, 4, 5, 2, 1,8]) == 80


