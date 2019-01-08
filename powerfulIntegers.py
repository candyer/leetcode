# https://leetcode.com/problems/powerful-integers/submissions/


# 970. Powerful Integers

# Given two non-negative integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
# Return a list of all powerful integers that have value less than or equal to bound.
# You may return the answer in any order.  In your answer, each value should occur at most once.

# Example 1:
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation: 
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2

# Example 2:
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
 
# Note:
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6


def powerfulIntegers(x, y, bound):
	"""
	:type x: int
	:type y: int
	:type bound: int
	:rtype: List[int]
	"""
	a = 0
	if x <= 1:
		a = 1
	else:
		while True:
			if pow(x, a) < bound:
				a += 1
			else:
				break
	b = 0
	if y <= 1:
		b = 1
	else:
		while True:
			if pow(y, b) < bound:
				b += 1
			else:
				break
	res = set()
	for i in range(a + 1):
		for j in range(b + 1):
			tmp = pow(x, i) + pow(y, j)
			if tmp <= bound:
				res.add(tmp)
	return list(res)


	
assert powerfulIntegers(2, 3, 10) == [2, 3, 4, 5, 7, 9, 10]
assert powerfulIntegers(3, 5, 15) == [2, 4, 6, 8, 10, 14]
assert powerfulIntegers(0, 5, 25) == [1, 2, 5, 6, 25]
assert powerfulIntegers(0, 0, 10) == [0, 1, 2]
assert powerfulIntegers(1, 1, 2) == [2]
assert powerfulIntegers(3, 7, 0) == []














