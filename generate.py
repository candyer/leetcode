# Leetcode 118 -- Pascal's Triangle

# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,Return
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows >= 0:
        res = [[1]*i for i in xrange(1,numRows+1)]
        for i in xrange(1, numRows):
            for j in xrange(1,len(res[i])-1):
                res[i][j] = res[i-1][j-1]+ res[i-1][j]
    return res
    
# import unittest
# class MyTest(unittest.TestCase):  
#     def testZero(self):
#         self.assertEqual(generate(0), [])

#     def testOne(self):
#         self.assertEqual(generate(1), [[1]])

#     def testTwo(self):
#         self.assertEqual(generate(2), [[1], [1, 1]])

#     def testThree(self):
#         self.assertEqual(generate(3), [[1], [1, 1], [1, 2, 1]])

#     def testFour(self):
#         self.assertEqual(generate(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

# if __name__ == '__main__':
#     unittest.main()


# Leetcode 119 -- Pascal's Triangle II
# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?

#solution 1
def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    return generate(rowIndex+1)[-1]

#solution 2
def factorial(n):
    res = 1
    while n:
        res *= n
        n -= 1
    return res
def combinations(a,b): # a >= b
    assert a >= b
    return factorial(a) / (factorial(b)* factorial(a-b))

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0: return [1]
    
    res = [1]+[0]*(rowIndex-1)+[1]
    left, right = 1, rowIndex-1
    while left <= right:
        res[left] = res[right] = combinations(rowIndex, left)
        left += 1
        right -= 1
    return res
