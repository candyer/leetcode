# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/

# 1252. Cells with Odd Values in a Matrix

# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices 
# where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri 
# and column ci by 1.

# Return the number of cells with odd values in the matrix after applying the increment to all indices.

 
# Example 1:
# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

# Example 2:
# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
 

# Constraints:
# 1 <= n <= 50
# 1 <= m <= 50
# 1 <= indices.length <= 100
# 0 <= indices[i][0] < n
# 0 <= indices[i][1] < m

#################
## brute force ##
#################
def oddCells(n, m, indices):
	"""
	:type n: int
	:type m: int
	:type indices: List[List[int]]
	:rtype: int
	"""
	grid = [[0 for j in range(m)]for i in range(n)]

	for r, c in indices:
		for i in range(n):
			grid[i][c] += 1
		for j in range(m):
			grid[r][j] += 1

	res = 0
	for i in range(n):
		for j in range(m):
			if grid[i][j] % 2:
				res += 1
	return res


#####################
## better solution ##
#####################
from collections import defaultdict
def oddCells(n, m, indices):
	"""
	:type n: int
	:type m: int
	:type indices: List[List[int]]
	:rtype: int
	"""
	row, col = defaultdict(int), defaultdict(int)
	for r, c in indices:
		row[r] += 1
		col[c] += 1

	num1 = num2 = 0
	for vr in row.values():
		if vr % 2:
			num1 += 1
	for vc in col.values():
		if vc % 2:
			num2 += 1
	return num1 * m + num2 * n - num1 * num2 * 2

assert oddCells(6, 2, [[1, 0], [5, 1]]) == 8
assert oddCells(2, 3, [[0,1],[1,1]]) == 6
assert oddCells(2, 2, [[1,1],[0,0]]) == 0
assert oddCells(10, 1, [[5, 0]]) == 9
assert oddCells(1, 4, [[0, 0], [0, 1], [0, 3], [0, 1]]) == 2

