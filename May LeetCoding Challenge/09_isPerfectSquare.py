# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/


# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.


# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 14
# Output: false


def isPerfectSquare(num: int) -> bool:
	'''Sum of odd numbers results in a square number'''
	i = 1
	total = 0
	while total < num:
		total += i
		if total == num:
			return True
		i += 2
	return False


def isPerfectSquare(num: int) -> bool:
	'''binary search'''
	if num <= 1:
		return True
	low, high = 2, num // 2
	print(low, high)
	while low <= high:
		mid = (low + high) // 2
		square = pow(mid, 2)
		if square == num:
			return True
		elif square > num:
			high = mid - 1
		else:
			low = mid + 1
	return False


assert(isPerfectSquare(1) == True)
assert(isPerfectSquare(16) == True)
assert(isPerfectSquare(14) == False)
assert(isPerfectSquare(169) == True)
assert(isPerfectSquare(72) == False)

