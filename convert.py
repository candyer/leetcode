# https://leetcode.com/problems/zigzag-conversion/description/

# 6. ZigZag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display 
# this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I


def convert(s, numRows):
	"""
	:type s: str
	:type numRows: int
	:rtype: str
	"""
	if numRows <= 1:
		return s
	block = numRows * 2 - 2
	res = []
	n = len(s)
	for i in range(numRows):
		tmp = []
		for j in range(i, n, block):
			tmp.append(s[j])
			if 0 < i < numRows - 1 and 0 < j + block - 2 * i < n:
				tmp.append(s[j + block - 2 * i])
		res.append(''.join(tmp))
	return ''.join(res)



assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"


