# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

# 1232. Check If It Is a Straight Line

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.

 
# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

# Constraints:
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.



def checkStraightLine(coordinates):
	"""
	:type coordinates: List[List[int]]
	:rtype: bool

	slope between A[x1, y1] and B[x2, y2] is (y1 - y2) / (x1 - x2), 
	so for every new point C, check if the slope AC equals to slope AB.
	convert the division into multiplication for better performance.
	"""
	x1, y1 = coordinates[0]
	x2, y2 = coordinates[1]
	return  all((y1 - y2) * ( x1 - x) == (x1 - x2) * ( y1 - y) for x, y in coordinates[2:])


assert checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True
assert checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False
assert checkStraightLine([[1, 6], [2, 5], [4, 3]]) == True
assert checkStraightLine([[1, 6], [2, 5]]) == True


