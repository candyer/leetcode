# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/


# 926. Flip String to Monotone Increasing


# A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), 
# followed by some number of '1's (also possibly 0.)

# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
# Return the minimum number of flips to make S monotone increasing.

# Example 1:
# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.

# Example 2:
# Input: "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.

# Example 3:
# Input: "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
 
# Note:
# 1 <= S.length <= 20000
# S only consists of '0' and '1' characters.




def minFlipsMonoIncr(S):
	"""
	:type S: str
	:rtype: int
	"""
	zero = one = 0
	for c in S:
		if c == '1':
			one = min(zero, one)
			zero += 1
		else:
			one = min(zero, one) + 1
	return min(zero, one)


assert minFlipsMonoIncr("100100100011111001011001001001") == 12
assert minFlipsMonoIncr("10010010001111100101110") == 7
assert minFlipsMonoIncr("00110") == 1
assert minFlipsMonoIncr("010110") == 2
assert minFlipsMonoIncr("00011000") == 2
assert minFlipsMonoIncr("1111011") == 1
assert minFlipsMonoIncr("1111111") == 0
assert minFlipsMonoIncr("00000000") == 0
assert minFlipsMonoIncr("1010100") == 3


