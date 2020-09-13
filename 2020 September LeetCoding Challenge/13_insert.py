# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3458/

# Insert Interval

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.


# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# NOTE: 
# input types have been changed on April 15, 2019. 
# Please reset to default code definition to get new method signature.


from typing import List

# Time complexity: O(nlgn)
# Space complexity:O(n)
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
	intervals.append(newInterval)
	res = []
	for start, end in sorted(intervals):
		if res and res[-1][1] >= start:
			res[-1][1] = max(res[-1][1], end)
		else:
			res.append([start, end])
	return res


# Time complexity: O(n)
# Space complexity:O(n)
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
	left, right = newInterval
	res, i = [], 0
	for i, (start, end) in enumerate(intervals):
		if left > end:
			res.append([start, end])
		elif right < start:
			i -= 1
			break
		else:
			left = min(left, start)
			right = max(right, end)
			
	return res + [[left, right]] + intervals[i + 1:]




assert(insert([], [10, 11]) == [[10, 11]])
assert(insert([[1,3],[6,9]], [2,5]) == [[1, 5], [6, 9]])
assert(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1, 2], [3, 10], [12, 16]])

