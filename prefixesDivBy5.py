# https://leetcode.com/problems/binary-prefix-divisible-by-5/description/


# 1018. Binary Prefix Divisible By 5

# Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number 
# (from most-significant-bit to least-significant-bit.)

# Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.


# Example 1:
# Input: [0,1,1]
# Output: [true,false,false]
# Explanation: 
# The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, 
# so answer[0] is true.

# Example 2:
# Input: [1,1,1]
# Output: [false,false,false]

# Example 3:
# Input: [0,1,1,1,1,1]
# Output: [true,false,false,false,true,false]

# Example 4:
# Input: [1,1,1,0,1]
# Output: [false,false,false,false,false]
 

# Note:
# 1 <= A.length <= 30000
# A[i] is 0 or 1


def prefixesDivBy5(A):
	"""
	:type A: List[int]
	:rtype: List[bool]
	"""
	res = []
	tmp = 0
	if A[0] == 1:
		tmp = 1
		res.append(False)
	else:
		tmp = 0
		res.append(True)
	for i in range(1, len(A)):
		tmp *= 2
		if A[i] == 1:
			tmp += 1
		res.append(tmp % 5 == 0)
	return res


assert prefixesDivBy5([0,1,1]) == [True, False, False]
assert prefixesDivBy5([1,1,1]) == [False, False, False]
assert prefixesDivBy5([0,1,1,1,1,1]) == [True, False, False, False, True, False]
assert prefixesDivBy5([1,1,1,0,1]) == [False, False, False, False, False]
assert prefixesDivBy5([1,0,1,0,1]) == [False, False, True, True, False]


