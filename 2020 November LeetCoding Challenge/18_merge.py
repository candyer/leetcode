# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3535/


# Merge Intervals


# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

 
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4


from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
	intervals.sort()
	n = len(intervals)
	i = 1
	res = [intervals[0]]
	while i < n:
		s1, e1 = res[-1]
		s2, e2 = intervals[i]
		if e1 >= s2:
			res[-1][1] = max(e1, e2)
		else:
			res.append([s2, e2])
		i += 1
	return res


assert(merge([[1,3],[2,6],[8,10],[15,18]]) == [[1, 6], [8, 10], [15, 18]])
assert(merge([[1,4],[4,5]]) == [[1, 5]])
assert(merge([[1,100],[10, 20], [40, 50]]) == [[1, 100]])








