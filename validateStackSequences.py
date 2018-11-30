# https://leetcode.com/problems/validate-stack-sequences/description/


# 946. Validate Stack Sequences


# Given two sequences pushed and popped with distinct values, return true if and only if this could have been 
# the result of a sequence of push and pop operations on an initially empty stack.

# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# Example 2:
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
 
# Note:
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.


def validateStackSequences(pushed, popped):
	"""
	:type pushed: List[int]
	:type popped: List[int]
	:rtype: bool
	"""
	n, m = len(pushed), len(popped)
	if n != m:
		return False
	stack = []
	i = j = 0
	while i < n:
		stack.append(pushed[i])
		while stack and popped[j] == stack[-1] and j < n:
			stack.pop()
			j += 1
		i += 1
	return stack == []

assert validateStackSequences([1,2,3,4,5], [4,5,3,2,1]) == True
assert validateStackSequences([1,2,3,4,5], [4,3,5,1,2]) == False
assert validateStackSequences([1,2,3], [3,2,1,7,5]) == False

