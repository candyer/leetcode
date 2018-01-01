# https://leetcode.com/problems/guess-number-higher-or-lower/#/description

def guessNumber(n):
	"""
	:type n: int
	:rtype: int
	function guess(n) is provided by leetcode 
	"""
	left, right = 1, n
	while left <= right:
		mid = (left + right) >> 1
		tmp = guess(mid)
		if tmp == 1:
			left = mid + 1
		elif tmp == -1:
			right = mid - 1
		else:
			return mid

