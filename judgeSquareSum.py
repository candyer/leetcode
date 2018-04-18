# https://leetcode.com/problems/sum-of-square-numbers/description/


# 633. Sum of Square Numbers

# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5

# Example 2:
# Input: 3
# Output: False


def judgeSquareSum(c):
	"""
	:type c: int
	:rtype: bool
	"""
	i = 0
	square = set()
	while i * i <= c:
		square.add( i * i )
		if c - i * i in square:
			return True
		i += 1
	return False

assert judgeSquareSum(10000)  == True
assert judgeSquareSum(162) == True
assert judgeSquareSum(999999999) == False
assert judgeSquareSum(1000000000) == True
assert judgeSquareSum(0) == True
assert judgeSquareSum(1) == True
assert judgeSquareSum(2) == True
assert judgeSquareSum(3) == False
assert judgeSquareSum(4) == True
assert judgeSquareSum(5) == True
assert judgeSquareSum(3) == False
assert judgeSquareSum(18) == True
assert judgeSquareSum(242) == True


