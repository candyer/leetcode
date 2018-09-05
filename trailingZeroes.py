# https://leetcode.com/problems/factorial-trailing-zeroes/description/


# 172. Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.

# Example 1:
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

# Note: Your solution should be in logarithmic time complexity.


def trailingZeroes(n):
	"""
	:type n: int
	:rtype: int
	"""
	res = 0
	while n >= 5:
		n /= 5
		res += n
	return res


assert trailingZeroes(3) == 0
assert trailingZeroes(5) == 1
assert trailingZeroes(7) == 1
assert trailingZeroes(25) == 6
assert trailingZeroes(51) == 12