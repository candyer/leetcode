# https://leetcode.com/problems/maximal-square/#/description
# leetcode 221 -- Maximal Square

# Given a 2D binary matrix filled with 0s and 1s, 
# find the largest square containing all 1s and return its area.

# For example, given the following matrix:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.


#solution 1
def valid_sqr(matrix,coor):
    for h,w in coor:
        if matrix[h][w] == "0":
            return False
    return True

def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if matrix == []:
        return 0
    num_row = len(matrix)
    num_col = len(matrix[0])
    count = [0]
    for size in range(1,min(num_row,num_col)+1):
        for row in range(num_row):
            for col in range(num_col):
                coor = [(height+row,width+col)for height in range(size) for width in range(size) 
                        if width+col<=num_col-1 if height+row <=num_row-1]  
                if len(coor) == size**2:
                    for sub in coor:
                        if valid_sqr(matrix, coor) == True:
                            count.append(len(coor))
    return max(count)



#Solution 2  O(n^2) running time
def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if matrix == []:
        return 0
    col, row = len(matrix), len(matrix[0])
    dp = [[0] * row for x in range(col)]
    res = 0
    for i in range(col):
        for j in range(row):
            dp[i][j] = int(matrix[i][j])
            if i and j and dp[i][j]:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
            res = max(res, dp[i][j])
    return res * res

# print maximalSquare([['1','0','1','0','0'],
#                      ['1','0','1','1','1'],
#                      ['1','1','1','1','1'],
#                      ['1','0','1','1','1']]) #9
# print maximalSquare([['1','0','1','0','0'],
#                      ['1','0','1','1','1'],
#                      ['1','1','1','1','1'],
#                      ['1','0','1','0','1']]) #4
# print maximalSquare([]) #0
# print maximalSquare([['1','0','1','0','1'],
#                      ['1','0','1','1','1']]) #1
# print maximalSquare([['1','0','1','0','0']]) #0
# print maximalSquare([['0','0'],['1','1']]) #1

import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        self.matrix1 = [['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','1','0','1']]
        self.matrix2 = [[]]
        self.matrix3 = [['0','1'],['1','0']]
        self.matrix4 = [['1','0','1','0'],['1','0','1','1']]
        self.matrix5 = [['1','1','1','1','1'],['1','1','1','1','1'],['1','1','1','1','1'],['1','1','1','1','1']]

    def test_matrix(self):
        self.assertEqual(maximalSquare(self.matrix1), 4)
        self.assertEqual(maximalSquare(self.matrix2), 0)
        self.assertEqual(maximalSquare(self.matrix3), 1)
        self.assertEqual(maximalSquare(self.matrix4), 1)
        self.assertEqual(maximalSquare(self.matrix5), 16)

if __name__ == '__main__':
    unittest.main()
