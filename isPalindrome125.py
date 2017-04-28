# https://leetcode.com/problems/valid-palindrome/#/description

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
# For the purpose of this problem, we define empty string as valid palindrome.


def isPalindrome(s):
	"""
	:type s: str
	:rtype: bool
	"""
	tmp = []
	for i in range(len(s)):
		if s[i].isalnum():
			tmp.append(s[i])
	for i in range(len(tmp) / 2):
		if tmp[i].lower() != tmp[len(tmp) - 1 - i].lower():
			return False
	return True

print isPalindrome("A man, a plan, a canal: Panama") #True
print isPalindrome(" ") #True
print isPalindrome("race a car") #False
