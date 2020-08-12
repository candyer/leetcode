# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3421/

# Pascal's Triangle II

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:
# Input: 3
# Output: [1,3,3,1]

# Follow up:
# Could you optimize your algorithm to use only O(k) extra space?


from typing import List
from math import factorial as f

def combinations(n, k):
	return f(n) // f(k) // f(n - k)

def getRow( rowIndex: int) -> List[int]:
	'''https://en.wikipedia.org/wiki/Pascal%27s_triangle#Formula'''
	res = [1 for i in range(rowIndex + 1)]
	for i in range(rowIndex + 1):
		res[i] = combinations(rowIndex, i)
	return res


assert(getRow(0) == [1])
assert(getRow(3) == [1, 3, 3, 1])
assert(getRow(11) == [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1])




