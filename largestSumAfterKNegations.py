# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/


# 1005. Maximize Sum Of Array After K Negations


# Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], 
# and we repeat this process K times in total.  (We may choose the same index i multiple times.)

# Return the largest possible sum of the array after modifying it in this way.


# Example 1:
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].

# Example 2:
# Input: A = [3,-1,0,2], K = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].

# Example 3:
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].

# Note:
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100


def largestSumAfterKNegations(A, K):
	"""
	:type A: List[int]
	:type K: int
	:rtype: int
	"""
	negative = []
	zero = 0
	positive = []
	for num in A:
		if num < 0:
			negative.append(num)
		elif num == 0:
			zero += 1
		else:
			positive.append(num)
	negative.sort()
	for i in range(len(negative)):
		if K > 0:
			K -= 1
			positive.append(-negative[i])
			negative[i] = 0
	res = sum(positive) + sum(negative)
	if zero > 0:
		return res
	positive.sort()
	mini = positive[0]
	
	if K % 2 == 0:
		return res
	else:
		return res - mini * 2


assert largestSumAfterKNegations([0,0,0,0,0], 9) == 0
assert largestSumAfterKNegations([-1,-2,-3,-4], 9) == 8
assert largestSumAfterKNegations([1,2,3,4], 10) == 10
assert largestSumAfterKNegations([4,2,3], 1) == 5
assert largestSumAfterKNegations([3,-1,0,2], 3) == 6 
assert largestSumAfterKNegations([2,-3,-1,5,-4], 2) == 13 



