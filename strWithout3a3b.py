# https://leetcode.com/problems/string-without-aaa-or-bbb/description/


# 984. String Without AAA or BBB


# Given two integers A and B, return any string S such that:

# S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.
 

# Example 1:
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.

# Example 2:
# Input: A = 4, B = 1
# Output: "aabaa"

# Note:
# 0 <= A <= 100
# 0 <= B <= 100
# It is guaranteed such an S exists for the given A and B.


def f(n, A, B, x, y):
	'''A >= B'''
	res = [0] * n
	for i in range(2, n, 3):
		if A > 0:
			res[i] = x
			A -= 1
	for j in range(1, n, 3):
		if B > 0:
			res[j] = y
			B -= 1
	for k in range(0, n, 3):
		if B > 0:
			res[k] = y
			B -= 1
		else:
			res[k] = x
			A -= 1
	return ''.join(res)

def strWithout3a3b(A, B):
	"""
	:type A: int
	:type B: int
	:rtype: str
	"""
	n = A + B
	if A < B:
		return f(n, A, B, 'a', 'b')
	return f(n, B, A, 'b', 'a')


assert strWithout3a3b(5, 2) == 'aabaaba'
assert strWithout3a3b(1, 3) == 'bbab'
assert strWithout3a3b(1, 2) == 'bba'
assert strWithout3a3b(4, 4) == 'aabbabba'
assert strWithout3a3b(3, 3) == 'aabbab'
assert strWithout3a3b(8, 5) == 'aabaabaabaabb'
assert strWithout3a3b(8, 3) == 'aabaabaabaa'


