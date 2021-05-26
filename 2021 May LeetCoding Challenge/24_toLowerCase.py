# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3754/


# To Lower Case


# Given a string s, 
# return the string after replacing every uppercase letter with the same lowercase letter.

# Example 1:
# Input: s = "Hello"
# Output: "hello"

# Example 2:
# Input: s = "here"
# Output: "here"

# Example 3:
# Input: s = "LOVELY"
# Output: "lovely"
 

# Constraints:
# 1 <= s.length <= 100
# s consists of printable ASCII characters.

from string import ascii_lowercase, ascii_uppercase
def toLowerCase(s: str) -> str:
	d = dict(zip(ascii_uppercase, ascii_lowercase))
	res = []
	for c in s:
		if c in d:
			res.append(d[c])
		else:
			res.append(c)
	return ''.join(res)


	d = dict(zip(ascii_uppercase, ascii_lowercase))
	return "".join(d[c] if c in d else c for c in s)

def toLowerCase(s: str) -> str:
	res = []
	for c in s:
		if 65 <= ord(c) <= 90:
			res.append(chr(ord(c) + 32))
		else:
			res.append(c)
	return ''.join(res)
	
	return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in s)

def toLowerCase(s: str) -> str:
	return s.lower()

assert(toLowerCase("Hello") == 'hello')
assert(toLowerCase("here") == 'here')
assert(toLowerCase("LOVELY") == 'lovely')







