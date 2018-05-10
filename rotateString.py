# https://leetcode.com/problems/rotate-string/description/

# 796. Rotate String

# We are given two strings, A and B.

# A shift on A consists of taking string A and moving the leftmost character to the rightmost 
# position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return 
# True if and only if A can become B after some number of shifts on A.

# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true

# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# Note:

# A and B will have length at most 100.

def rotate(n, s, i):
	s = list(s)
	s[:] = s[n - i :] + s[: n - i]   
	return ''.join(s)

def rotateString(A, B):
	"""
	:type A: str
	:type B: str
	:rtype: bool
	"""		
	n = len(A)
	if A == B: return True
	i = 1
	while i < n:
		if rotate(n, A, i) == B:
			return True
		i += 1

	return False

assert rotateString('abcde', 'cdeab') == True
assert rotateString('abcde', 'abced') == False
assert rotateString('abcde', 'abce') == False
assert rotateString('', '') == True
assert rotateString('z', 'z') == True


