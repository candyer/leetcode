# https://leetcode.com/problems/buddy-strings/description/

# 859. Buddy Strings

# Given two strings A and B of lowercase letters, return true if and only 
# if we can swap two letters in A so that the result equals B.

 
# Example 1:
# Input: A = "ab", B = "ba"
# Output: true

# Example 2:
# Input: A = "ab", B = "ab"
# Output: false

# Example 3:
# Input: A = "aa", B = "aa"
# Output: true

# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true

# Example 5:
# Input: A = "", B = "aa"
# Output: false

# Note:
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.



from collections import Counter as c
def buddyStrings(A, B):
	"""
	:type A: str
	:type B: str
	:rtype: bool
	"""
	da = c(A)
	db = c(B)
	if da.keys() != db.keys():
		return False

	count = 0
	mark = False
	for a, b in zip(A,B):
		if a != b:
			count += 1
		else:
			if da[a] != db[b]:
				return False
			elif da[a] >= 2 and db[b] >= 2:
				mark = True

	if count == 2 or count == 0 and mark:
		return True
	return False
	


assert buddyStrings("ab", "ba") == True
assert buddyStrings("ab", "ab") == False
assert buddyStrings("aa", "aa") == True
assert buddyStrings("", "aa") == False
assert buddyStrings("a", "aa") == False
assert buddyStrings("aaaaaaabc", "aaaaaaacb") == True
assert buddyStrings("aaaaaaabc", "aaaaaaacd") == False
assert buddyStrings("acaca", "aacca") == True
assert buddyStrings("acabb", "aacbb") == True









