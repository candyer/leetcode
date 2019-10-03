# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

# 1209. Remove All Adjacent Duplicates in String II

# Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and 
# removing them causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made.
# It is guaranteed that the answer is unique.

# Example 1:
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.

# Example 2:
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

# Example 3:
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
 
# Constraints:
# 1 <= s.length <= 10^5
# 2 <= k <= 10^4
# s only contains lower case English letters.


def removeDuplicates(s, k):
	"""
	:type s: str
	:type k: int
	:rtype: str
	"""
	stack = []
	blocks = []
	n, m = 0, 1 # n is length of stack, m is the length of current block of duplicates
	for c in s:
		if n < m or m < k:
			if stack:
				if stack[-1] == c:
					m += 1
				else:
					blocks.append(m)
					m = 1
			stack.append(c)
			n += 1
			
		if n >= k and m == k:
			stack = stack[:n - k]
			n -= k
			if blocks:
				m = blocks[-1]	
				blocks.pop()
			else:
				m = 1
	return ''.join(stack)


assert removeDuplicates("abcd", 2) == 'abcd'
assert removeDuplicates("deeedbbcccbdaa", 3) == 'aa'
assert removeDuplicates("pbbcggttciiippooaais", 2) == 'ps'
assert removeDuplicates("ababbaba", 2) == ''
assert removeDuplicates("aabbccddddddddccbbac", 4) == 'aaac'
assert removeDuplicates("nnwssswwnvbnnnbbqhhbbbhmmmlllm", 3) == 'vqm'

