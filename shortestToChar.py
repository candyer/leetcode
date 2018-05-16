# https://leetcode.com/problems/shortest-distance-to-a-character/description/

# 821. Shortest Distance to a Character

# Given a string S and a character C, return an array of integers representing the shortest 
# distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

# Note:
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.


def shortestToChar(S, C):
	"""
	:type S: str
	:type C: str
	:rtype: List[int]
	"""
	n = len(S)
	res = [0] * n
	indice = []
	for i in range(n):
		if S[i] == C:
			indice.append(i)

	indice = [-indice[0]] + indice + [indice[-1] + (n - indice[-1]) * 2]
	m = len(indice)
	for j in range(1, m):
		begin, end = indice[j - 1], indice[j]
		for k in range(max(0, begin + 1), min(end, n)):
			res[k] = min(k - begin, end - k)
	return res

assert shortestToChar("abaaasdfghjkl", "b") == [1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert shortestToChar("abaa", "b") == [1, 0, 1, 2]
assert shortestToChar("aaba", "b") == [2, 1, 0, 1]
assert shortestToChar("loveleetcode", 'e') == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
assert shortestToChar("eloveleetcode", 'e') == [0, 1, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
assert shortestToChar("abcde", 'e') == [4, 3, 2, 1, 0]

