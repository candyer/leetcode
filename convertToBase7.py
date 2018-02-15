# https://leetcode.com/problems/base-7/description/

# 504. Base 7

# Given an integer, return its base 7 string representation.

# Example 1:   Input: 100   Output: "202"
# Example 2:   Input: -7    Output: "-10"

# Note: The input will be in range of [-1e7, 1e7].


def convertToBase7(num):
	"""
	:type num: int
	:rtype: str
	"""
	res = []
	if num == 0: 
		return'0'
	n = abs(num)
	while n:
		tmp = n % 7
		n /= 7
		res.append(str(tmp))
	if num < 0:
		res.append('-')
	return ''.join(res[::-1])

assert convertToBase7(100) == '202'
assert convertToBase7(234) == '453'
assert convertToBase7(-7) == '-10'
assert convertToBase7(-234) == '-453'
assert convertToBase7(0) == '0'



def convertToBaseN(num, base):
	"""
	:type num: int
	:rtype: str
	"""
	res = []
	if num == 0: 
		return'0'
	n = abs(num)
	while n:
		tmp = n % base
		n /= base
		res.append(str(tmp))
	if num < 0:
		res.append('-')
	return ''.join(res[::-1])

print convertToBaseN(14, 13) == '11'
print convertToBaseN(57, 5) == '212'




