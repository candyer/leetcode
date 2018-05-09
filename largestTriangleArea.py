
# https://leetcode.com/problems/largest-triangle-area/description/

# 812. Largest Triangle Area


# You have a list of points in the plane. Return the area of the largest triangle that 
# can be formed by any 3 of the points.

# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: 
# The five points are show in the figure below. The red triangle is the largest.


# Notes:

# 3 <= points.length <= 50.
# No points will be duplicated.
# -50 <= points[i][j] <= 50.
# Answers within 10^-6 of the true value will be accepted as correct.

# https://en.wikipedia.org/wiki/Shoelace_formula


def ShoelaceFormula(a, b, c):
	return abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1] - a[1]*b[0]-b[1]*c[0]-c[1]*a[0]) / 2.0

from itertools import combinations as c
def largestTriangleArea(points):
	"""
	:type points: List[List[int]]
	:rtype: float
	"""
	area = 0
	for x, y, z in c(points, 3):
		area = max(area, ShoelaceFormula(x, y, z))
	return area

assert largestTriangleArea([[2,5],[7,7],[10,8],[10,10],[1,1]]) == 14.5
assert largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]) == 2.0
assert largestTriangleArea([[0,2],[9, 0],[5,7]]) == 27.5

