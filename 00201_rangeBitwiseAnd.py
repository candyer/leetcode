# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

# 201. Bitwise AND of Numbers Range

# Given a range [m, n] where 0 <= m <= n <= 2147483647, 
# return the bitwise AND of all numbers in this range, inclusive.

# Example 1:

# Input: [5,7]
# Output: 4
# Example 2:

# Input: [0,1]
# Output: 0


def rangeBitwiseAnd(m: int, n: int) -> int:
	'''
	x & y: Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
	the trick is to find the common part between m and n.	
	'''
	shift = 0
	while m != n:
		m >>= 1
		n >>= 1
		shift += 1
	return n << shift  


assert(rangeBitwiseAnd(5, 7) == 4)
assert(rangeBitwiseAnd(0, 1) == 0)
assert(rangeBitwiseAnd(7, 2999999) == 0)



