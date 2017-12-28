# Leetcode 343 -- Integer Break

# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
# Note: you may assume that n is not less than 2.


def integerBreak(n):
	"""
	:type n: int   n >= 2
	:rtype: int
	"""
	if n == 2: return 1
	if n == 3: return 2
	if n % 3 == 0:  return 3**(n/3)
	elif n % 3 == 1:  return 3**((n-4)/3) * 4
	elif n % 3 == 2:  return 3**(n/3) * 2


print integerBreak(57) # 1162261467 3**19
print integerBreak(58) # 1549681956 3**((58-4)/3) * 4
print integerBreak(59) # 2324522934 3**(59/3) * 2
