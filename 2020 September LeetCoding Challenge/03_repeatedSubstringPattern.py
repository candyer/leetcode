# https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3447/

# Repeated Substring Pattern

# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of 
# the substring together. You may assume the given string consists of lowercase English letters only and its length will 
# not exceed 10000.

# Example 1:
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.

# Example 2:
# Input: "aba"
# Output: False

# Example 3:
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


############################################################
def repeatedSubstringPattern(s: str) -> bool:
	n = len(s)
	for i in range(n // 2):
		if n % (i + 1) == 0:
			rep = n // ( i + 1)
			sub_arr = s[:i + 1]
			# if all(s[j:j + i + 1] == sub_arr for j in range(i + 1, n, i + 1)):
			if sub_arr * rep == s:
				return True
	return False



############################################################
def repeatedSubstringPattern(s: str) -> bool:
	return s in (s + s)[1:-1]

assert(repeatedSubstringPattern("abab") == True)
assert(repeatedSubstringPattern("aba") == False)
assert(repeatedSubstringPattern("abcabcabcabc") == True)
assert(repeatedSubstringPattern("abcababcab") == True)
assert(repeatedSubstringPattern("abaabaaba") == True)
assert(repeatedSubstringPattern("aaaaaaaaaaaa") == True)
assert(repeatedSubstringPattern("ab") == False)






