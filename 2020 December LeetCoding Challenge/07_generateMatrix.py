# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557/

# Spiral Matrix II


# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]
 

# Constraints:
# 1 <= n <= 20


from typing import List
def generateMatrix(n: int) -> List[List[int]]:
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


assert(generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
assert(generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])




