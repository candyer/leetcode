# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/


# 1167. Minimum Cost to Connect Sticks

# You have some sticks with positive integer lengths.

# You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  
# You perform this action until there is one stick remaining.

# Return the minimum cost of connecting all the given sticks into one stick in this way.

 
# Example 1:
# Input: sticks = [2,4,3]
# Output: 14

# Example 2:
# Input: sticks = [1,8,3,5]
# Output: 30
 

# Constraints:
# 1 <= sticks.length <= 10^4
# 1 <= sticks[i] <= 10^4

from heapq import heappush, heappop
def connectSticks(sticks):
	"""
	:type sticks: List[int]
	:rtype: int
	"""
	array = []
	for stick in sticks:
		heappush(array, stick)
	res = 0
	n = len(sticks)
	while n > 1:
		a = heappop(array)
		b = heappop(array)
		res += a + b
		heappush(array, a + b)
		n -= 1
	return res


assert connectSticks([2,4,3]) == 14
assert connectSticks([1,8,3,5]) == 30
assert connectSticks([1,2,3,4,5,6]) == 51
