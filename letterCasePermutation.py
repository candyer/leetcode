# https://leetcode.com/problems/letter-case-permutation/description/

# 784. Letter Case Permutation

# Given a string S, we can transform every letter individually to be lowercase or uppercase 
# to create another string.  Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]

# Note:
# S will be a string with length at most 12.
# S will consist only of letters or digits.

from itertools import product as p
def letterCasePermutation(S):
	"""
	:type S: str
	:rtype: List[str]
	"""
	tmp = []
	for c in S:
		if c.isalpha():
			tmp.append([c.lower(), c.upper()])
		else:
			tmp.append(c)
	return [''.join(i) for i in p(*tmp)]

print letterCasePermutation("a1b2c3D4")
print letterCasePermutation("a1b2") == ['a1b2', 'a1B2', 'A1b2', 'A1B2']
print letterCasePermutation("3z4") == ['3z4', '3Z4']
print letterCasePermutation("12345") == ['12345']
