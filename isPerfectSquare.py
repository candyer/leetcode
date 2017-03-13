# https://leetcode.com/problems/valid-perfect-square/#/description

def isPerfectSquare(num):
	"""
	:type num: int
	:rtype: bool
	"""
	# solution 1 Newton's Method
	x = num
	while x * x > num:
		x = (x + num / x) / 2
	return x * x == num


	# solution 2
	# a perfect square number can be represented as 1 + 3 + 5 + 7 + 9 + ...
	count = 1
	while num > 0:
		num -= count
		count += 2
	return num == 0


	# solution 3 binary search
	left, right = 0, num
	while left <= right:
		mid = (left + right) / 2
		if mid * mid >= num:
			right = mid - 1
		else:
			left = mid + 1
	return left * left == num
