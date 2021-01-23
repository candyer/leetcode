# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3614//


# Sort the Matrix Diagonally

# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going 
# in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], 
# where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

# Example 1:
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100


from collections import defaultdict
from typing import List
def diagonalSort(mat: List[List[int]]) -> List[List[int]]:
    rows = len(mat)
    cols = len(mat[0])
    d = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            d[r - c].append(mat[r][c])
    for k, v in d.items():
        d[k] = sorted(v)
    for r in range(rows):
        for c in range(cols):
            mat[r][c] = d[r - c][min(r, c)]
    return mat

assert(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]) == [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]])



