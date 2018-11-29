# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/


# Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
# Return the least number of moves to make every value in A unique.

# Example 1:
# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].

# Example 2:
# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 
# Note:
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000


def minIncrementForUnique(A):
	"""
	:type A: List[int]
	:rtype: int
	"""
	n = len(A)
	if n <= 1:
		return 0
	A.sort()
	count = 0
	i = 0
	while i < n - 1:
		if A[i + 1] <= A[i]:
			tmp = A[i] - A[i + 1] + 1
			count += tmp
			A[i + 1] += tmp
		i += 1
	return count

assert minIncrementForUnique([]) == 0
assert minIncrementForUnique([1,2]) == 0
assert minIncrementForUnique([1,2,2]) == 1
assert minIncrementForUnique([3,2,1,2,1,7]) == 6








