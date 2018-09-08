# https://leetcode.com/problems/powx-n/description/


# 50. Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:
# Input: 2.00000, 10
# Output: 1024.00000

# Example 2:
# Input: 2.10000, 3
# Output: 9.26100

# Example 3:
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Note:
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [-231, 231 - 1]




def myPow(x, n):
	"""
	:type x: float
	:type n: int
	:rtype: float
	"""
	if n < 0: return 1 / myPow(x, -n)
	elif n == 0: return 1
	if n % 2:
		return x * myPow(x, n - 1)
	else:
		return myPow(x * x, n / 2)





print myPow(2.000, 10)# 1024.0
print myPow(2.10000, 3)# 9.261








