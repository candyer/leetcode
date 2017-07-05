# https://leetcode.com/problems/perfect-number/#/description



# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

# Example:   Input: 28     Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)


#tip https://en.wikipedia.org/wiki/Perfect_number

def checkPerfectNumber(num):
	"""
	:type num: int
	:rtype: bool
	"""
	if num in [6, 28, 496, 8128, 33550336]:
		return True
	return False
