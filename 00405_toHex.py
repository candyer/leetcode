# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

# 405. Convert a Number to Hexadecimal

# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, 
# two’s complement method is used.

# Note:
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, 
# it is represented by a single zero character '0'; otherwise, 
# the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.

# Example 1:
# Input:
# 26
# Output:
# "1a"

# Example 2:
# Input:
# -1
# Output:
# "ffffffff"


def toHex(num: int) -> str:	
	if num == 0:
		return '0'
	if num < 0:
		num += pow(2, 32)

	d = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
	res = []
	while num:
		digit = num % 16
		if digit < 10:
			res.append(str(digit))
		else:
			res.append(d[digit])
		num //= 16
	return ''.join(res[::-1])
		

assert(toHex(26) == '1a')
assert(toHex(-1) == 'ffffffff')
assert(toHex(0) == '0')


