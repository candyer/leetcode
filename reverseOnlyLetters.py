# https://leetcode.com/problems/reverse-only-letters/description/

# 917. Reverse Only Letters


# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, 
# and all letters reverse their positions.

 
# Example 1:
# Input: "ab-cd"
# Output: "dc-ba"

# Example 2:
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

# Example 3:
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
 
# Note:
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "



def reverseOnlyLetters(S):
	"""
	:type S: str
	:rtype: str
	"""
	n = len(S)
	letters = []
	for c in S:
		if c.isalpha():
			letters.append(c)

	letters.reverse()
	res = list(S)
	j = 0
	for i in range(n):
		if res[i].isalpha():
			res[i] = letters[j]
			j += 1
	return ''.join(res)
	

assert reverseOnlyLetters("123j") == '123j'
assert reverseOnlyLetters("ab-cd") == "dc-ba"
assert reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
assert reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"



