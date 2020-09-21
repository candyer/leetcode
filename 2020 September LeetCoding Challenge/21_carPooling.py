# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3467/


# Car Pooling

# You are driving a vehicle that has capacity empty seats initially available for passengers.  
# The vehicle only drives east (ie. it cannot turn around and drive west.)

# Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about 
# the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and 
# drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

# Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 


# Example 1:
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false

# Example 2:
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true

# Example 3:
# Input: trips = [[2,1,5],[3,5,7]], capacity = 3
# Output: true

# Example 4:
# Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
# Output: true


# Constraints:
# trips.length <= 1000
# trips[i].length == 3
# 1 <= trips[i][0] <= 100
# 0 <= trips[i][1] < trips[i][2] <= 1000
# 1 <= capacity <= 100000

#####################################################################
from typing import List
def carPooling(trips: List[List[int]], capacity: int) -> bool:
	if not trips:
		return True
	trips.sort(key=lambda x:x[1])
	passengers = [0] * 1001
	for num, start, end in trips:
		for i in range(start, end):
			if passengers[i] > capacity - num:
				return False
			passengers[i] += num
	return True


#####################################################################
from typing import List
def carPooling(trips: List[List[int]], capacity: int) -> bool:
	change = []
	for num, start, end in trips:
		change.append([start, num])
		change.append([end, -num])
	change.sort()
	passengers = 0
	for stop, num in change:
		passengers += num
		if passengers > capacity:
			return False
	return True

assert(carPooling([[2,1,5],[3,3,7]], 4) == False)
assert(carPooling([[2,1,5],[3,3,7]], 5) == True)
assert(carPooling([[2,1,5],[3,5,7]], 3) == True)
assert(carPooling([[3,2,7],[3,7,9],[8,3,9]], 11) == True)
assert(carPooling([[9,3,4],[9,1,7],[4,2,4],[7,4,5]], 23) == True)





