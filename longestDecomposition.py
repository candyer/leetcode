# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/

# 1147. Longest Chunked Palindrome Decomposition

# Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

# Each a_i is a non-empty string;
# Their concatenation a_1 + a_2 + ... + a_k is equal to text;
# For all 1 <= i <= k,  a_i = a_{k+1 - i}.
 

# Example 1:
# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".

# Example 2:
# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".

# Example 3:
# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".

# Example 4:
# Input: text = "aaa"
# Output: 3
# Explanation: We can split the string on "(a)(a)(a)".
 

# Constraints:
# text consists only of lowercase English characters.
# 1 <= text.length <= 1000


from collections import defaultdict
def longestDecomposition(text):
	"""
	:type text: str
	:rtype: int
	"""
	n = len(text)
	d = defaultdict(list)
	for i in range(n):
		d[text[i]].append(i)

	left, right, res = 0, n - 1, 0
	while left < right:
		if text[left] == text[right]:
			res += 2
			left += 1
			right -= 1
		else:
			for i in d[text[right]]:
				if i > left:
					tmp = i
					length = i - left + 1
					if text[left:left + length] == text[right - length + 1:right + 1]:
						break
			if text[left:left + length] == text[right - length + 1:right + 1] and left + length - 1 != right:
				res += 2
				left += length
				right -= length
			else:
				res += 1
				break
	if left == right:
		res += 1
	return res

assert longestDecomposition("ghiabcdefhelloadamhelloabcdefghi") == 7
assert longestDecomposition("merchant") == 1
assert longestDecomposition("antaprezatepzapreanta") == 11
assert longestDecomposition("aaa") == 3
assert longestDecomposition("abazaza") == 3
assert longestDecomposition("abadxyabcxydaba") == 11
assert longestDecomposition("nufbkflwjjlwjjnufbkf") == 4



