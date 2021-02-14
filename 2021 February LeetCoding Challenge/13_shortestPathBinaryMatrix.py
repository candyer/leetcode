# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3638/

# Shortest Path in Binary Matrix


# In an N by N square grid, each cell is either empty (0) or blocked (1).
# A clear path from top-left to bottom-right has length k if and only if it is composed of 
# cells C_1, C_2, ..., C_k such that:
# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.  
# If such a path does not exist, return -1.

 
# Example 1:
# Input: [[0,1],[1,0]]
# Output: 2

# Example 2:
# Input: [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4


# Note:
# 1 <= grid.length == grid[0].length <= 100
# grid[r][c] is 0 or 1

from typing import List
from collections import deque
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    rows = len(grid)
    if grid[0][0] or grid[rows - 1][-1]:
        return -1
    drc = [[-1, -1],[-1, 0],[-1, 1],[0, -1],[0, 1],[1, -1],[1, 0],[1, 1]]
    visited = {(0, 0)}
    queue = deque([(0,0,1)])
    while queue:
        r, c, count = queue.popleft()
        if r == c == rows - 1:
            return count
        for x, y in drc:
            rx = r + x
            cy = c + y
            if (rx, cy) not in visited and 0 <= rx < rows and 0 <= cy < rows and grid[rx][cy] == 0:
                visited.add((rx, cy))
                queue.append((rx, cy, count + 1))
    return -1


assert(shortestPathBinaryMatrix([[0,1],[1,0]]) == 2)
assert(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]) == 4)
assert(shortestPathBinaryMatrix([[0,0,0,0,0],[1,1,1,1,0],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0]]) == 13)

