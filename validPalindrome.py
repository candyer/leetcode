# https://leetcode.com/problems/valid-palindrome-ii/description/

# 680. Valid Palindrome II


# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True

# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.



def validPalindrome(s):
	"""
	:type s: str
	:rtype: bool
	"""
	n = len(s)
	left, right = 0, n - 1
	while left < right:
		if s[left] == s[right]:
			left += 1
			right -= 1
		else:
			return s[left + 1:right + 1] == s[left + 1:right + 1][::-1] or s[left:right] == s[left:right][::-1]
	return True



assert validPalindrome("aba") == True
assert validPalindrome("abca") == True
assert validPalindrome("abdca") == False
