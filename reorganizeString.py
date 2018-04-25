# https://leetcode.com/problems/reorganize-string/description/

# 767. Reorganize String

# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each 
# other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

# Example 1:

# Input: S = "aab"
# Output: "aba"
# Example 2:

# Input: S = "aaab"
# Output: ""
# Note:

# S will consist of lowercase letters and have length in range [1, 500].


from collections import Counter as c
def reorganizeString(S):
	"""
	:type S: str
	:rtype: str
	"""
	d = c(S)
	n = len(S)
	res = [''] * n
	tmp = zip(d.values(), d.keys())
	tmp.sort(reverse=True)
	start = 0
	for v, k in tmp:
		if v > (n + 1) / 2:
			return ''
		for _ in range(v):
			if start < n:
				res[start] = k
			else:
				start = 1
				res[start] = k
			start += 2
	return ''.join(res)


assert reorganizeString('aab') == 'aba'
assert reorganizeString('aaabbc') == 'ababac'
assert reorganizeString('aaab') == ''




