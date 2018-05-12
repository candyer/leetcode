# https://leetcode.com/problems/goat-latin/description/

# 824. Goat Latin


# A sentence S is given, composed of words separated by spaces. Each word consists of lowercase 
# and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

# The rules of Goat Latin are as follows:

# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
# For example, the word 'apple' becomes 'applema'.
 
# If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to 
# the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
 
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the 
# end and so on.
# Return the final sentence representing the conversion from S to Goat Latin. 

 
# Example 1:

# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
# Example 2:

# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa 
# azylmaaaaaaaaa ogdmaaaaaaaaaa"
 
# Notes:

# S contains only uppercase, lowercase and spaces. Exactly one space between each word.
# 1 <= S.length <= 150.


def convert(i, word):
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	word = list(word)
	if not word[0] in vowels:
		beginning = word.pop(0)
		word.append(beginning)
	word.extend(['ma'] + ['a'] * (i + 1))
	return ''.join(word)


def toGoatLatin(S):
	"""
	:type S: str
	:rtype: str
	"""
	res = []
	S = S.split()
	n = len(S)
	for i in range(n):
		res.append(convert(i, S[i]))
	return ' '.join(res)

assert toGoatLatin("I speak Goat Latin") == 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'
assert toGoatLatin("The quick brown fox jumped over the lazy dog") == \
'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa'
assert toGoatLatin("Each word consists of lowercase and uppercase letters only") == \
'Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa'




















