
# https://leetcode.com/problems/valid-parenthesis-string/description/


# 678. Valid Parenthesis String

# Given a string containing only three types of characters: '(', ')' and '*', 
# write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.

# Example 1:
# Input: "()"
# Output: True

# Example 2:
# Input: "(*)"
# Output: True

# Example 3:
# Input: "(*))"
# Output: True
# Note:
# The string size will be in the range [1, 100].

def checkValidString(s):
	left = 0
	for c in s:
		if c in '(*':
			left += 1
		else:
			left -= 1
		if left < 0:

			return False
	if left == 0:
		return True

	right = 0
	for c in s[::-1]:
		if c in ')*':
			right += 1
		else:
			right -= 1
		if right < 0:
			return False
	return True

assert(checkValidString("()") == True)
assert(checkValidString("(*)") == True)
assert(checkValidString("(*))") == True)
assert(checkValidString("*()(**))") == True)
assert(checkValidString("(((**))") == True)
assert(checkValidString("**((****") == True)
assert(checkValidString("**))****") == True)
assert(checkValidString("*****(*(") == False)
assert(checkValidString("*))*****") == False)
assert(checkValidString("******") == True)
assert(checkValidString("(*()") == True)
assert(checkValidString("()*)") == True)
assert(checkValidString("*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)") == False)
assert(checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()") == True)

