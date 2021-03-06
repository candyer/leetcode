# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3362/

# Validate IP Address

# Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

# IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, 
# each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

# Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

# IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. 
# The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 
# is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters 
# in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address
# (Omit leading zeros and using upper cases).

# However, we don't replace a consecutive group of zero value with a single empty group using two consecutive 
# colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

# Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 
# 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

# Note: You may assume there is no extra space or special characters in the input string.


# Example 1:
# Input: "172.16.254.1"
# Output: "IPv4"
# Explanation: This is a valid IPv4 address, return "IPv4".

# Example 2:
# Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"
# Explanation: This is a valid IPv6 address, return "IPv6".

# Example 3:
# Input: "256.256.256.256"
# Output: "Neither"
# Explanation: This is neither a IPv4 address nor a IPv6 address.

from typing import List
def isValidIPv4(IP: List[str]):
	for s in IP:
		n = len(s)
		if n == 0 or n > 3:
			return "Neither" 
		if s.startswith('0') and s != '0':
			return "Neither"
		if not s.isdigit() or int(s) > 255:
			return "Neither"
	return "IPv4"

def isValidIPv6(IP):
	for s in IP:
		n = len(s)
		if n == 0 or n > 4:
			return "Neither"
		for c in s:
			if not c in '0123456789abcdef':
				return "Neither"
	return "IPv6"

def validIPAddress(IP: str) -> str:
	if IP.count('.') == 3:
		return isValidIPv4(IP.split('.'))
	elif IP.count(':') == 7:
		return isValidIPv6(IP.lower().split(':'))
	else:
		return "Neither"


assert(validIPAddress("172.16.254.1") == 'IPv4')
assert(validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334") == 'IPv6')
assert(validIPAddress("2001:0db8:85a3:1234:8A2E:0370:7334:0000") == 'IPv6')
assert(validIPAddress("256.256.256.256") == 'Neither')
assert(validIPAddress("2001:0db8:85a3::8A2E:0370:7334") == 'Neither')
assert(validIPAddress("1e1.4.5.6") == 'Neither')
assert(validIPAddress("2001:db8:85a3:0::8a2E:0370:7334") == 'Neither')
assert(validIPAddress("1081:db8:85a3:01:-0:8A2E:0370:7334") == 'Neither')



