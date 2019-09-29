# https://leetcode.com/problems/spiral-matrix-ii/description/

# 59. Spiral Matrix II

# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

def generateMatrix(n):
	"""
	:type n: int
	:rtype: List[List[int]]
	"""
	grid = [[0 for i in range(n)] for j in range(n)]
	d = {'right':[0, 1], 'down':[1, 0], 'left':[0, -1], 'up':[-1, 0]}
	nextd = {'right':'down', 'down':'left', 'left':'up', 'up':'right'}

	direction = 'right'
	num = 1
	x, y = 0, 0
	while num <= n ** 2:
		if x < n and y < n and grid[x][y] == 0:
			grid[x][y] = num
			num += 1
			x += d[direction][0]
			y += d[direction][1]
		else:
			x -= d[direction][0]
			y -= d[direction][1]			
			direction = nextd[direction]
			x += d[direction][0]
			y += d[direction][1]
	return grid  

assert generateMatrix(1) == [[1]]
assert generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

