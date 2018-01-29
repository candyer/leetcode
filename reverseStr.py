# https://leetcode.com/problems/reverse-string-ii/description/
# 541. Reverse String II

# Given a string and an integer k, you need to reverse the first k characters for every 2k 
# characters counting from the start of the string. If there are less than k characters left, 
# reverse all of them. If there are less than 2k but greater than or equal to k characters, 
# then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

def reverseStr(s, k):
	"""
	:type s: str
	:type k: int
	:rtype: str
	"""
	res = list(s)
	for i in range(0, len(s), k*2):
		res[i: i + k] = reversed(s[i: i + k])
	return ''.join(res)


assert reverseStr('abcdefg', 2) == 'bacdfeg'
assert reverseStr('abcdefghigklmnopq', 3) == 'cbadefihggklonmpq'


		