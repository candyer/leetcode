# ohttps://leetcode.com/problems/smallest-range-ii/description/



# 910. Smallest Range II


# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).
# After this process, we have some array B.
# Return the smallest possible difference between the maximum value of B and the minimum value of B.


# Example 1:
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]

# Example 2:
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]

# Example 3:
# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]
 

# Note:
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000


from collections import Counter as c
def smallestRangeII(A, K):
	"""
	:type A: List[int]
	:type K: int
	:rtype: int
	"""
	A.sort()
	mini, maxi = A[0], A[-1]
	res = maxi - mini
	for i in range(len(A) - 1):
		a = min(mini + K, A[i + 1] - K)
		b = max(maxi - K, A[i] + K)
		res = min(res, b - a)
	return res

assert smallestRangeII([1], 0) == 0
assert smallestRangeII([0, 10], 2) == 6
assert smallestRangeII([1, 3, 6], 3) == 3
assert smallestRangeII([9, 0, 8, 5, 4, 0, 10, 0, 8, 8], 6) == 8
assert smallestRangeII([9, 0, 8, 5, 4, 0, 10, 0, 8, 8], 7) == 10
assert smallestRangeII([4, 10, 2, 1, 10, 0, 10, 0, 10, 9], 9) == 10
assert smallestRangeII([1, 2, 8, 9, 10, 20], 9) == 9
assert smallestRangeII([1, 2, 8], 9) == 7
assert smallestRangeII([1, 2, 9], 9) == 8
assert smallestRangeII([1, 2, 9], 6) == 5







