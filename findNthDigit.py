# https://leetcode.com/problems/nth-digit/description/

# 400. Nth Digit

# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).

# Example 1:   Input:3   Output:3
# Example 2:   Input:11   Output:0

# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, 
# which is part of the number 10.

def findNthDigit(n):
	"""
	:type n: int
	:rtype: int
	"""
	start = 1
	digit = 1
	length = 9
	while n > digit * length:
		n -= digit * length
		start *= 10
		digit += 1
		length *= 10
	num = start + (n - 1) / digit
	idx = (n - 1) % digit
	return int(str(num)[idx])


assert findNthDigit(0) == 0
assert findNthDigit(3) == 3
assert findNthDigit(11) == 0
assert findNthDigit(122) == 6
assert findNthDigit(123) == 6
assert findNthDigit(12234563) == 2
assert findNthDigit(12234561) == 6
assert findNthDigit(1223456783) == 8
assert findNthDigit(2147483647) == 2


