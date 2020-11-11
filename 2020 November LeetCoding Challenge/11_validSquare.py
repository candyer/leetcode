# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/565/week-2-november-8th-november-14th/3527/

# Valid Square

# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
# The coordinate (x,y) of a point is represented by an integer array with two integers.

# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
 

# Note:
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.



from typing import List
from collections import Counter

def dist(p1: List[int], p2: List[int]) -> int:
	return pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)

def validSquare(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
	points = [p1, p2, p3, p4]
	distance = Counter()
	for i in range(4):
		for j in range(i + 1, 4):
			distance[dist(points[i], points[j])] += 1
	vals = distance.values()
	return 2 in vals and 4 in vals


assert(validSquare([0,0], [1,1], [1,0], [0,1]) == True)
assert(validSquare([0,0], [0,0], [0,1], [0,0]) == False)
assert(validSquare([1,0], [-1,0], [0,1], [0,-1]) == True)




