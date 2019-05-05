# https://leetcode.com/problems/valid-boomerang/description/


# 1037. Valid Boomerang

# A boomerang is a set of 3 points that are all distinct and not in a straight line.

# Given a list of three points in the plane, return whether these points are a boomerang.

# Example 1:
# Input: [[1,1],[2,3],[3,2]]
# Output: true

# Example 2:
# Input: [[1,1],[2,2],[3,3]]
# Output: false
 

# Note:
# points.length == 3
# points[i].length == 2
# 0 <= points[i][j] <= 100

def isBoomerang(points):
	"""
	:type points: List[List[int]]
	:rtype: bool
	"""
	if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
		return False
	differ = set()
	xs = set()
	ys = set()
	for x, y in points:
		differ.add(x - y)
		xs.add(x)
		ys.add(y)
	return len(differ) > 1 and len(xs) > 1 and len(ys) > 1

print isBoomerang([[1,1],[2,3],[3,2]])
print isBoomerang([[1,1],[1,1],[3,2]])
print isBoomerang([[1,1],[2,2],[3,3]])
print isBoomerang([[1,5],[2,6],[3,7]])
print isBoomerang([[0,1],[1,1],[2,1]])
print isBoomerang([[2,1],[2,9],[2,12]])

