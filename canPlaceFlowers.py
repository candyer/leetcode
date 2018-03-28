# https://leetcode.com/problems/can-place-flowers/description/

# 605. Can Place Flowers

# Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
# However, flowers cannot be planted in adjacent plots - they would compete for water and both 
# would die.

# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 
# 	means not empty), and a number n, return if n new flowers can be planted in it without 
# violating the no-adjacent-flowers rule.

# Example 1:   Input: flowerbed = [1,0,0,0,1], n = 1   Output: True

# Example 2:   Input: flowerbed = [1,0,0,0,1], n = 2   Output: False

# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.


def canPlaceFlowers(flowerbed, n):
	"""
	:type flowerbed: List[int]
	:type n: int
	:rtype: bool
	"""
	m = len(flowerbed)
	start = end = False
	begin = 0
	if flowerbed[0] == 0:
		start = True
	if flowerbed[-1] == 0:
		end = True

	if 1 in flowerbed:
		begin = flowerbed.index(1)
		if begin != 0:
			start = True
	else:
		if n <= (m + 1) / 2:
			return True
		return False

	n -= begin / 2
	if n <= 0:
		return True
	
	i = begin
	while i < m:
		j = i
		count = 1
		while flowerbed[j] == 0 and j < m - 1:			
			j += 1
			if j == m - 1 and flowerbed[j] == 0 and end:
				n -= (count + 1) / 2
			elif flowerbed[j] == 1:
				n -= (count - 1) / 2
			if n <= 0:
				return True
				break
			count += 1
		i += count 
	return False


print canPlaceFlowers([1,0,0,0,1,0,0], 2) == True
print canPlaceFlowers([1,0,0,0,0,1], 2) == False
print canPlaceFlowers([1,0,0,0,1], 1) == True
print canPlaceFlowers([0,0,1,0,0,0,1,0,0], 4) == False
print canPlaceFlowers([0,0,1,0,0,0,1,0,0], 3) == True
print canPlaceFlowers([0], 1) == True
print canPlaceFlowers([0,0,0,0,0], 3) == True
print canPlaceFlowers([1,0,0,0,1], 2) == False
