# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3491/

# Remove Duplicate Letters

# Given a string s, remove duplicate letters so that every letter appears once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.

# Note: 
# This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 
# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:
# 1 <= s.length <= 104
# s consists of lowercase English letters.


def removeDuplicateLetters(s: str) -> str:
	char_last_pos = {c: i for i, c in enumerate(s)}
	stack = []
	for i, c in enumerate(s):
		if not c in stack:
			while stack and stack[-1] > c and i < char_last_pos[stack[-1]]:
				stack.pop()
			stack.append(c)
	return "".join(stack)


assert(removeDuplicateLetters("bcabc") == "abc")
assert(removeDuplicateLetters("cbacdcbc") == "acdb")








