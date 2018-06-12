# https://leetcode.com/problems/maximize-distance-to-closest-person/description/

# 849. Maximize Distance to Closest Person

# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
# Return that maximum distance to closest person.

# Example 1:
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.

# Example 2:
# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.

# Note:
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.


def maxDistToClosest(seats):
	"""
	:type seats: List[int]
	:rtype: int
	"""
	n = len(seats)
	res = begin = end = 0
	if 1 in seats:
		begin = seats.index(1)
		end = seats[::-1].index(1)
		res = max(begin, end)
	else:
		return n
	end = n - end

	tmp = 0
	for i in range(begin, end):
		if seats[i] == 0:
			tmp += 1
		else:
			res = max(res, ((tmp + 1) / 2))
			tmp = 0
	return res

		
assert maxDistToClosest([1,0,0,0,1,0,1]) == 2
assert maxDistToClosest([1,0]) == 1
assert maxDistToClosest([1,0,1,1,1]) == 1
assert maxDistToClosest([0,0,0,0,1]) == 4
assert maxDistToClosest([0,0,0,0,0]) == 5
assert maxDistToClosest([0,0,1,0,0,0]) == 3
assert maxDistToClosest([1,1,1,1,0]) == 1
assert maxDistToClosest([1,0,0,0]) == 3



