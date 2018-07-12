# https://leetcode.com/problems/to-lower-case/description/

# 709. To Lower Case

# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.


# Example 1:
# Input: "Hello"
# Output: "hello"

# Example 2:
# Input: "here"
# Output: "here"

# Example 3:
# Input: "LOVELY"
# Output: "lovely"


def toLowerCase(str):
	"""
	:type str: str
	:rtype: str
	"""
	return str.lower()

assert toLowerCase("Hello") == 'hello'
assert toLowerCase("here") == 'here'
assert toLowerCase("LOVELY") == 'lovely'
assert toLowerCase("") == ''