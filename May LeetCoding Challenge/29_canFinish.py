# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3344/

# Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
# which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. 
# 			 So it is possible.
# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# 			 To take course 1 you should have finished course 0, and to take course 0 you should
# 			 also have finished course 1. So it is impossible.
 

# Constraints:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
# Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5

from typing import List
from collections import defaultdict
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
	graph = defaultdict(set)
	neighbors = defaultdict(set)
	for course, pre in prerequisites:
		graph[course].add(pre)
		neighbors[pre].add(course)

	nodes_without_cycle = 0
	stack = [course for course in range(numCourses) if course not in graph]
	while stack:
		node = stack.pop()
		nodes_without_cycle += 1
		for n in neighbors[node]:
			graph[n].remove(node)
			if not graph[n]:
				stack.append(n)
	return nodes_without_cycle == numCourses


assert(canFinish(2, [[1,0]]) == True)
assert(canFinish(2, [[1,0],[0,1]]) == False)
assert(canFinish(8, [[1,5],[1,6], [5,4], [6,3],[2,7],[3,1]]) == False)






