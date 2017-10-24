
# https://leetcode.com/problems/minimum-path-sum/description/
# 64. Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right 
# which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1->3->1->1->1 minimizes the sum.

def minPathSum(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	rows = len(grid)
	cols = len(grid[0])
	if rows == 0 or cols == 0: return 0
	dp = grid
	for r in range(rows):
		for c in range(cols):
			if r == 0 and c != 0:
				dp[r][c] += dp[r][c - 1]
			elif r != 0 and c == 0:
				dp[r][c] += dp[r - 1][c]
			elif r != 0 and c != 0:
				dp[r][c] += min(dp[r - 1][c], dp[r][c - 1])
	return dp[rows - 1][cols - 1]

assert minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7
assert minPathSum([[],[],[]]) == 0
assert minPathSum([[]]) == 0
assert minPathSum([[1, 2, 3], [3, 2, 1], [4, 7, 1], [2, 3, 6]]) == 13

