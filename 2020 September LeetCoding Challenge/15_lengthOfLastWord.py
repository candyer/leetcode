# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3461/

# Length of Last Word


# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return 
# the length of last word (last word means the last appearing word if we loop from left to right) in the string.
# If the last word does not exist, return 0.

# Note: A word is defined as a maximal substring consisting of non-space characters only.

# Example:
# Input: "Hello World"
# Output: 5
 

def lengthOfLastWord(s: str) -> int:
	arr = s.split()
	return len(arr[-1]) if arr else 0

assert(lengthOfLastWord("Hello World") == 5)
assert(lengthOfLastWord("") == 0)
assert(lengthOfLastWord("a ") == 1)