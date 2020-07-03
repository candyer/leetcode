# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/543/week-5-june-29th-june-30th/3375/

# Unique Paths

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the 
# bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?
 
# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Example 2:
# Input: m = 7, n = 3
# Output: 28

# Constraints:
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

##########################################################################
def uniquePaths(m: int, n: int) -> int:
	dp = [[1 for i in range(n)] for i in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
	return dp[m - 1][n - 1]


##########################################################################
from math import factorial 
def uniquePaths(m, n):
	return factorial(m + n - 2) // (factorial(n - 1) * factorial(m - 1))


assert(uniquePaths(1, 1) == 1)
assert(uniquePaths(3, 1) == 1)
assert(uniquePaths(3, 2) == 3)
assert(uniquePaths(7, 3) == 28)
assert(uniquePaths(4, 4) == 20)
assert(uniquePaths(5, 5) == 70)

