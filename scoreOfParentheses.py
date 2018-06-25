# https://leetcode.com/problems/score-of-parentheses/description/

# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 
# Example 1:
# Input: "()"
# Output: 1

# Example 2:
# Input: "(())"
# Output: 2

# Example 3:
# Input: "()()"
# Output: 2

# Example 4:
# Input: "(()(()))"
# Output: 6
 
# Note:
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50



def scoreOfParentheses(S):
	"""
	:type S: str
	:rtype: int
	"""

	stack = []
	for c in S:
		if c == '(':
			stack.append(c)
		else:
			pre = stack.pop()
			if pre == '(':
				stack.append(1)
			else:
				while stack[-1] != '(':
					pre += stack.pop()
				stack.pop()
				stack.append(pre * 2)
	return sum(stack)




assert scoreOfParentheses("()") == 1
assert scoreOfParentheses("(())") == 2
assert scoreOfParentheses("()()") == 2
assert scoreOfParentheses("(()(()))") == 6
assert scoreOfParentheses("(()(()))()()()()") == 10
assert scoreOfParentheses("((()(()))(()))") == 16







