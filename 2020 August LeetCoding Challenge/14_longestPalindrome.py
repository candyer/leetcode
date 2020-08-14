# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3423/

# Longest Palindrome

# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes 
# that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:
# Input: "abccccdd"

# Output: 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.



from collections import Counter
def longestPalindrome(s: str) -> int:
	res = 0
	for v in Counter(s).values():
		res += v
		if v % 2:
			res -= 1
	if res < len(s):
		res += 1
	return res

assert(longestPalindrome("abccccdd") == 7)
assert(longestPalindrome("aaabbbccc") == 7)
assert(longestPalindrome("a") == 1)