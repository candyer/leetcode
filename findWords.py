# https://leetcode.com/problems/keyboard-row/description/

# 500. Keyboard Row

# Given a List of words, return the words that can be typed using letters of 
# alphabet on only one row's of American keyboard.

# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

def f(s):
	row1 = 'qwertyuiop'
	row2 = 'asdfghjkl'
	row3 = 'zxcvbnm'
	r1 = r2 = r3 = 0
	for c in s:
		if c.lower() in row1:
			r1 += 1
		elif c.lower() in row2:
			r2 += 1
		else:
			r3 += 1
	if r1 == r2 == 0 or r2 == r3 == 0 or r1 == r3 == 0:
		return True
	return False

def findWords(words):
	"""
	:type words: List[str]
	:rtype: List[str]
	"""
	res = []
	for word in words:
		if f(word):
			res.append(word)
	return res

assert findWords(["Hello", "Alaska", "Dad", "Peace"]) == ['Alaska', 'Dad']


