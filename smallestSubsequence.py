# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/

# 1081. Smallest Subsequence of Distinct Characters

# Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.


# Example 1:
# Input: "cdadabcc"
# Output: "adbc"

# Example 2:
# Input: "abcd"
# Output: "abcd"

# Example 3:
# Input: "ecbacba"
# Output: "eacb"

# Example 4:
# Input: "leetcode"
# Output: "letcod"
 
# Note:
# 1 <= text.length <= 1000
# text consists of lowercase English letters.


def smallestSubsequence(text):
	"""
	:type text: str
	:rtype: str
	"""
	rightmost_idx = {c: i for i, c in enumerate(text)}
	res = []
	left = 0
	while rightmost_idx:
		right = min(rightmost_idx.values())
		char = ''
		idx = 0
		for i in range(left, right + 1):
			if text[i] not in res:
				if char == '':
					char, idx = text[i], i
				elif text[i] < char:
					char, idx = text[i], i
		res.append(char)
		rightmost_idx.pop(char)
		left = idx + 1
	return ''.join(res)



assert smallestSubsequence("cdadabcc") == 'adbc'
assert smallestSubsequence("abcd") == 'abcd'
assert smallestSubsequence("ecbacba") == 'eacb'
assert smallestSubsequence("leetcode") == 'letcod'
assert smallestSubsequence("baaaaab") == 'ab'


