# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/563/week-5-october-29th-october-31st/3512/

# Maximize Distance to Closest Person

# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, 
# and seats[i] = 0 represents that the ith seat is empty (0-indexed).

# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
# Return that maximum distance to the closest person.


# Example 1:
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.

# Example 2:
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.

# Example 3:
# Input: seats = [0,1]
# Output: 1
 

# Constraints:
# 2 <= seats.length <= 2 * 10^4
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.

from typing import List
def maxDistToClosest(seats: List[int]) -> int:
	seats.append(1)
	n, count = len(seats), 0
	res = seats.index(1)
	for i in range(res + 1, n):
		if seats[i] == 0:
			count += 1
		else:
			if i + 1 < n:
				res = max(res, (count + 1) // 2)
			else:
				res = max(res, count)
			count = 0
	return res

assert(maxDistToClosest([1,0,0,0,1,0,1]) == 2)
assert(maxDistToClosest([1,0,0,0]) == 3)
assert(maxDistToClosest([0,1]) == 1)
assert(maxDistToClosest([0,0,0,1,0,0,0,1,0,1]) == 3)
assert(maxDistToClosest([0,0,0,1,0,0,0,1,0,1,0,0,0,0]) == 4)
assert(maxDistToClosest([0,1,0,0,0,1,0,1,0,0,0,0,1]) == 2)







