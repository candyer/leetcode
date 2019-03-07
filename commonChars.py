# https://leetcode.com/problems/find-common-characters/description/


# 1002. Find Common Characters

# Given an array A of strings made only from lowercase letters, return a list of all characters that 
# show up in all strings within the list (including duplicates).  For example, if a character occurs 
# 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.


# Example 1:
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: ["cool","lock","cook"]
# Output: ["c","o"]

# Note:
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter


from collections import Counter as c
def commonChars(A):
	"""
	:type A: List[str]
	:rtype: List[str]
	"""
	d = c(A[0])
	for string in A[1:]:
		d1 = c(string)
		d2 = {}
		for key, val in d1.items():
			if key in d:
				d2[key] = min(d[key], d1[key])
		d = d2
	res = []
	for key, val in d.items():
		res.extend([key] * val)
	return res


assert commonChars(["bella","label","roller"]) == ['e', 'l', 'l']
assert commonChars(["cool","lock","cook"]) == ['c', 'o']
assert commonChars(["cool"]) == ['c', 'l', 'o', 'o']


