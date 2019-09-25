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

#####################
#### brute force ####
#####################
def lastSubstring(s):
	"""
	:type s: str
	:rtype: str
	"""
	maxi = max(s)
	pre = -2
	res = ''
	for i in range(len(s)):
		if s[i] == maxi:
			if pre + 1 != i:
				res = max(res, s[i:])
			pre = i
	return res


#####################
#### suffix array ###
#####################
def lastSubstring(s):
	if len(set(s)) == 1:
		return s
	n = len(s)
	pos = n - 1
	for i in range(n - 2, -1, -1):
		j = 0
		while pos + j < n:
			curr, tail = s[i + j], s[pos + j]
			if curr < tail:
				break
			elif curr > tail:
				pos = i
				break
			else:
				j += 1
		if pos + j == n:
			pos = i
	return s[pos:]

assert lastSubstring('tatywyyrb') == 'yyrb'
assert lastSubstring('abab') == 'bab'
assert lastSubstring('leetcode') == 'tcode'
assert lastSubstring('upgups') == 'ups'
assert lastSubstring('lslydbyjwm') == 'yjwm'
assert lastSubstring('zzzzzzzzzz') == 'zzzzzzzzzz'
assert lastSubstring('zzzzzazzzz') == 'zzzzzazzzz'






