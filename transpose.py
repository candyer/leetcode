# https://leetcode.com/problems/transpose-matrix/description/


# 867. Transpose Matrix

# Given a matrix A, return the transpose of A.

# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices 
# of the matrix.

# Example 1:
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]

# Example 2:
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
 

# Note:
# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000


def transpose(A):
	"""
	:type A: List[List[int]]
	:rtype: List[List[int]]
	"""
	rows = len(A)
	cols = len(A[0])
	res = [[[]for j in range(rows)] for i in range(cols)]
	for row in range(rows):
		for col in range(cols):
			res[col][row] = A[row][col]
	return res


assert transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]
assert transpose([[1,2,3],[4,5,6]]) == [[1, 4], [2, 5], [3, 6]]
assert transpose([[1,2,3]]) == [[1], [2], [3]]
assert transpose([[1]]) == [[1]]
