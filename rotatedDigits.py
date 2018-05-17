# https://leetcode.com/problems/rotated-digits/description/

# 788. Rotated Digits

# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that 
# is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 
# rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other 
# number and become invalid.

# Now given a positive number N, how many numbers X from 1 to N are good?

# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:

# N  will be in range [1, 10000].


def is_good_number(n):
	rotate = {
		0: 0,
		1: 1,
		2: 5,
		5: 2,
		6: 9,
		8: 8,
		9: 6
	}

	tmp = []
	m = n
	while m:
		digit = m % 10
		if digit in rotate:
			tmp.append(str(rotate[digit]))
		else:
			return False
		m /= 10
	return str(n) != ''.join(tmp[::-1])


def rotatedDigits(N):
	"""
	:type N: int
	:rtype: int
	"""
	res = 0
	for i in range(1, N + 1):
		if is_good_number(i):
			res += 1
	return res

assert rotatedDigits(9996) == 2318
assert rotatedDigits(3453) == 975
assert rotatedDigits(96) == 38
assert rotatedDigits(20) == 9

