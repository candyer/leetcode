# https://leetcode.com/problems/generate-parentheses/

# 22. Generate Parentheses


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]
 
# Constraints:
# 1 <= n <= 8


from typing import List
def solve(l, r, path, res):
	'''
	l, r means the number of '(' and ')' unused.
	'''
	if l > r:
		return 
	if l == r == 0:
		res.append(path)
	if l:
		solve(l - 1, r, path + '(', res)
	if r:
		solve(l, r - 1, path + ')', res)

def generateParenthesis(n: int) -> List[str]:
	res = []
	solve(n, n, '', res)
	return res

assert(generateParenthesis(1) == ['()'])
assert(generateParenthesis(2) == ['(())', '()()'])
assert(generateParenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()'])






