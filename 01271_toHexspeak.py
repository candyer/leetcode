# https://leetcode.com/problems/hexspeak/description/

# 1271. Hexspeak

# A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, 
# then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  
# Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.
# Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

 
# Example 1:
# Input: num = "257"
# Output: "IOI"
# Explanation:  257 is 101 in hexadecimal.

# Example 2:
# Input: num = "3"
# Output: "ERROR"
 
# Constraints:
# 1 <= N <= 10^12
# There are no leading zeros in the given string.
# All answers must be in uppercase letters.



def toHexspeak(num: str) -> str:
	d = {0: 'O', 1:'I', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
	res = []
	num = int(num)
	while num:
		digit = num % 16
		if not digit in d:
			return 'ERROR'
		else:
			res.append(d[digit])
		num //= 16
	return ''.join(res[::-1])
        

assert(toHexspeak('257') == 'IOI')
assert(toHexspeak('3') == 'ERROR')
