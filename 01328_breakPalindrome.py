# https://leetcode.com/problems/break-a-palindrome/description/


# 1328. Break a Palindrome

# Given a palindromic string palindrome, replace exactly one character by any lowercase English letter 
# so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

# After doing so, return the final string.  If there is no way to do so, return the empty string.


# Example 1:
# Input: palindrome = "abccba"
# Output: "aaccba"

# Example 2:
# Input: palindrome = "a"
# Output: ""
 

# Constraints:
# 1 <= palindrome.length <= 1000
# palindrome consists of only lowercase English letters.

from typing import List
def breakPalindrome(palindrome: str) -> str:
	n = len(palindrome)
	if n == 1: 
		return ''
	arr = list(palindrome)

	i = 0
	while i < n:
		if arr[i] != 'a' and i != n - i - 1:
			arr[i] = 'a'
			break
		i += 1
	if i == n:
		arr[i - 1] = chr(ord(arr[i - 1]) + 1)
	return ''.join(arr)


assert(breakPalindrome("abccba") == 'aaccba')
assert(breakPalindrome("a") == '')
assert(breakPalindrome("cdc") == 'adc')
assert(breakPalindrome("aa") == 'ab')
assert(breakPalindrome("aaaaaaaaa") == 'aaaaaaaab')
assert(breakPalindrome("aba") == 'abb')
assert(breakPalindrome("aaabaaa") == 'aaabaab')





