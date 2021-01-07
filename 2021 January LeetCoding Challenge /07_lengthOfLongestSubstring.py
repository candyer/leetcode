# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3595/


# Longest Substring Without Repeating Characters


# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0
 

# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

def lengthOfLongestSubstring(s: str) -> int:
	d  = {}
	left = res = 0
	for right in range(len(s)):
		if s[right] in d:
			left = max(left, d[s[right]])
		res = max(res, right - left + 1)
		d[s[right]] = right + 1
	return res


assert(lengthOfLongestSubstring("abcddcbae") == 5)
assert(lengthOfLongestSubstring("abcabcbb") == 3)
assert(lengthOfLongestSubstring("bbbbb") == 1)
assert(lengthOfLongestSubstring("pwwkew") == 3)
assert(lengthOfLongestSubstring("") == 0)


