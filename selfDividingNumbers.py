# https://leetcode.com/problems/self-dividing-numbers/description/

# 728. Self Dividing Numbers
# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, 
# and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self 
# dividing number, including the bounds if possible.

# Example 1:
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# Note:

# The boundaries of each input argument are 1 <= left <= right <= 10000.

def is_self_deviding(n):
	num = n
	while num:
		digit = num % 10
		if digit == 0:
			return False
		if n % digit != 0:
			return False
		num /= 10
	return True

def selfDividingNumbers(left, right):
	"""
	:type left: int
	:type right: int
	:rtype: List[int]
	"""
	res = []
	for i in range(left, right + 1):
		if is_self_deviding(i):
			res.append(i)
	return res 
	

assert selfDividingNumbers(100, 130) == [111, 112, 115, 122, 124, 126, 128]

