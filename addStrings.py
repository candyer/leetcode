# https://leetcode.com/problems/add-strings/description/

# 415. Add Strings

# Given two non-negative integers num1 and num2 represented as string, 
# return the sum of num1 and num2.

# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


def addStrings(num1, num2):
	"""
	:type num1: str
	:type num2: str
	:rtype: str
	"""
	m, n = len(num1), len(num2)
	res = []
	digit = 0
	while m > 0 and n > 0:
		m -= 1
		n -= 1
		digit, remainder = divmod(int(num1[m]) + int(num2[n]) + digit, 10)
		res.append(str(remainder))

	while m > 0:
		digit, remainder = divmod(int(num1[m - 1]) + digit, 10)
		res.append(str(remainder))
		m -= 1

	while n > 0:
		digit, remainder = divmod(int(num2[n - 1]) + digit, 10)
		res.append(str(remainder))
		n -= 1

	if digit > 0:
		res.append(str(digit))

	return ''.join(res[::-1])



assert addStrings('123', '46') == '169'
assert addStrings('111', '1234') == '1345'
assert addStrings('173', '46') == '219'
assert addStrings('993', '96') == '1089'
assert addStrings('993', '99999') == '100992'
assert addStrings('10000', '101') == '10101'
