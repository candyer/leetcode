# https://leetcode.com/contest/leetcode-weekly-contest-30/problems/reshape-the-matrix/

# You're given a matrix represented by a two-dimensional array, and two positive integers r and c 
# representing the row number and column number of the wanted reshaped matrix, respectively.

# The reshaped matrix need to be filled with all the elements of the original matrix in the same 
# row-traversing order as they were.

# If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; 
# Otherwise, output the original matrix.

# Note:
# The height and width of the given matrix is in range [1, 100].
# The given r and c are all positive.

def matrixReshape(nums, r, c):
	"""
	:type nums: List[List[int]]
	:type r: int
	:type c: int
	:rtype: List[List[int]]
	"""
	row = len(nums)
	col = len(nums[0])
	if row * col != r * c: 
		return nums
	res = []
	tmp = []
	for i in range(row):
		for j in range(col):
			tmp.append(nums[i][j])
			if len(tmp) == c:
				res.append(tmp)
				tmp = []
	return res


print matrixReshape([[1,2,3,4,5,6], [7,8,9,10,11,12]], 3, 4) #[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print matrixReshape([[1,2],[3,4],[5,6],[7,8],[9,10]], 2, 5) #[[1,2,3,4,5],[6,7,8,9,10]]
print matrixReshape([[1,2],[3,4],[5,6],[7,8]], 2, 4) #[[1,2,3,4],[5,6,7,8]]
print matrixReshape([[1,2],[3,4]], 1, 8) #[[1,2],[3,4]]

