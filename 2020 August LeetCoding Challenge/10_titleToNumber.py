# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419/

# Excel Sheet Column Number

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...

# Example 1:
# Input: "A"
# Output: 1

# Example 2:
# Input: "AB"
# Output: 28

# Example 3:
# Input: "ZY"
# Output: 701
 
# Constraints:
# 1 <= s.length <= 7
# s consists only of uppercase English letters.
# s is between "A" and "FXSHRXW".


def titleToNumber(s: str) -> int:
	n = len(s)
	res = 0
	for i in range(n):
		res += (ord(s[i]) - ord('A') + 1) * pow(26, (n - i - 1))
	return res

assert(titleToNumber("A") == 1)
assert(titleToNumber("AB") == 28)
assert(titleToNumber("ZY") == 701)
assert(titleToNumber("FXSHRXW") == 2147483647)
assert(titleToNumber("FXXW") == 122327)

