# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

# 557. Reverse Words in a String III

# Given a string, you need to reverse the order of characters in each word within 
# a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Note: In the string, each word is separated by single space and there will not 
# be any extra space in the string.

def reverseWords(s):
	"""
	:type s: str
	:rtype: str
	"""
	res = s.split()
	for i in range(len(res)):
		res[i] = res[i][::-1]
	return ' '.join(res)


assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"