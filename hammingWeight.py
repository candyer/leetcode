# https://leetcode.com/problems/number-of-1-bits/description/

# 191. Number of 1 Bits

# Write a function that takes an unsigned integer and returns the number of '1' 
# bits it has (also known as the Hamming weight).

# For example, the 32-bit integer '11' has binary representation 
# 00000000000000000000000000001011, so the function should return 3.

def hammingWeight(n):
	"""
	:type n: int
	:rtype: int
	"""
	return bin(n)[2:].count('1')
print hammingWeight(0)