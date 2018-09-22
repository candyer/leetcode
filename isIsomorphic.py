# https://leetcode.com/problems/isomorphic-strings/description/


# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character but a character may map to itself.


# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

# Note:
# You may assume both s and t have the same length.


def isIsomorphic(s, t):
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	d1, d2 = {}, {}
	for c1, c2 in zip(s, t):
		if d1.setdefault(c1, c2) != c2 or d2.setdefault(c2, c1) != c1:
			return False
	return True


assert isIsomorphic("egg", "add") == True
assert isIsomorphic("foo", "bar") == False
assert isIsomorphic("paper", "title") == True
assert isIsomorphic("paper", "titll") == False

