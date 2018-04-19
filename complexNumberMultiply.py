# https://leetcode.com/problems/complex-number-multiplication/description/


# 537. Complex Number Multiplication

# Given two strings representing two complex numbers.

# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

# Example 1:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
# Note:

# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a and b will both belong to the 
# range of [-100, 100]. And the output should be also in this form.

def complexNumberMultiply(a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	n1, c = a.split('+')
	n2, e = b.split('+')
	n1 = int(n1)
	n2 = int(n2)
	c = int(c[:-1])
	e = int(e[:-1])

	res = [str(n1 * n2 + c * e * (-1)), '+', str(n1 * e + n2 * c) + 'i']
	return ''.join(res)


assert complexNumberMultiply("1+0i", "1+0i") == '1+0i'
assert complexNumberMultiply("1+1i", "1+1i") == '0+2i'
assert complexNumberMultiply("1+-1i", "1+-1i") == '0+-2i'

