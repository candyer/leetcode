# https://leetcode.com/problems/koko-eating-bananas/description/

# 875. Koko Eating Bananas

# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  
# The guards have gone and will come back in H hours.

# Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, 
# and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, 
# and won't eat any more bananas during this hour.

# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
# Return the minimum integer K such that she can eat all the bananas within H hours.


# Example 1:
# Input: piles = [3,6,7,11], H = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23

# Note:
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9

def time_needed(piles, k):
	time = 0
	for pile in piles:
		time += (pile - 1) / k + 1 
	return time

def minEatingSpeed(piles, H):
	"""
	:type piles: List[int]
	:type H: int
	:rtype: int
	"""
	lo, hi = 1, max(piles)
	while lo < hi:
		mi = (lo + hi) / 2
		if time_needed(piles, mi) > H:
			lo = mi + 1
		else:
			hi = mi
	return lo

assert minEatingSpeed([3,6,7,11], 8) == 4
assert minEatingSpeed([30,11,23,4,20], 5) == 30
assert minEatingSpeed([30,11,23,4,20], 6) == 23
assert minEatingSpeed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818) == 14






