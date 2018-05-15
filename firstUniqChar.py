# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# 387. First Unique Character in a String

# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

##############################
###### brute force TLE #######
##############################

# def firstUniqChar(s):
# 	"""
# 	:type s: str
# 	:rtype: int
# 	"""
# 	n = len(s)
# 	for i in xrange(n):
# 		if s.count(s[i]) == 1:
# 			return i 
# 	return -1


##############################
###### brute force TLE #######
##############################


from collections import defaultdict
def firstUniqChar(s):
	"""
	:type s: str
	:rtype: int
	"""
	n = len(s)
	count = defaultdict(list)
	for i in range(n):
		count[s[i]].append(i)

	res = float('inf')
	for letter, indices in count.items():
		if len(indices) == 1:
			res = min(res, indices[0])
	if res ==  float('inf'):
		return -1
	return res




print firstUniqChar("leetcode")
print firstUniqChar("loveleetcode")
print firstUniqChar("loeleetcod")
print firstUniqChar("aabbccss")
print firstUniqChar("")