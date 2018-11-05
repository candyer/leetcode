# https://leetcode.com/problems/max-area-of-island/description/

# 695. Max Area of Island

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.


def area(grid, row, col, visited, rows, cols):
	if not (0 <= row < rows and 0 <= col < cols and (row, col) not in visited and grid[row][col]):
		return 0
	visited.add((row, col))
	return (1 + area(grid, row + 1, col, visited, rows, cols) 
			  + area(grid, row - 1, col, visited, rows, cols) 
			  + area(grid, row, col - 1, visited, rows, cols) 
			  + area(grid, row, col + 1, visited, rows, cols))


def maxAreaOfIsland(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	rows = len(grid)
	cols = len(grid[0])
	res = 0
	visited = set()
	for row in range(rows):
		for col in range(cols):
			tmp = area(grid, row, col, visited, rows, cols)
			res = max(res, tmp)
	return res


print maxAreaOfIsland([
		[0,0,1,0,0,0,0,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,1,0,0,0],
		[0,1,1,0,1,0,0,0,0,0,0,0,0],
		[0,1,0,0,1,1,0,0,1,0,1,0,0],
		[0,1,0,0,1,1,0,0,1,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,0,0],
		[0,0,0,0,0,0,0,1,1,1,0,0,0],
		[0,0,0,0,0,0,0,1,1,0,0,0,0]]) #6

print maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) #0

