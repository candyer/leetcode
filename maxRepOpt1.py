# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/description/

# 1156. Swap For Longest Repeated Character Substring

# Given a string text, we are allowed to swap two of the characters in the string. 
# Find the length of the longest substring with repeated characters.

# Example 1:
# Input: text = "ababa"
# Output: 3
# Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.

# Example 2:
# Input: text = "aaabaaa"
# Output: 6
# Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.

# Example 3:
# Input: text = "aaabbaaa"
# Output: 4

# Example 4:
# Input: text = "aaaaa"
# Output: 5
# Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.

# Example 5:
# Input: text = "abcdef"
# Output: 1

# Constraints:
# 1 <= text.length <= 20000
# text consist of lowercase English characters only.



from collections import Counter as c
def maxRepOpt1(text):
	"""
	:type text: str
	:rtype: int
	"""
	n = len(text)
	d = c(text)
	counts = []
	text += '*'
	res = 0
	tmp = 1
	for i in range(n):
		if text[i] == text[i + 1]:
			tmp += 1
		else:
			counts.append((text[i], tmp))
			res = max(res, min(tmp + 1, d[text[i]]))
			tmp = 1

	for i in range(1, len(counts) - 1):
		left_c, left_count = counts[i - 1]
		mid_c, mid_count = counts[i]
		right_c, right_count = counts[i + 1]

		if left_c == right_c and mid_count == 1:
			res = max(res, min(left_count + right_count + 1, d[right_c]))

	return res

assert maxRepOpt1("adfaaaa") == 5
assert maxRepOpt1("aaabbbb") == 4
assert maxRepOpt1("ababa") == 3
assert maxRepOpt1("aaabaaa") == 6
assert maxRepOpt1("aaabbaaa") == 4
assert maxRepOpt1("aaaaa") == 5
assert maxRepOpt1("abcdef") == 1
assert maxRepOpt1("aabbaccdda") == 3
assert maxRepOpt1("adbaccaaa") == 4



