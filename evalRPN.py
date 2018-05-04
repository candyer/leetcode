# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/


# 150. Evaluate Reverse Polish Notation

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Note:

# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a 
# result and there won't be any divide by zero operation.
# Example 1:

# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22


def evalRPN(tokens):
	"""
	:type tokens: List[str]
	:rtype: int
	"""
	if not tokens:
		return 0
	
	signs = {
		'+': lambda x, y: y + x, 
		'-': lambda x, y: y - x, 
		'*': lambda x, y: y * x, 
		'/': lambda x, y: int(float(y) / x), 
	}

	stack = []
	for token in tokens:
		if token in signs:
			x = stack.pop()
			y = stack.pop()
			stack.append(signs[token](x, y))
		else:
			stack.append(int(token))
	return stack[0]

assert evalRPN(["4","3","-"]) == 1
assert evalRPN(["2", "1", "+", "3", "*"]) == 9
assert evalRPN(["4", "13", "5", "/", "+"]) == 6
assert evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22




