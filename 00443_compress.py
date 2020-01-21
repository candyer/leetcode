# https://leetcode.com/problems/string-compression/description/

# 443. String Compression

# Given an array of characters, compress it in-place. 
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.

# Follow up:
# Could you solve it using only O(1) extra space?

# Example 1:
# Input: ["a","a","b","b","c","c","c"]
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

# Example 2:
# Input: ["a"]
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# Explanation:
# Nothing is replaced.

# Example 3:
# Input: ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.

# Note:
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.

from typing import List
def compress(chars: List[str]) -> int:
	pre = chars[0]
	n = len(chars)
	count = 0
	pos = 0
	for char in chars:
		if pre == char:
			count += 1
		else:
			chars[pos] = pre
			pos += 1
			if count > 1:
				for c in str(count):
					chars[pos] = c
					pos += 1
			pre = char
			count = 1

	chars[pos] = pre
	pos += 1	
	if count > 1:
		for c in str(count):
			chars[pos] = c
			pos += 1
	return pos
	
assert(compress(["a","b","b","b","b","b","b"]) == 3)
assert(compress(["a","b","b","b","b","b","z"]) == 4)
assert(compress(["a","a","b","b","c","c","c"]) == 6)
assert(compress(["a","a","b","b","c","c","z"]) == 7)
assert(compress(["a"]) == 1)
assert(compress(["a", "b"]) == 2)
assert(compress(["a", "a"]) == 2)
assert(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4)
assert(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b","z"]) == 5)





