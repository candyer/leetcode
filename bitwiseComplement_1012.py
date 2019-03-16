# https://leetcode.com/problems/complement-of-base-10-integer/description/


# 1012. Complement of Base 10 Integer


# Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 
# 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

# The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  
# For example, the complement of "101" in binary is "010" in binary.

# For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.


# Example 1:
# Input: 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

# Example 2:
# Input: 7
# Output: 0
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

# Example 3:
# Input: 10
# Output: 5
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

# Note:
# 0 <= N < 10^9


def bitwiseComplement(N):
	"""
	:type N: int
	:rtype: int
	"""
	res = []
	for c in bin(N)[2:]:
		if c == '1':
			res.append('0')
		else:
			res.append('1')
	return int(''.join(res), 2)

assert bitwiseComplement(5) == 2
assert bitwiseComplement(7) == 0
assert bitwiseComplement(10) == 5
assert bitwiseComplement(0) == 1
assert bitwiseComplement(98765432) == 35452295

