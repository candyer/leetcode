# Leetcode 73 -- Set Matrix Zeroes

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    # Brute force O(mn) running time, O(m + n) space
    rows, cols = len(matrix), len(matrix[0])
    r,c= [], []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                if row not in r:
                    r.append(row)
                if col not in c:
                    c.append(col)

    for row in range(rows):
        for col in range(cols):
            if row in r or col in c:
                matrix[row][col] = 0
    return matrix

print setZeroes([[2,0,0],[3,0,1],[1,2,8]]) #[[0,0,0],[0,0,0],[1,0,0]]
print setZeroes([[]])
print setZeroes([[2,3,0],[3,0,1],[0,2,8]])


