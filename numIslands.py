# https://leetcode.com/problems/number-of-islands/description/


# 200. Number of Islands


# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


from collections import deque
def numIslands(grid):
	"""
	:type grid: List[List[str]]
	:rtype: int
	"""
	# if not grid: return 0
	res = 0
	lands = set()
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == '1':
				lands.add((r, c))

	while lands:
		res += 1
		stack = deque([lands.pop()])
		while stack:
			r, c = stack.popleft()
			for pos in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
				if pos in lands:
					stack.append(pos)
					lands.remove(pos)
	return res
			

assert numIslands([
	['0', '1', '0', '1', '0'],
	['1', '0', '0', '1', '0'],
	['0', '1', '0', '1', '1'],
	['1', '1', '0', '0', '1']]) == 4
assert numIslands([
	['0', '1', '0', '0', '0'],
	['0', '1', '0', '1', '0'],
	['0', '1', '1', '1', '0'],
	['0', '0', '0', '0', '0']]) == 1
assert numIslands([]) == 0





