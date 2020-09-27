# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3474/


# Evaluate Division

# You are given equations in the format A / B = k, where A and B are variables represented as strings, 
# and k is a real number (floating-point number). Given some queries, return the answers. If the answer 
# does not exist, return -1.0.

# The input is always valid. You may assume that evaluating the queries will result in no division by zero 
# and there is no contradiction.

# Example 1:
# Input: 
# equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

# Example 2:
# Input: 
# equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]

# Example 3:
# Input: 
# equations = [["a","b"]], values = [0.5], 
# queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
 

# Constraints:
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= equations[i][0], equations[i][1] <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= queries[i][0], queries[i][1] <= 5
# equations[i][0], equations[i][1], queries[i][0], queries[i][1] consist of lower case English letters and digits.

from typing import List
from collections import defaultdict
def dfs(a, b, visited, graph):
	if a == b:
		return 1.0
	visited.add(a)
	for g in graph[a]:
		if g in visited:
			continue
		visited.add(g)
		d = dfs(g, b, visited, graph)
		if d > 0:
			return d * graph[a][g]  #a/b == g/b * a/g
	return -1.0

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
	graph = defaultdict(dict)
	for (a, b), value in zip(equations, values):
		graph[a][b] = value
		graph[b][a] = 1.0 / value
	res = []
	for a, b in queries:
		if a in graph and b in graph:
			res.append(dfs(a, b, set(), graph))
		else:
			res.append(-1)
	return res


print(calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
print(calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
print(calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))




















