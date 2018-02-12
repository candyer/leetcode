# https://leetcode.com/problems/roman-to-integer/description/


# 13. Roman to Integer

# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

def romanToInt(s):
	"""
	:type s: str
	:rtype: int
	"""
	roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	res = 0
	n = len(s)
	for i in range(0, n - 1):
		if roman[s[i]] < roman[s[i + 1]]:
			res -= roman[s[i]]
		else:		
			res += roman[s[i]]
	return res + roman[s[-1]]


assert romanToInt('DCXXI') == 621
assert romanToInt('MMMCMXCIX') == 3999

