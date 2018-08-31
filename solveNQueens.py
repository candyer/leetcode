# https://leetcode.com/problems/n-queens/description/


# 51. N-Queens

# The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' 
# both indicate a queen and an empty space respectively.

# Example:

# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.



def dfs(n, queens=[], diagonal1=[], diagonal2=[], res=[]):
	i = len(queens)
	if n == i:
		res.append(queens)
		return [[]]
	for j in range(n):
		print i, j
		if j in queens or i - j in diagonal1 or i + j in diagonal2:
			continue
		dfs(n, queens+[j], diagonal1+[i - j], diagonal2+[i +j], res)
	return res


def solveNQueens(n):
	"""
	:type n: int
	:rtype: List[List[str]]
	"""
	queens = dfs(n, queens=[], diagonal1=[], diagonal2=[], res=[])
	res = []
	for queen in queens:
		tmp = []
		for q in  queen:
			tmp.append(''.join(['.'] * q + ['Q'] + ['.'] * (n - q - 1)))
		res.append(tmp)
	return res

assert solveNQueens(0) == [[]]
assert solveNQueens(1) == [['Q']]
assert solveNQueens(2) == []
assert solveNQueens(4) == [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]





