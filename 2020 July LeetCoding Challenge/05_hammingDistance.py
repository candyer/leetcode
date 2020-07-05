# https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3381/

# Hamming Distance

# The Hamming distance between two integers is the number of positions 
# at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 2^31.

# Example:
# Input: x = 1, y = 4

# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.


def hammingDistance(x: int, y: int) -> int:
	res = 0
	while x or y:
		if x % 2 != y % 2:
			res += 1
		x //= 2
		y //= 2
	return res


def hammingDistance(x: int, y: int) -> int:
	return bin(x ^ y).count('1')

assert(hammingDistance(1, 4) == 2)
assert(hammingDistance(4, 4) == 0)
assert(hammingDistance(7, 100) == 4)



