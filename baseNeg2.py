# https://leetcode.com/problems/convert-to-base-2/description/


# 1017. Convert to Base -2


# Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

# The returned string must have no leading zeroes, unless the string is "0".

# Example 1:
# Input: 2
# Output: "110"
# Explantion: (-2) ^ 2 + (-2) ^ 1 = 2

# Example 2:
# Input: 3
# Output: "111"
# Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

# Example 3:
# Input: 4
# Output: "100"
# Explantion: (-2) ^ 2 = 4
 

# Note:
# 0 <= N <= 10^9


def baseNeg2(N):
	"""
	:type N: int
	:rtype: str
	"""
	if N == 0:
		return '0'
	res = []
	while N:
		res.append(str(N % 2))
		N = -(N / 2)
	return ''.join(res[::-1])


assert baseNeg2(2) == '110'
assert baseNeg2(3) == '111'
assert baseNeg2(4) == '100'
assert baseNeg2(0) == '0'
assert baseNeg2(999999999) == '1001100111011111101111000000011'



