# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3450/

# Image Overlap

# Two images A and B are given, represented as binary, square matrices of the same size.  
# (A binary matrix has only 0s and 1s as values.)

# We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on 
# top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

# (Note also that a translation does not include any kind of rotation.)

# What is the largest possible overlap?

# Example 1:
# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.

# Notes: 
# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1

from typing import List
from collections import Counter
def largestOverlap(A: List[List[int]], B: List[List[int]]) -> int:
	n = len(A)
	# get the coordinations of all the ones from matrix A and B
	A = [[r, c] for c in range(n) for r in range(n) if A[r][c] == 1]
	B = [[r, c] for c in range(n) for r in range(n) if B[r][c] == 1]

	#for each 1 in matrix A, count how many steps needed to go to each 1 in matrix B, return the max
	count = Counter()
	for ra, ca in A:
		for rb, cb in B:
			count[(ra - rb, ca - cb)] += 1
	if count:
		return max(count.values())
	return 0

assert(largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]) == 3)
assert(largestOverlap([[0,0],[1,0]], [[0,1],[0,0]]) == 1)
assert(largestOverlap([[0,0],[0,0]], [[0,0],[0,0]]) == 0)

