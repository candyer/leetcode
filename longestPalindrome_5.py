# https://leetcode.com/problems/longest-palindromic-substring/description/

# 5. Longest Palindromic Substring


# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"


def longestPalindrome(s):
	"""
	:type s: str
	:rtype: str
	"""
	n = len(s)
	dp = [[True if i == j else False for j in range(n)] for i in range(n)]
	res = s[:1]
	for i in range(n):
		for j in range(i - 1, -1, -1):
			if s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1]):
				dp[i][j] = True
				if i - j + 1 > len(res):
					res = s[j : i + 1]	
	return res



assert longestPalindrome("babad") == "bab"
assert longestPalindrome("cbbd") == "bb"
assert longestPalindrome("cdadcxyx") == "cdadc"
