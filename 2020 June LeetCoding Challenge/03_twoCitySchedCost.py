# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/

# Two City Scheduling

# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A 
# is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

# Example 1:
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

# Note:
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000


from typing import List
def twoCitySchedCost(costs):
	"""
	:type costs: List[List[int]]
	:rtype: int
	"""
	cost = 0
	n = len(costs)
	for i, (a, b) in enumerate(sorted(costs, key=lambda array: array[0] - array[1])):
		if i < n / 2:
			cost += a
		else:
			cost += b
	return cost


assert(twoCitySchedCost([[8, 3], [1, 7], [8, 8], [7, 8], [9, 6], [4, 10]]) == 29)
assert(twoCitySchedCost([[4, 1], [4, 9], [9, 3], [3, 7], [1, 5], [5, 6]]) == 18)
assert(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) == 110)




