# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/

# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


from collections import Counter
def firstUniqChar(s: str) -> int:
	d = Counter(s)
	i = 0
	while i < len(s):
		if d[s[i]] == 1:
			return i
		i += 1
	return -1

assert(firstUniqChar("leetcode") == 0)
assert(firstUniqChar("loveleetcode") == 2)