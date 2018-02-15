# https://leetcode.com/problems/longest-palindrome/description/

# 409. Longest Palindrome

# Given a string which consists of lowercase or uppercase letters, find the length of 
# the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:  Input: "abccccdd"   Output: 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

from collections import Counter as c
def longestPalindrome(s):
	"""
	:type s: str
	:rtype: int
	"""
	d = c(s)
	res = odd = 0
	for val in d.values():
		if val % 2 == 0:
			res += val
		else:
			res += val - 1
			odd = 1
	return res + odd

assert longestPalindrome("abccccddeee") == 9
assert longestPalindrome("a") == 1
assert longestPalindrome("abbccc") == 5
assert longestPalindrome("cccbBb") == 5
assert longestPalindrome("ccc") == 3
