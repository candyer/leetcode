# https://leetcode.com/problems/perfect-squares/description/

# 279. Perfect Squares

# Given a positive integer n, find the least number of perfect square numbers 
# (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.



def numSquares(n):
	"""
	:type n: int
	:rtype: int
	"""
	dp = [0]
	count = 1
	while count <= n:
		tmp = float('inf')
		for i in range(1, int(count**0.5) + 1):
			remaining = count - i * i
			if dp[remaining] + 1 < tmp:
				tmp = dp[remaining] + 1
		dp.append(tmp)
		count += 1
	return dp[n]

assert numSquares(12) == 3
assert numSquares(23) == 4
assert numSquares(87) == 4
