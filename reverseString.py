# https://leetcode.com/problems/reverse-string/description/
# Leetcode 344 -- Reverse String

# Write a function that takes a string as input and returns the string reversed.
# Example: Given s = "hello", return "olleh".

def reverseString(s):
	"""
	:type s: str
	:rtype: str
	"""  
	#solution 1
	return s[::-1]

	#solution 2
	return "".join(reversed(list(s)))


print reverseString("hello") # "olleh"
print reverseString("h") # "h"
print reverseString("") # ""
print reverseString("apple") # "elppa"
