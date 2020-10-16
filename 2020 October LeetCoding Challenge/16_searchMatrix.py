# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3497/


# Search a 2D Matrix

# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
# Output: false

# Example 3:
# Input: matrix = [], target = 0
# Output: false
 

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 0 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4

from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
	if not matrix:
		return False
	elif not matrix[0]:
		return False
	rows = len(matrix)
	cols = len(matrix[0])

	for r in range(rows):
		if target in [matrix[r][0], matrix[r][-1]]:
			return True
		elif matrix[r][0] < target < matrix[r][-1]:
			for c in range(cols):
				if matrix[r][c] < target:
					continue
				elif matrix[r][c] == target:
					return True
				else:
					return False
	return False



from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
	if len(matrix) > 0:
		rows = len(matrix)
		cols = len(matrix[0])

		left, right = 0, rows * cols - 1
		while left <= right:
			mid = (left + right) // 2
			if matrix[mid // cols][mid % cols] == target:
				return True
			elif matrix[mid // cols][mid % cols] > target:
				right = mid - 1
			elif matrix[mid // cols][mid % cols] < target:
				left = mid + 1
		else:
			return False
	else:
		return False



assert(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3) == True)
assert(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13) == False)
assert(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30) == True)
assert(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 100) == False)
assert(searchMatrix([], 0) == False)
assert(searchMatrix([[]], 1) == False)


