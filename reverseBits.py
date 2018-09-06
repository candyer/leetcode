# https://leetcode.com/problems/reverse-bits/description/

# 190. Reverse Bits

# Reverse bits of a given 32 bits unsigned integer.

# Example:

# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
#              return 964176192 represented in binary as 00111001011110000010100101000000.
# Follow up:
# If this function is called many times, how would you optimize it?



def reverseBits(n):
	'''
	@param n, an integer
	@return an integer
	'''
	return int(bin(n)[2:].zfill(32)[::-1], 2)


assert reverseBits(1) == 2147483648
assert reverseBits(1456789) == 2841405440
assert reverseBits(87654387) == 3489569952
