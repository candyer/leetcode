# https://leetcode.com/contest/weekly-contest-78/problems/expressive-words/

# 809. Expressive Words

# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", 
# "hi" -> "hiiii".  Here, we have groups, of adjacent letters that are all the same character, 
# and adjacent characters to the group are different.  A group is extended if that group is 
# length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be 
# extended in the second example.  As another example, the groups of "abbcccaaaa" would be 
# "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.

# For some given string S, a query word is stretchy if it can be made to be equal to S by 
# extending some groups.  Formally, we are allowed to repeatedly choose a group (as defined 
# 	above) of characters c, and add some number of the same character c to it so that the 
# length of the group is 3 or more.  Note that we cannot extend a group of size one like "h" 
# to a group of size two like "hh" - all extensions must leave the group extended - ie., 
# at least 3 characters long.

# Given a list of query words, return the number of words that are stretchy. 

# Example:
# Input: 
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.
# Notes:

# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters

def f(string):
	res = []
	string += '*'
	count = 1
	length = 0
	for i in range(1, len(string)):
		if string[i] != string[i - 1]:
			res.append([string[i - 1], count])
			length += 1
			count = 1
		else:
			count += 1
	return length, res	

def expressiveWords(S, words):
	"""
	:type S: str
	:type words: List[str]
	:rtype: int
	"""
	length_x, x = f(S)
	res = 0
	for word in words:
		flag = True
		length_y, y = f(word)
		if length_x == length_y:
			for a, b in zip(x, y):
				if a[0] != b[0]:
					flag = False
					break
				elif a[1] < b[1]:
					flag = False
					break
				elif a[1] < 3 and a[1] != b[1]:
					flag = False
					break
			if flag:
				res += 1
	return res

assert expressiveWords("heeellooo", ["helo", "heclo", "hello", "helloooooo", "hi"]) == 1
assert expressiveWords("abcd", ["abc"]) == 0
















