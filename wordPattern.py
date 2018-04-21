# https://leetcode.com/problems/word-pattern/description/

# 290. Word Pattern

# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.



def wordPattern(pattern, str):
	"""
	:type pattern: str
	:type str: str
	:rtype: bool
	"""
	str = str.split()
	m, n = len(pattern), len(str)
	if m != n: 
		return False
	dp, ds = {}, {}
	
	for i in range(m):
		if dp.get(pattern[i], 0) != ds.get(str[i], 0):
			return False
		dp[pattern[i]] = i + 1
		ds[str[i]] = i + 1
	return True


assert wordPattern("cddc", "dog cat cat dog") == True
assert wordPattern("cddc", "dog cat cat dog dog") == False
assert wordPattern("cddc", "x y z y") == False


