# https://leetcode.com/contest/leetcode-weekly-contest-52/problems/repeated-string-match/

def repeatedStringMatch(A, B):
	"""
	:type A: str
	:type B: str
	# :rtype: int
	# """
	m, n = len(A), len(B)
	res, i = n / m, 0
	while i < 3:
		if B in A * (res + i): 
			return res + i
		i += 1
	return -1

assert repeatedStringMatch("abcd", "cdabcdab") == 3
assert repeatedStringMatch("abc", "cbabc") == -1
assert repeatedStringMatch("abc", "cb") == -1
assert repeatedStringMatch("abcd", "da") == 2
assert repeatedStringMatch("abcdefghij", "ja") == 2
assert repeatedStringMatch("abcdefghij", "z") == -1
assert repeatedStringMatch("abc", "c") == 1
assert repeatedStringMatch("a", "aaaaaaaaaaa") == 11
assert repeatedStringMatch("ab", "aabb") == -1
assert repeatedStringMatch("aaaaaaaaa", "aabb") == -1
