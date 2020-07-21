# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3397/

# Word Search

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# Example:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
 

# Constraints:
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3


from typing import List
def search(board:List[List[str]], word:str, rows:int, cols:int, r:int, c:int, i:int) -> bool:
	if i == len(word):
		return True
	if r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c]:
		return False
	cur = board[r][c]
	board[r][c] = 0
	res =  search(board, word, rows, cols, r - 1, c, i + 1) \
		or search(board, word, rows, cols, r + 1, c, i + 1) \
		or search(board, word, rows, cols, r, c - 1, i + 1) \
		or search(board, word, rows, cols, r, c + 1, i + 1)
	board[r][c] = cur
	return res

def exist(board: List[List[str]], word: str) -> bool:
	if not board: return False
	rows = len(board)
	cols = len(board[0])
	for r in range(rows):
		for c in range(cols):
			if search(board, word, rows, cols, r, c, 0):
				return True
	return False


assert(exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCF") == True)
assert(exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "SEE") == True)
assert(exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCB") == False)




