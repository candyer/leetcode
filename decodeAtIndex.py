# https://leetcode.com/problems/decoded-string-at-index/description/

# 884. Decoded String at Index


# An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one 
# character at a time and the following steps are taken:

# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
# Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

# Example 1:
# Input: S = "leet2code3", K = 10
# Output: "o"
# Explanation: 
# The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10th letter in the string is "o".

# Example 2:
# Input: S = "ha22", K = 5
# Output: "h"
# Explanation: 
# The decoded string is "hahahaha".  The 5th letter is "h".

# Example 3:
# Input: S = "a2345678999999999999999", K = 1
# Output: "a"
# Explanation: 
# The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
 
# Note:
# 2 <= S.length <= 100
# S will only contain lowercase letters and digits 2 through 9.
# S starts with a letter.
# 1 <= K <= 10^9
# The decoded string is guaranteed to have less than 2^63 letters.



# def decodeAtIndex(S, K):
# 	"""
# 	:type S: str
# 	:type K: int
# 	:rtype: str
# 	"""
# 	count = 0
# 	tmp = []
# 	for c in S:
# 		if K <= count:
# 			return tmp[K - 1]
# 		if c.isalpha():
# 			tmp.append(c)
# 			count += 1
# 		else:
# 			tmp *= int(c)
# 			count *= int(c)
# 		print tmp
# 	return 111, #tmp[K - 1]	


def decodeAtIndex(S, K):
	"""
	:type S: str
	:type K: int
	:rtype: str
	"""
	count = 0
	for c in S:
		if c.isalpha():
			count += 1
		else:
			count *= int(c)
	for c in S[::-1]:
		K %= count
		if K == 0 and c.isalpha():
			return c
		if c.isalpha():
			count -= 1
		else:
			count /= int(c)
			
	   
assert decodeAtIndex("leet2code3", 10) == 'o'
assert decodeAtIndex("ha22", 5) == 'h'
assert decodeAtIndex("a2345678999999999999999", 99999999) == 'a'

































