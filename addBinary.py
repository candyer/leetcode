# https://leetcode.com/problems/add-binary/#/description

# Given two binary strings, return their sum (also a binary string).
# For example,
# a = "11"     b = "1"      Return "100".


def addBinary(a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	return bin(int(a, 2) + int(b, 2))[2:]

print addBinary("110101100", "1000000000000000000001") #"1000000000000110101101"
