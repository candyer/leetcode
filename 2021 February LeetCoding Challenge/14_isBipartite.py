# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3639/

# Is Graph Bipartite?


# Given an undirected graph, return true if and only if it is bipartite.
# Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, 
# such that every edge in the graph has one node in A and another node in B.
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between 
# nodes i and j exists. Each node is an integer between 0 and graph.length - 1. There are no self edges 
# or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.


# Example 1:
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.

# Example 2:
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: We cannot find a way to divide the set of nodes into two independent subsets.
 

# Constraints:
# 1 <= graph.length <= 100
# 0 <= graph[i].length < 100
# 0 <= graph[i][j] <= graph.length - 1
# graph[i][j] != i
# All the values of graph[i] are unique.
# The graph is guaranteed to be undirected. 

from typing import List
from collections import deque
def isBipartite(graph: List[List[int]]) -> bool:
    color = {} 
    for i in range(len(graph)):
        if not i in color:
            color[i] = 1
            queue = deque([i])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True

assert(isBipartite([[1,3],[0,2],[1,3],[0,2]]) == True)
assert(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]) == False)
assert(isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]) == False)





