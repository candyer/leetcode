# https://leetcode.com/problems/shortest-completing-word/description/

# 748. Shortest Completing Word

# Find the minimum length word from a given dictionary words, which has all the letters from the 
# string licensePlate. Such a word is said to complete the given string licensePlate

# Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

# It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in 
# the array.

# The license plate might have the same letter occurring multiple times. For example, given a 
# licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

# Example 1:
# Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
# Output: "steps"
# Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
# Note that the answer is not "step", because the letter "s" must occur in the word twice.
# Also note that we ignored case for the purposes of comparing whether a letter exists in the word.

# Example 2:
# Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
# Output: "pest"
# Explanation: There are 3 smallest length words that contains the letters "s".
# We return the one that occurred first.

# Note:
# licensePlate will be a string with length in range [1, 7].
# licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
# words will have a length in the range [10, 1000].
# Every words[i] will consist of lowercase letters, and have length in range [1, 15].



from collections import Counter as c
def f(n, word, d):
	d1 = c(word)
	all_in = True
	flag = False
	for k, v in d.items():
		if d1.get(k) == None:
			all_in = False
		elif d1.get(k) < v:
			all_in = False
		if k in d1:
			flag = True
	if not flag:
		all_in = False
	return all_in, flag

# print f(7, 'suggest', {'a': 1, 'h': 1})
# print f(4, 'easy', {'a': 1, 'h': 1})
# print f(7, 'husband', {'a': 1, 'h': 1})

def shortestCompletingWord(licensePlate, words):
	"""
	:type licensePlate: str
	:type words: List[str]
	:rtype: str
	"""
	d = {}
	licensePlate = licensePlate.lower()
	for c in licensePlate:
		if c.isalpha():
			d[c] = d.get(c, 0) + 1

	res1 = ''
	res2 = ''
	length1 = length2 = 20
	for word in words:
		n = len(word)
		all_in, flag = f(n, word, d)
		
		if all_in and n < length1:
			res1 = word
			length1 = n
		if flag and n < length2:
			res2 = word
			length2 = n
	if res1:
		return res1
	return res2


assert shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]) == 'steps'
assert shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]) == 'pest'
assert shortestCompletingWord("Ah71752",
["suggest","letter","of","husband","easy","education","drug","prevent","writer","old","ahhhhh"]) == 'ahhhhh'






