# https://leetcode.com/problems/last-stone-weight/description/

# 1046. Last Stone Weight

# We have a collection of rocks, each rock has a positive integer weight.

# Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  
# The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 
# Example 1:
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 
# Note:
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

from heapq import heapify, heappop, heappush
def lastStoneWeight(stones):
	"""
	:type stones: List[int]
	:rtype: int
	"""
	array = []
	for stone in stones:
		heappush(array, stone * (-1))
	n = len(stones)
	while n >= 2:
		max1 = heappop(array)
		max2 = heappop(array)
		if max1 != max2:
			heappush(array, max1 - max2)
			n -= 1
		else:
			n -= 2
	if n:
		return heappop(array) * (-1)
	return 0


assert lastStoneWeight([2,7,4,1,8,1]) == 1
assert lastStoneWeight([1]) == 1
assert lastStoneWeight([2, 2]) == 0

