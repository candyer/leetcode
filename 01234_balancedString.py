# https://leetcode.com/problems/replace-the-substring-for-balanced-string/description/

# 1234. Replace the Substring for Balanced String

# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
# A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
# Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.
# Return 0 if the string is already balanced.


# Example 1:
# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced.

# Example 2:
# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

# Example 3:
# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER". 

# Example 4:
# Input: s = "QQQQ"
# Output: 3
# Explanation: We can replace the last 3 'Q' to make s = "QWER".
 

# Constraints:
# 1 <= s.length <= 10^5
# s.length is a multiple of 4
# s contains only 'Q', 'W', 'E' and 'R'.


from collections import Counter
def balancedString(s):
	"""
	:type s: str
	:rtype: int
	"""
	n = len(s)
	avg = n / 4
	d = Counter(s)
	res = float('inf')
	left = 0
	for right in range(n):
		d[s[right]] -= 1
		while left < n and max(d.values()) <= avg:
			res = min(res, right - left + 1)
			d[s[left]] += 1
			left += 1
	return res


assert balancedString("QWER") == 0
assert balancedString("QQWE") == 1
assert balancedString("QQQW") == 2
assert balancedString("QQQQ") == 3
assert balancedString("QQQQWWWE") == 3
assert balancedString("WWEQERQWQWWRWWERQWEQ") == 4







