# https://leetcode.com/problems/reverse-vowels-of-a-string/description/


# 345. Reverse Vowels of a String
# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".

# Note:
# The vowels does not include the letter "y".


def reverseVowels(s):
	"""
	:type s: str
	:rtype: str
	"""
	res = list(s)
	vowels = ['a', 'e', 'i', 'o', 'u']
	index = []
	v = []
	for i in range(len(s)):
		if s[i].lower() in vowels:
			index.append(i)
			v.append(s[i])
	for i, c in zip(index, v[::-1]):
		res[i] = c
	return ''.join(res)


assert reverseVowels('hello') == 'holle'
assert reverseVowels('leetcode') == 'leotcede'
assert reverseVowels('Aa') == 'aA'




