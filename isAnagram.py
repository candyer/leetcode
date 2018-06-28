# https://leetcode.com/problems/valid-anagram/description/

# 242. Valid Anagram

# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.


def isAnagram(s, t):
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	return sorted(s) == sorted(t)

assert isAnagram("anagram", "nagaram") == True
assert isAnagram("rat", "car") == False