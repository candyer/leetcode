# https://leetcode.com/problems/squares-of-a-sorted-array/description/


# 977. Squares of a Sorted Array

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, 
# also in sorted non-decreasing order.

# Example 1:
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

# Example 2:
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 
# Note:
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.



def sortedSquares(A):
	"""
	:type A: List[int]
	:rtype: List[int]
	"""
	for i, num in enumerate(A):
		A[i] = pow(num, 2)
	return sorted(A)


assert sortedSquares([-4,-1,0,3,10]) == [0, 1, 9, 16, 100]
assert sortedSquares([-7,-3,2,3,11]) == [4, 9, 9, 49, 121]






