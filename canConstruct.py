# https://leetcode.com/problems/ransom-note/description/


# 383. Ransom Note

# Given an arbitrary ransom note string and another string containing letters 
# from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

from collections import Counter as c
def canConstruct(ransomNote, magazine):
	"""
	:type ransomNote: str
	:type magazine: str
	:rtype: bool
	"""
	d1, d2 = c(ransomNote), c(magazine)
	for k, v in d1.items():
		if v > d2[k]:
			return False
	return True

assert canConstruct('a', 'b') == False
assert canConstruct('aa', 'ab') == False
assert canConstruct('dba', 'aabcd') == True



