# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3667/

# Integer to Roman

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. The same principle applies to the number nine, 
# which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

# Example 1:
# Input: num = 3
# Output: "III"

# Example 2:
# Input: num = 4
# Output: "IV"

# Example 3:
# Input: num = 9
# Output: "IX"

# Example 4:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 5:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
# Constraints:
# 1 <= num <= 3999


def intToRoman(num: int) -> str:
    romans = [
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "M", "MM", "MMM"]
        ]

    res = [''] * 4
    i = 0
    while num:
    	# print('-------', num % 10, romans[i][num % 10])
    	res[3 - i] = romans[i][num % 10]
    	num //= 10
    	i += 1
    return ''.join(res)


assert(intToRoman(3) == "III")
assert(intToRoman(4) == "IV")
assert(intToRoman(9) == "IX")
assert(intToRoman(58) == "LVIII")
assert(intToRoman(1994) == "MCMXCIV")

