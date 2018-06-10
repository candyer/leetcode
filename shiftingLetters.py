# https://leetcode.com/problems/shifting-letters/description/

# 848. Shifting Letters

# We have a string S of lowercase letters, and an integer array shifts.

# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

# Return the final string after all such shifts to S are applied.

# Example 1:
# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"

# Explanation: 
# We start with "abc".
# After shifting the first 1 letters of S by 3, we have "dbc".
# After shifting the first 2 letters of S by 5, we have "igc".
# After shifting the first 3 letters of S by 9, we have "rpl", the answer.

# Note:
# 1 <= S.length = shifts.length <= 20000
# 0 <= shifts[i] <= 10 ^ 9


def shiftingLetters(S, shifts):
	"""
	:type S: str
	:type shifts: List[int]
	:rtype: str
	"""
	n = len(S)
	shifts[-1] %= 26
	for i in range(n - 2, -1, -1):
		shifts[i] += shifts[i + 1]
		shifts[i] %= 26

	res = [''] * n
	for i, (c, num) in enumerate(zip(S, shifts)):
		if (ord(c) + num) > 122:
			res[i] = chr(97 + (ord(c) + num) - 122 - 1)
		else:
			res[i] = chr((ord(c) + num))
	return ''.join(res)


assert shiftingLetters("abc", [3,5,9]) == 'rpl'
assert shiftingLetters("abc", [1,50,90]) == 'llo'
assert shiftingLetters("azt", [1234567, 987654, 45671234]) == 'zpr'

from random import randint as r
from random import choice as c

n = r(1, 10)
S = []
shifts = []
for i in range(n):
	S.append(c('abcdefghijklmnopqrstuvwxyz'))
	shifts.append(r(1, 1000000000))
S = ''.join(S)

print S, shifts
print shiftingLetters(S, shifts)



