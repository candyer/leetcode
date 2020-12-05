# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3555/

# Can Place Flowers


# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
# and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.



# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length


# from typing import List
# def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
# 	if 0 not in flowerbed:
# 		return False
# 	i = flowerbed.index(1)
# 	n -= i // 2
# 	count = 0
# 	while i < len(flowerbed):
# 		if flowerbed[i] == 0:
# 			count += 1
# 		else:
# 			n -= (max(0, count - 1)) // 2
# 			count = 0
# 			if n <= 0:
# 				return True
# 		i += 1
# 	if count:
# 		n -= count // 2
# 	return n <= 0



from typing import List
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
	flowerbed = [1, 0] + flowerbed + [0, 1]
	count = 0
	for plot in flowerbed:
		if plot == 0:
			count += 1
		else:
			n -= (max(0, count - 1)) // 2
			if n <= 0:
				return True
			count = 0
	return False


assert(canPlaceFlowers([1,0,0,0,1], 1) == True)
assert(canPlaceFlowers([1,0,0,0,1], 2) == False)
assert(canPlaceFlowers([0,0,0,1,1,0,0], 2) == True)
assert(canPlaceFlowers([1], 2) == False)
assert(canPlaceFlowers([0,0,0,0,1,0,0,1,0,0,1], 3) == False)







