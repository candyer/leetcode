# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3451/

# Word Pattern

# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false

# Example 4:
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters 
# that may be separated by a single space.




def wordPattern(pattern: str, str: str) -> bool:
	n = len(pattern)
	words = str.split(' ')
	if len(words) != n:
		return False

	d_pattern, d_word = {}, {}
	for i in range(n):
		if d_pattern.get(pattern[i], -1) != d_word.get(words[i], -1):
			return False
		d_pattern[pattern[i]] = d_word[words[i]] = i
	return True


assert(wordPattern("abba", "dog cat cat dog") == True)
assert(wordPattern("abba", "dog cat cat fish") == False)
assert(wordPattern("aaaa", "dog cat cat dog") == False)
assert(wordPattern("abba", "dog dog dog dog") == False)
assert(wordPattern("abba", "dog cat dog cat") == False)


