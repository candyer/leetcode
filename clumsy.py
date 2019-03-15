# https://leetcode.com/problems/clumsy-factorial/description/


# 1006. Clumsy Factorial


# Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  
# For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

# We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for 
# a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using 
# the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction 
# steps, and multiplication and division steps are processed left to right.

# Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.

# Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.

 
# Example 1:
# Input: 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1

# Example 2:
# Input: 10
# Output: 12
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
 
# Note:
# 1 <= N <= 10000
# -2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)


def clumsy(N):
	"""
	:type N: int
	:rtype: int
	"""
	if N <= 2: return [1, 2][N - 1]
	res = 0
	tmp = N
	j = 1
	for i in range(N - 1, 0, -1):
		op = j % 4
		if op == 1:
			tmp *= i
		elif op == 2:
			tmp /= i
			if j < 4:
				res += tmp
			else:
				res -= tmp
		elif op == 3:
			res += i
		else:
			tmp = i
		j += 1
	if op in [0, 1]:
		res -= tmp
	return res



def clumsy1(N):
	if N <= 4:
		return [1, 2, 6, 7][N - 1]
	op = N % 4
	if op == 0:
		return N + 1
	elif op in [1, 2]:
		return N + 2
	else:
		return N - 1


assert clumsy(1) == 1
assert clumsy(2) == 2
assert clumsy(3) == 6
assert clumsy(4) == 7
assert clumsy(5) == 7
assert clumsy(6) == 8
assert clumsy(7) == 6
assert clumsy(8) == 9
assert clumsy(9) == 11
assert clumsy(10) == 12
assert clumsy(10) == 12
assert clumsy(13) == 15
assert clumsy(401) == 403
assert clumsy(10000) == 10001


