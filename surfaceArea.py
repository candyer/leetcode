# https://leetcode.com/problems/surface-area-of-3d-shapes/description/

# 892. Surface Area of 3D Shapes

# On a N * N grid, we place some 1 * 1 * 1 cubes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
# Return the total surface area of the resulting shapes.
 
# Example 1:
# Input: [[2]]
# Output: 10

# Example 2:
# Input: [[1,2],[3,4]]
# Output: 34

# Example 3:
# Input: [[1,0],[0,2]]
# Output: 16

# Example 4:
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32

# Example 5:
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
 
# Note:
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50




def surfaceArea(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	res = 0
	n = len(grid)
	if n == 0:
		return 0
	elif n == 1:
		return grid[0][0] * 4 + 2
	grid = [[0] * (n + 2)] + grid
	
	for i in range(1, n + 1):
		grid[i] = [0] + grid[i] + [0]
	grid.append([0] * (n + 2))

	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if grid[i][j] > 0:
				res += 2
				if grid[i - 1][j] < grid[i][j]: #'up'
					res += grid[i][j] - grid[i - 1][j]
				if grid[i + 1][j] < grid[i][j]: #'down'
					res += grid[i][j] - grid[i + 1][j]
				if grid[i][j - 1] < grid[i][j]: #'left'
					res += grid[i][j] - grid[i][j - 1]
				if grid[i][j + 1] < grid[i][j]: #'right'
					res += grid[i][j] - grid[i][j + 1]
	return res






def surfaceArea(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	n = len(grid)
	res = 0
	for r in range(n):
		for c in range(n):
			if grid[r][c]:
				res += 2 # top + bottom
			for neighbor_r, neighbor_c in [(r - 1, c), [r + 1, c], [r, c - 1], [r, c + 1]]: #up, down, left, right
				if 0 <= neighbor_r < n and 0 <= neighbor_c < n:
					val = grid[neighbor_r][neighbor_c]
				else:
					val = 0
				res += max(grid[r][c] - val, 0)
	return res


assert surfaceArea([]) == 0
assert surfaceArea([[2]]) == 10
assert surfaceArea([[1,2],[3,4]]) == 34
assert surfaceArea([[1,0],[0,2]]) == 16
assert surfaceArea([[1,1,1],[1,0,1],[1,1,1]]) == 32
assert surfaceArea([[2,2,2],[2,1,2],[2,2,2]]) == 46













