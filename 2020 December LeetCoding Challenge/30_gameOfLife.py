# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3586/


# Game of Life


# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British 
# mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead 
# (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following 
# four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births 
# and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
 

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
 

# Follow up:
# Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first 
# and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems 
# when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?



##################################################################################3
# Time complexity: O(MN)
# Space complexity: O(MN)
from typing import List
def gameOfLife(board: List[List[int]]) -> None:
    rows = len(board)
    cols = len(board[0])
    copy_of_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0
            for i, j in neighbors:
                r, c = row + i, col + j
                if 0 <= r < rows and 0 <= c < cols and copy_of_board[r][c] == 1:
                    live_neighbors += 1
            if copy_of_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[row][col] = 0
            if copy_of_board[row][col] == 0 and live_neighbors == 3:
                board[row][col] = 1



##################################################################################3
# Time complexity: O(MN)
# Space complexity: O(1)
from typing import List
def gameOfLife(board: List[List[int]]) -> None:
    rows = len(board)
    cols = len(board[0])
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0
            for i, j in neighbors:
                r, c = row + i, col + j
                if 0 <= r < rows and 0 <= c < cols and board[r][c] in [1, -1]:
                    live_neighbors += 1
            if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[row][col] = -1
            if board[row][col] == 0 and live_neighbors == 3:
                board[row][col] = 2

    for row in range(rows):
        for col in range(cols):
            if board[row][col] > 0:
                board[row][col] = 1
            else:
                board[row][col] = 0



print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])) #[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
print(gameOfLife([[1,1],[1,0]])) #[[1,1],[1,1]]












