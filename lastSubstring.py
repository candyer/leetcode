# https://leetcode.com/problems/last-substring-in-lexicographical-order/description/

# 1163. Last Substring in Lexicographical Order


# Given a string s, return the last substring of s in lexicographical order.

# Example 1:
# Input: "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. 
# The lexicographically maximum substring is "bab".

# Example 2:
# Input: "leetcode"
# Output: "tcode"

# Note:
# 1 <= s.length <= 4 * 10^5
# s contains only lowercase English letters.

from collections import defaultdict
def lastSubstring(s):
	"""
	:type s: str
	:rtype: str
	"""
	n = len(s)

	poses = []
	maxi = max(s)
	pre = -2
	for i in range(n):
		if s[i] == maxi:
			if pre + 1 != i:
				poses.append(i)
			pre = i

	res = ''
	for pos in poses:
		res = max(res, s[pos:])
	return res

assert lastSubstring('abab') == 'bab'
assert lastSubstring('leetcode') == 'tcode'
assert lastSubstring('upgups') == 'ups'
assert lastSubstring('lslydbyjwm') == 'yjwm'
assert lastSubstring('zzzzzzzzzz') == 'zzzzzzzzzz'
assert lastSubstring('zzzzzazzzz') == 'zzzzzazzzz'






