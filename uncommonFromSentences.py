# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

# 884. Uncommon Words from Two Sentences

# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Return a list of all uncommon words. 
# You may return the list in any order.


# Example 1:
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]

# Example 2:
# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
 

# Note:
# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A and B both contain only spaces and lowercase letters.

from collections import Counter as c

def uncommonFromSentences(A, B):
	"""
	:type A: str
	:type B: str
	:rtype: List[str]
	"""
	res = []
	for word, count in c(A.split() + B.split()).items():
		if count == 1:
			res.append(word)
	return res

assert uncommonFromSentences("this apple is sweet", "this apple is sour") == ['sweet', 'sour']
assert uncommonFromSentences("apple apple", "banana") == ['banana']
assert uncommonFromSentences("", "") == []
assert uncommonFromSentences("", "apple") == ['apple']


