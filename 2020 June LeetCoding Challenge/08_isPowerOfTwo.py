# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3354/

# Power of Two

# Given an integer, write a function to determine if it is a power of two.

# Example 1:
# Input: 1
# Output: true 
# Explanation: 20 = 1

# Example 2:
# Input: 16
# Output: true
# Explanation: 24 = 16

# Example 3:
# Input: 218
# Output: false


def isPowerOfTwo(n: int) -> bool:
	return n and not n & (n - 1)

assert(isPowerOfTwo(0) == False)
assert(isPowerOfTwo(1) == True)
assert(isPowerOfTwo(2) == True)
assert(isPowerOfTwo(218) == False)