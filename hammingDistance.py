# https://leetcode.com/problems/hamming-distance/description/
# 461. Hamming Distance

# The Hamming distance between two integers is the number of positions at which the 
# corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:   0 <= x, y < 231.

# Example:   Input: x = 1, y = 4    Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)

# The above arrows point to positions where the corresponding bits are different.

def hammingDistance(x, y):
	"""
	:type x: int
	:type y: int
	:rtype: int
	"""
	a = '{0:032b}'.format(x)
	b = '{0:032b}'.format(y)
	count = 0
	for i in range(32):
		if a[i] != b[i]:
			count += 1
	return count

assert hammingDistance(1, 4) == 2
assert hammingDistance(2**31, 3456789) == 14

