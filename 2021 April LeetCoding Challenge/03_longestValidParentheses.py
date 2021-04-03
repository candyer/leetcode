# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3695/

# Longest Valid Parentheses


# Given a string containing just the characters '(' and ')', 
# find the length of the longest valid (well-formed) parentheses substring.

 
# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:
# Input: s = ""
# Output: 0
 

# Constraints:
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.

def longestValidParentheses(s: str) -> int:
	stack = [[')', -1]]
	res = 0
	for i, c in enumerate(s):
		if c == ')' and stack[-1][0] == '(':
			stack.pop()
			res = max(res, i - stack[-1][1])
		else:
			stack.append([c, i])
	return res

assert(longestValidParentheses("(()") == 2)
assert(longestValidParentheses(")()())") == 4)
assert(longestValidParentheses("") == 0)
        




