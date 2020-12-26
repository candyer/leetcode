# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3580/


# Diagonal Traverse

# Given a matrix of M x N elements (M rows, N columns), 
# return all elements of the matrix in diagonal order as shown in the below image.

# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]

# Note:
# The total number of elements of the given matrix will not exceed 10,000.


from typing import List
from collections import defaultdict
def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    d = defaultdict(list)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            d[r + c].append(matrix[r][c])

    res = []
    for key, vals in d.items():
        if key % 2:
            res.extend(vals)
        else:
            res.extend(vals[::-1])
    return res

assert(findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9])
