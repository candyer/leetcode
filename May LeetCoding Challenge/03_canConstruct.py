# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/


# Given an arbitrary ransom note string and another string containing letters from all the magazines, 
# write a function that will return true if the ransom note can be constructed from the magazines ; 
# otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
	d1 = Counter(ransomNote)
	d2 = Counter(magazine)
	for k, v in d1.items():
		if k not in d2 or v > d2[k]:
			return False
	return True

assert(canConstruct("a", "b") == False)
assert(canConstruct("aa", "ab") == False)
assert(canConstruct("aa", "aab") == True)