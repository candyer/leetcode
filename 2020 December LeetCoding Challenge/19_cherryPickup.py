# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3571/


# Cherry Pickup II


# Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of 
# cherries that you can collect.

# You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , 
# and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

# Return the maximum number of cherries collection using both robots  by following the rules below:

# From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
# When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
# When both robots stay on the same cell, only one of them takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in the grid.
 
# Example 1:
# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.

# Example 2:
# Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.

# Example 3:
# Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
# Output: 22
# Example 4:

# Input: grid = [[1,1],[1,1]]
# Output: 4
 

# Constraints:
# rows == grid.length
# cols == grid[i].length
# 2 <= rows, cols <= 70
# 0 <= grid[i][j] <= 100 

from typing import List
from collections import defaultdict
def cherryPickup(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    poses = {(0, cols - 1): grid[0][0] + grid[0][-1]}
    for row in range(1, rows):
        poses1 = defaultdict(int)
        for (col1, col2), val in poses.items():
            robot1 = [c1 for c1 in [col1 - 1, col1, col1 + 1] if 0 <= c1 < cols]
            robot2 = [c2 for c2 in [col2 - 1, col2, col2 + 1] if 0 <= c2 < cols]
            for c1 in robot1:
                for c2 in robot2:
                    if c1 < c2:
                        tmp = val + grid[row][c1] + grid[row][c2]
                        poses1[(c1, c2)] = max(poses1[(c1, c2)], tmp)
        poses = poses1
    return max(poses.values())


assert(cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]) == 24)
assert(cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]) == 28)
assert(cherryPickup([[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]) == 22)
assert(cherryPickup([[1,1],[1,1]]) == 4)























