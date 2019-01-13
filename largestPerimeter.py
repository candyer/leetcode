# https://leetcode.com/problems/largest-perimeter-triangle/description/

# 976. Largest Perimeter Triangle


# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
# If it is impossible to form any triangle of non-zero area, return 0.


# Example 1:
# Input: [2,1,2]
# Output: 5

# Example 2:
# Input: [1,2,1]
# Output: 0

# Example 3:
# Input: [3,2,3,4]
# Output: 10

# Example 4:
# Input: [3,6,2,3]
# Output: 8
 
# Note:
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6


def largestPerimeter(A):
	"""
	:type A: List[int]
	:rtype: int
	as a triangle, sum of each two sides > the other side; difference of each two sides < the other side.
	"""
	n = len(A)
	A.sort(reverse=True)
	a, b, c = 0, 1, 2

	while A[a] - A[b] >= A[c] and c < n - 1:
		a += 1
		b += 1
		c += 1
	if A[a] + A[b] > A[c] and A[a] + A[c] > A[b] and A[b] + A[c] > A[a] and A[a] - A[c] < A[b] and A[b] - A[c] < A[a] and A[c] - A[a] < A[b]:
		return A[a] + A[b] + A[c]
	return 0




def largestPerimeter(A):
	"""
	:type A: List[int]
	:rtype: int
	as a triangle, sum of each two sides > the other side; difference of each two sides < the other side.
	"""
	A.sort(reverse=True)
	for i in range(len(A) - 2):
		if A[i + 2] + A[i + 1] > A[i]:
			return A[i] + A[i + 1] + A[i + 2]
	return 0


assert largestPerimeter([2,1,2]) == 5
assert largestPerimeter([1,2,1]) == 0
assert largestPerimeter([3,2,3,4]) == 10
assert largestPerimeter([3,6,2,3]) == 8
assert largestPerimeter([64,32,16,8,4,2]) == 0
assert largestPerimeter([64,32,16,8,4,5]) == 17





