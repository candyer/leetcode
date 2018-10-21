# https://leetcode.com/problems/long-pressed-name/description/


# 925. Long Pressed Name

# Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

# Example 1:
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.

# Example 2:
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

# Example 3:
# Input: name = "leelee", typed = "lleeelee"
# Output: true

# Example 4:
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
 
# Note:
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.


def f(name):
	res = []
	name = list(name) + [0]
	n = len(name)
	i = 0
	while i < n - 1:
		j = 1
		while name[i] == name[i + 1]:
			j += 1
			i += 1
		if name[i] != name[i + 1]:
			res.append((name[i], j))
			i += 1
	return res

def isLongPressedName(name, typed):
	"""
	:type name: str
	:type typed: str
	:rtype: bool
	"""
	origin = f(name)
	typed_name = f(typed)
	if len(origin) != len(typed_name):
		return False

	for a, b in zip(origin, typed_name):
		a1, count_a = a
		b1, count_b = b
		if a1 != b1 or count_a > count_b:
			return False
	return True

assert isLongPressedName("alex", "aaleex") == True
assert isLongPressedName("saeed", "ssaaedd") == False
assert isLongPressedName("leelee", "lleeelee") == True
assert isLongPressedName("laiden", "laiden") == True
assert isLongPressedName('box', 'bo') == False
assert isLongPressedName('box', 'boxxa') == False









