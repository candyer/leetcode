# https://leetcode.com/contest/leetcode-weekly-contest-38/problems/course-schedule-iii/

# There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and 
# closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. 
# You will start at the 1st day.

# Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be 
# taken.

# Example:  Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]   Output: 3
# Explanation: 
# There're totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
# Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
# The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
# Note:
# The integer 1 <= d, t, n <= 10,000.
# You can't take two courses simultaneously.


import heapq
def scheduleCourse(courses):
	courses = sorted(courses, key = lambda (t, d): d)
	h = []
	start = 0
	for t, end in courses:
		start += t
		heapq.heappush(h, -t)
		while start > end:
			start += heapq.heappop(h)
	return len(h)


print scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) #3
print scheduleCourse([[10, 20], [40, 100], [120, 250], [200, 500]]) #4
print scheduleCourse([[200, 250], [50, 300], [120, 450], [200, 260]]) #3
