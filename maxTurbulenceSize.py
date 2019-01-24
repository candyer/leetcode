# https://leetcode.com/problems/longest-turbulent-subarray/description/


# 978. Longest Turbulent Subarray

# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# Return the length of a maximum size turbulent subarray of A.

# Example 1:
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])

# Example 2:
# Input: [4,8,12,16]
# Output: 2

# Example 3:
# Input: [100]
# Output: 1
 
# Note:
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9



def maxTurbulenceSize(A):
	"""
	:type A: List[int]
	:rtype: int
	"""
	n = len(A)
	res = 1
	tmp = [1] * n
	up = None
	i = 1
	while i < n:
		if A[i - 1] < A[i]:
			if up == False:
				tmp[i] = tmp[i - 1] + 1
			else:
				tmp[i] = 2
			up = True
		elif A[i - 1] > A[i]:
			if up == True:
				tmp[i] = tmp[i - 1] + 1
			else:
				tmp[i] = 2
			up = False
		else:
			up = None
		res = max(res, tmp[i])
		i += 1
	return res

assert maxTurbulenceSize([9,4,2,10,7,8,8,1,9]) == 5
assert maxTurbulenceSize([4,8,12,16]) == 2
assert maxTurbulenceSize([100]) == 1
assert maxTurbulenceSize([1, 1, 2, 2, 3, 3, 2, 4]) == 3




