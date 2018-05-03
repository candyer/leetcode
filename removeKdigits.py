# https://leetcode.com/problems/remove-k-digits/description/

# 402. Remove K Digits


# Given a non-negative integer num represented as a string, remove k digits from the number so that 
# the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be >= k.
# The given num does not contain any leading zero.
# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading 
# zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


def removeKdigits(num, k):
	"""
	:type num: str
	:type k: int
	:rtype: str
	"""
	n = len(num)
	stack = []
	digits = n - k
	
	for i in range(n):
		while stack and stack[- 1] > num[i] and k > 0:
			stack.pop()
			k -= 1
		stack.append(num[i])

	j = 0
	while j < digits and stack[j] == '0':
		j += 1

	if j == digits:
		return '0'
	return ''.join(stack[j:digits])

assert removeKdigits("14327569", 8) == '0'
assert removeKdigits("14327569", 4) == '1256'
assert removeKdigits("1432219", 4) == '119'
assert removeKdigits("421357", 4) == '13'
assert removeKdigits("1432219", 3) == '1219'
assert removeKdigits("10200", 1) == '200'
assert removeKdigits("10", 2) == '0'
assert removeKdigits("10", 1) == '0'














