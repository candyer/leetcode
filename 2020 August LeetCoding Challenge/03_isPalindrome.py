# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/

# Valid Palindrome

# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false
 
# Constraints:
# s consists only of printable ASCII characters.


def isPalindrome(s: str) -> bool:
	s = s.lower()
	left, right = 0, len(s) - 1
	while left < right:
		while left < right and not s[left].isalnum():
			left += 1
		while  left < right and not s[right].isalnum():
			right -= 1
		if s[left] != s[right]:
			return False
		else:
			left += 1
			right -= 1
	return True

assert(isPalindrome("A man, a plan, a canal: Panama") == True)
assert(isPalindrome("race a car") == False)
assert(isPalindrome("<.") == True)
assert(isPalindrome("1s") == False)


