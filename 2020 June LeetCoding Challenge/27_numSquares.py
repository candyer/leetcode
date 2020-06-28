# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3373/


# Perfect Squares

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


def numSquares(n: int) -> int:
	dp = [float('inf')] * (n + 1)
	dp[0] = 0
	for i in range(1, int(n ** 0.5) + 1):
		dp[i * i] = 1

	for i in range(1, n):
		j = 1
		while i + j * j <= n:
			dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])
			j += 1
	return dp[n]

assert(numSquares(12) == 3)
assert(numSquares(13) == 2)
assert(numSquares(8) == 2)
assert(numSquares(23) == 4)



