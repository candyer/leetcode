# https://leetcode.com/problems/queens-that-can-attack-the-king/description/

# 1222. Queens That Can Attack the King

# On an 8x8 chessboard, there can be multiple Black Queens and one White King.

# Given an array of integer coordinates queens that represents the positions of the Black Queens, 
# and a pair of coordinates king that represent the position of the White King, 
# return the coordinates of all the queens (in any order) that can attack the King.

# Example 1:
# Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
# Output: [[0,1],[1,0],[3,3]]
# Explanation:  
# The queen at [0,1] can attack the king cause they're in the same row. 
# The queen at [1,0] can attack the king cause they're in the same column. 
# The queen at [3,3] can attack the king cause they're in the same diagnal. 
# The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
# The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
# The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.

# Example 2:
# Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
# Output: [[2,2],[3,4],[4,4]]

# Example 3:
# Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],
# 				 [2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
# Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
 

# Constraints:
# 1 <= queens.length <= 63
# queens[0].length == 2
# 0 <= queens[i][j] < 8
# king.length == 2
# 0 <= king[0], king[1] < 8
# At most one piece is allowed in a cell.

###############################################################
def queensAttacktheKing(queens, king):
	"""
	:type queens: List[List[int]]
	:type king: List[int]
	:rtype: List[List[int]]
	"""
	res = []
	x, y = king
	diff = x - y
	total = x + y
	minix, maxix = -1, float('inf')
	miniy, maxiy = -1, float('inf')
	minid1, maxid1 = -1, float('inf')
	minid2, maxid2 = -1, float('inf')

	for r, c in queens:
		##### check the cloest queen in the same row #####
		if r == x:
			if c < y:
				minix = max(minix, c)
			elif c > y:
				maxix = min(maxix, c)

		##### check the cloest queen in the same column #####
		if c == y:
			if r < x:
				miniy = max(miniy, r)
			elif r > x:
				maxiy = min(maxiy, r)	

		##### check the cloest queen topleft-bottomright diagnally #####
		if r - c == diff:
			if r + c < total:
				minid1 = max(minid1, r)
			elif r + c > total:
				maxid1 = min(maxid1, r)

		##### check the cloest queen topright-bottomleft diagnally #####		
		if r + c == total:
			if r - c < diff:
				minid2 = max(minid2, r)
			elif r + c > diff:
				maxid2 = min(maxid2, r)

	##### queen and king are in the same row #####
	if minix > -1:
		res.append([x, minix])
	if maxix < float('inf'):
		res.append([x, maxix])

	##### queen and king are in the same column #####
	if miniy > -1:
		res.append([miniy, y])
	if maxiy < float('inf'):
		res.append([maxiy, y])
	
	##### queen and king are in the same topleft-bottomright diagnal#####
	if minid1 > -1:
		res.append([minid1, minid1 - diff])
	if maxid1 < float('inf'):
		res.append([maxid1, maxid1 - diff])

	##### queen and king are in the same topright-bottomleft diagnal#####
	if minid2 > -1:
		res.append([minid2, total - minid2])
	if maxid2 < float('inf'):
		res.append([maxid2, total - maxid2])

	return res



# cleaner version 
###############################################################
from collections import defaultdict
def queensAttacktheKing(queens, king):
	"""
	:type queens: List[List[int]]
	:type king: List[int]
	:rtype: List[List[int]]
	"""
	d = defaultdict(list)
	for queen in queens:
		d[queen[0]].append(queen[1])

	res = []
	direction = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
	for r, c in direction:
		x, y = king
		while 0 <= x <=7 and 0 <= y <= 7:
			if x in d and y in d[x]:
				res.append([x, y])
				break
			x += r
			y += c
	return res

print queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0])
print queensAttacktheKing([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3])
print queensAttacktheKing([
	[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],
	[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], 
	king = [3,4])
print queensAttacktheKing([
	[4,7],[1,3],[6,6],[3,0],[0,2],[0,7],[6,2],[3,7],[5,1],[2,5],[0,3],[7,2],[4,0],[1,2],[3,3],[5,5],[4,4],
	[6,3],[1,5],[5,0],[0,4],[6,4],[5,4],[3,2],[0,0],[4,5],[0,5],[2,3],[1,0],[6,5],[5,3],[0,1],[7,0],[4,6],
	[5,7],[7,4],[2,0],[4,3],[3,4]],
	[2,4])

