# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

# 1160. Find Words That Can Be Formed by Characters

# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.

# Example 1:
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Example 2:
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: 
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 
# Note:
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# All strings contain lowercase English letters only.


from collections import Counter
def countCharacters(words, chars):
	"""
	:type words: List[str]
	:type chars: str
	:rtype: int
	"""
	d_char = Counter(chars)
	res = 0
	for word in words:
		flag = True
		for k, v in Counter(word).items():
			if v > d_char[k]:
				flag = False
				break
		if flag:
			res += len(word)
	return res


assert countCharacters(["cat","bt","hat","tree"], chars = "atach") == 6
assert countCharacters(["hello","world","leetcode"], chars = "welldonehoneyr") == 10
assert countCharacters(["athomea", "at","home"], chars = "athomea") == 13
assert countCharacters(["abbc", "ab","bc"], chars = "abc") == 4
assert countCharacters(["abbc", "abb","bc"], chars = "abbc") == 9
