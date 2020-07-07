# https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3383/

# Island Perimeter

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
# and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.

 

# Example:
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:

# Time complexity: O(rows*cols)
# space complexity: O(1)
#################################################
from typing import List
def islandPerimeter(grid: List[List[int]]) -> int:
	rows = len(grid)
	cols = len(grid[0]) if rows else 0
	res = 0
	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == 1:
				res += 4
				if row > 0 and grid[row - 1][col]:
					res -= 2
				if col > 0 and grid[row][col - 1]:
					res -= 2
	return res


#################################################
from typing import List
def islandPerimeter(grid: List[List[int]]) -> int:
	rows = len(grid)
	cols = len(grid[0]) if rows else 0
	res = 0
	for row in range(rows):
		for col in range(cols):
			if grid[row][col] == 1:
				if row == 0 or grid[row - 1][col] == 0:
					res += 1
				if col == 0 or grid[row][col - 1] == 0:
					res += 1	
				if row == rows - 1 or grid[row + 1][col] == 0:
					res += 1
				if col == cols - 1 or grid[row][col + 1] == 0:
					res += 1
	return res					


assert(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16)


