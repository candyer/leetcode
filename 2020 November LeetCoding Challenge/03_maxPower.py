# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3518/


# Consecutive Characters

# Given a string s, the power of the string is the maximum length of a non-empty substring that 
# contains only one unique character.

# Return the power of the string.

# Example 1:
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.

# Example 2:
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

# Example 3:
# Input: s = "triplepillooooow"
# Output: 5

# Example 4:
# Input: s = "hooraaaaaaaaaaay"
# Output: 11

# Example 5:
# Input: s = "tourist"
# Output: 1
 

# Constraints:
# 1 <= s.length <= 500
# s contains only lowercase English letters.



def maxPower(s: str) -> int:
	s += '*'
	res = count = 1
	for i in range(1, len(s)):
		if s[i - 1] == s[i]:
			count += 1
		else:
			res = max(res, count)
			count = 1
	return res

assert(maxPower("leetcode") == 2)
assert(maxPower("abbcccddddeeeeedcba") == 5)
assert(maxPower("triplepillooooow") == 5)
assert(maxPower("hooraaaaaaaaaaay") == 11)
assert(maxPower("tourist") == 1)
assert(maxPower("t") == 1)
assert(maxPower("cc") == 2)










