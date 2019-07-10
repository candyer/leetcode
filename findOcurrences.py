# https://leetcode.com/problems/occurrences-after-bigram/


# 1078. Occurrences After Bigram

# Given words first and second, consider occurrences in some text of the form "first second third", 
# where second comes immediately after first, and third comes immediately after second.

# For each such occurrence, add "third" to the answer, and return the answer.

# Example 1:
# Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
# Output: ["girl","student"]

# Example 2:
# Input: text = "we will we will rock you", first = "we", second = "will"
# Output: ["we","rock"]
 
# Note:
# 1 <= text.length <= 1000
# text consists of space separated words, where each word consists of lowercase English letters.
# 1 <= first.length, second.length <= 10
# first and second consist of lowercase English letters.


def findOcurrences(text, first, second):
	"""
	:type text: str
	:type first: str
	:type second: str
	:rtype: List[str]
	"""
	words = text.split()
	n = len(words)
	res = []
	for i in range(n - 2):
		if words[i] == first and words[i + 1] == second:
			res.append(words[i + 2])
	return res


assert findOcurrences("alice is a good girl she is a good student", "a", "good") == ['girl', 'student']
assert findOcurrences("we will we will rock you", "we", "will") == ['we', 'rock']
assert findOcurrences("a a a b", 'a', 'a') == ['a', 'b']
