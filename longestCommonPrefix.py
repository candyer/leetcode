# https://leetcode.com/problems/longest-common-prefix/description/


# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	if not strs: return ''
	mini, maxi = min(strs), max(strs)

	for i, string in enumerate(mini):
		if string != maxi[i]:
			return mini[:i]
	return mini




print longestCommonPrefix(["bzc", "azertyui",  "aertiertyuio"]) == ''
print longestCommonPrefix(["atcg", "ag", "cg"]) == ''
print longestCommonPrefix(["abc", "abcd", "abcde"]) == 'abc'
print longestCommonPrefix([]) == ''