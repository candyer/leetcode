# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/description/

# 1253. Reconstruct a 2-Row Binary Matrix

# Given the following details of a matrix with n columns and 2 rows :

# The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
# Your task is to reconstruct the matrix with upper, lower and colsum.

# Return it as a 2-D integer array.
# If there are more than one valid solution, any of them will be accepted.
# If no valid solution exists, return an empty 2-D array.


# Example 1:
# Input: upper = 2, lower = 1, colsum = [1,1,1]
# Output: [[1,1,0],[0,0,1]]
# Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.

# Example 2:
# Input: upper = 2, lower = 3, colsum = [2,2,1,1]
# Output: []

# Example 3:
# Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
 

# Constraints:
# 1 <= colsum.length <= 10^5
# 0 <= upper, lower <= colsum.length
# 0 <= colsum[i] <= 2


from typing import List
def reconstructMatrix(upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
	"""
	:type upper: int
	:type lower: int
	:type colsum: List[int]
	:rtype: List[List[int]]
	"""
	n = len(colsum)
	count_of_2 = colsum.count(2)
	if count_of_2 > upper:
		return []
	count_of_1 = upper - count_of_2
	row0 = []
	for i in range(n):
		if colsum[i] == 2:
			row0.append(1)
			colsum[i] -= 1
			upper -= 1
		elif colsum[i] == 1 and count_of_1 > 0:
			row0.append(1)
			colsum[i] -= 1
			count_of_1 -= 1
			upper -= 1
		else:
			row0.append(0)
	if sum(colsum) != lower:
		return []
	return [row0, colsum]


assert(reconstructMatrix(2, 1, [1,1,1]) == [[1, 1, 0], [0, 0, 1]])
assert(reconstructMatrix(2, 3, [2,2,1,1]) == [])
assert(reconstructMatrix(5, 5, [2,1,2,0,1,0,1,2,0,1]) == [[1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]])
assert(reconstructMatrix(1, 3, [1, 2, 1, 0]) == [[0, 1, 0, 0], [1, 1, 1, 0]])
assert(reconstructMatrix(1, 4, [2,1,2,0,0,2]) == [])










