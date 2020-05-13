# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/

# Remove K Digits

# Given a non-negative integer num represented as a string, 
# remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. 
# Note that the output must not contain leading zeroes.

# Example 3:
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


def removeKdigits(num: str, k: int) -> str:
	stack = []
	for n in num:
		while stack and stack[-1] > n and k:
			stack.pop()
			k -= 1
		stack.append(n)
	return ''.join(stack[:len(stack) - k]).lstrip('0') or '0'


assert(removeKdigits("1432219", 3) == '1219')
assert(removeKdigits("10200", 1) == '200')
assert(removeKdigits("10", 2) == '0')
assert(removeKdigits("100", 2) == '0')
assert(removeKdigits("111", 2)== '1')

