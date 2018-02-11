# https://leetcode.com/problems/integer-to-roman/description/

# 12. Integer to Roman

# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.


def intToRoman(num):
	"""
	:type num: int
	:rtype: str
	"""
	romans = [
		["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
		["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
		["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
		["", "M", "MM", "MMM"]
		]
	res = []
	res.append(romans[3][num / 1000 % 10]);
	res.append(romans[2][num / 100 % 10]);
	res.append(romans[1][num / 10 % 10]);
	res.append(romans[0][num % 10]);
	return ''.join(res)


assert intToRoman(101) == 'CI'
assert intToRoman(1000) == 'M'
assert intToRoman(200) == 'CC'
assert intToRoman(1500) == 'MD'
assert intToRoman(3999) == 'MMMCMXCIX'
