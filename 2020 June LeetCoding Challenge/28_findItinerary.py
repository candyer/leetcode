# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3374/

# Reconstruct Itinerary

# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, 
# the itinerary must begin with JFK.

# Note:
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order 
# when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than 
# ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.

# Example 1:
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

# Example 2:
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.

from collections import defaultdict
def findItinerary(tickets):
	flights = defaultdict(list)
	for departure, arrival in sorted(tickets, reverse=True):
		flights[departure].append(arrival)
	path = []
	def visit(airport):
		while flights[airport]:
			visit(flights[airport].pop())
		path.append(airport)
	visit('JFK')
	return path[::-1]


assert(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'])
assert(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'])
assert(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ['JFK', 'NRT', 'JFK', 'KUL'])

