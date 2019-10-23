# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/


# 1221. Split a String in Balanced Strings


# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.

# Example 1:
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

# Example 2:
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

# Example 3:
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".
 

# Constraints:
# 1 <= s.length <= 1000
# s[i] = 'L' or 'R'


def balancedStringSplit(s):
	"""
	:type s: str
	:rtype: int
	"""
	count = res = 0
	for c in s:
		if c == 'R':
			count += 1
		else:
			count -= 1
		if count == 0:
			res += 1
	return res


assert balancedStringSplit("RLRRLLRLRL") == 4
assert balancedStringSplit("RLLLLRRRLR") == 3
assert balancedStringSplit("LLLLRRRR") == 1
assert balancedStringSplit("RRLRLL") == 1




