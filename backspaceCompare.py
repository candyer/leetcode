# https://leetcode.com/problems/backspace-string-compare/description/

# 844. Backspace String Compare

# Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# # means a backspace character.

# Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

# Example 2:
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".

# Example 3:
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".

# Example 4:
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

# Note:
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.

# Follow up:
# Can you solve it in O(N) time and O(1) space?


# def f(s):
# 	n = len(s)
# 	stack = []
# 	for c in s:
# 		if stack and c == "#":
# 			stack.pop()
# 		elif stack == [] and c == '#':
# 			continue
# 		else:
# 			stack.append(c)
# 	return ''.join(stack)


def f(s):
	n = len(s)
	stack = []
	for c in s:
		if c != '#':
			stack.append(c)
		elif stack:
			stack.pop()
	return ''.join(stack)





def backspaceCompare(S, T):
	"""
	:type S: str
	:type T: str
	:rtype: bool
	"""
	return f(S) == f(T)


assert backspaceCompare("ab#c", "ad#c") == True
assert backspaceCompare("ab##", "c#d#") == True
assert backspaceCompare("a##c", "#a#c") == True
assert backspaceCompare("a#c", "b") == False
assert backspaceCompare("y#fo##f", "y#f#o##f") == True
assert backspaceCompare("y#fo##fX", "y#f#o##f") == False





