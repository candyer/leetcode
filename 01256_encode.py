# https://leetcode.com/problems/encode-number/description/

# 1256. Encode Number
# Given a non-negative integer num, Return its encoding string.

# The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:

# 0 - ''
# 1 - '0'
# 2 - '1'
# 3 - '00'
# 4 - '01'
# 5 - '10'
# 6 - '11'
# 7 - '000'

# Example 1:
# Input: num = 23
# Output: "1000"

# Example 2:
# Input: num = 107
# Output: "101100"

# Constraints:
# 0 <= num <= 10^9

###############################################################
from math import log
def encode(num: int) -> str:
	if num == 0: 
		return ''
	return bin(num + 1)[-int(log(num + 1, 2)):]


###############################################################
def encode(num: int) -> str:
	return bin(num + 1)[3:]



assert(encode(0) == '')
assert(encode(1) == '0')
assert(encode(3) == '00')
assert(encode(4) == '01')
assert(encode(7) =='000')
assert(encode(23) == '1000')
assert(encode(107) == '101100')
assert(encode(9999999) == '00110001001011010000000')


