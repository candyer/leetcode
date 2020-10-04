# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3483/

# Remove Covered Intervals

# Given a list of intervals, remove all intervals that are covered by another interval in the list.
# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
# After doing so, return the number of remaining intervals.


# Example 1:
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

# Example 2:
# Input: intervals = [[1,4],[2,3]]
# Output: 1

# Example 3:
# Input: intervals = [[0,10],[5,12]]
# Output: 2

# Example 4:
# Input: intervals = [[3,10],[4,10],[5,11]]
# Output: 2

# Example 5:
# Input: intervals = [[1,2],[1,4],[3,4]]
# Output: 1
 

# Constraints:
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# All the intervals are unique.


from typing import List
def removeCoveredIntervals(intervals: List[List[int]]) -> int:
	res, left, right = 0, -1, -1
	for a, b in sorted(intervals):
		if a > left and b > right:
			left = a
			res += 1
		right = max(right, b)
	return res

assert(removeCoveredIntervals([[1,4],[3,6],[2,8]]) == 2)
assert(removeCoveredIntervals([[1,4],[2,3]]) == 1)
assert(removeCoveredIntervals([[0,10],[5,12]]) == 2)
assert(removeCoveredIntervals([[3,10],[4,10],[5,11]]) == 2)
assert(removeCoveredIntervals([[1,2],[1,4],[3,4]]) == 1)
assert(removeCoveredIntervals([[1,8],[4,9],[4,10]]) == 2)












