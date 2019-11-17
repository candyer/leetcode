# https://leetcode.com/problems/shift-2d-grid/description/

# 1260. Shift 2D Grid


# Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.
# In one shift operation:

# Element at grid[i][j] becomes at grid[i][j + 1].
# Element at grid[i][m - 1] becomes at grid[i + 1][0].
# Element at grid[n - 1][m - 1] becomes at grid[0][0].
# Return the 2D grid after applying shift operation k times.


# Example 1:
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]

# Example 2:
# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

# Example 3:Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]
 

# Constraints:
# 1 <= grid.length <= 50
# 1 <= grid[i].length <= 50
# -1000 <= grid[i][j] <= 1000
# 0 <= k <= 100

#############################################################################
from typing import List
def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
	row = len(grid)
	col = len(grid[0])
	nums = []
	for i in range(row):
		for j in range(col):
			nums.append(grid[i][j])

	res = [[0 for j in range(col)] for i in range(row)]
	m = -k
	for i in range(row):
		for j in range(col):
			res[i][j] = nums[m % (row * col)]
			m += 1
	return res


#############################################################################
from typing import List
def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
	row, col = len(grid), len(grid[0])
	total = row * col
	start = total - k % total
	res = []
	tmp = []
	for i in range(start, start + total + 1):
		j = i % total
		r, c = j // col, j % col
		if (j - start) % col == 0 and tmp:
			res.append(tmp)
			tmp = []
		tmp.append(grid[r][c])
	return res


#############################################################################
from typing import List
def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
	row, col = len(grid), len(grid[0])
	total = row * col
	start = total - k % total
	res = []
	for i in range(start, start + total):
		j = i % total
		r, c = j // col, j % col
		if (j - start) % col == 0:
			res.append([])
		res[-1].append(grid[r][c])
	return res


assert(shiftGrid([[1,2,3],[4,5,6],[7,8,9]],5) == [[5, 6, 7], [8, 9, 1], [2, 3, 4]])   
assert(shiftGrid([[1,2,3],[4,5,6],[7,8,9]],1) == [[9, 1, 2], [3, 4, 5], [6, 7, 8]])
assert(shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]],4) == [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]])
assert(shiftGrid([[1,2,3],[4,5,6],[7,8,9]],9) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])








