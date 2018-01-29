# https://leetcode.com/problems/sum-of-two-integers/description/

# 371. Sum of Two Integers

# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example:
# Given a = 1 and b = 2, return 3.


def getSum(a, b):
	"""
	:type a: int
	:type b: int
	:rtype: int
	"""
	return sum([a, b])

print getSum(1, 2)
print getSum(2, 3)