# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3650/

# Search a 2D Matrix II


# Write an efficient algorithm that searches for a target value in an m x n integer matrix. 
# The matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
 
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9

from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
	'''start from the bottom left corner'''
	rows = len(matrix)
	cols = len(matrix[0])
	r, c = rows - 1, 0
	while r >= 0 and c < cols:
		if matrix[r][c] == target:
			return True
		elif matrix[r][c] > target:
			r -= 1
		else:
			c += 1
	return False


from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
	'''start from the top right corner'''
	rows = len(matrix)
	cols = len(matrix[0])
	r, c = 0, cols - 1
	while r < rows and c >= 0:
		if matrix[r][c] == target:
			return True
		elif matrix[r][c] < target:
			r += 1
		else:
			c -= 1
	return False


assert(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5) == True)
assert(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20) == False)


