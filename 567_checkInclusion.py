# https://leetcode.com/contest/leetcode-weekly-contest-30/problems/permutation-in-string/

# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
# In other words, one of the first string's permutations is the substring of the second string.

# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"       Output:True
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"        Output: False

# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].


import collections
def checkInclusion(s1, s2):
	m = len(s1)
	n = len(s2)
	target = collections.Counter(s1)
	current = collections.Counter(s2[:m])
	if current == target:
		return True
	for i in range(n - m):
		if s2[i] in current and current[s2[i]] > 1:
			current[s2[i]] -= 1
		else:
			current.pop(s2[i])
		if s2[i + m] in current:
			current[s2[i + m]] += 1
		else:
			current[s2[i + m]] = 1
		if current == target:
			return True
	return False


print checkInclusion("ab", "eidbaooo") #True
print checkInclusion("adc","dcda") #True
print checkInclusion('oeidbaoowerty', 'eidbaooo') #False
print checkInclusion('oeidbaoo', 'eidbaooo') #True
print checkInclusion('ab', 'eidbaooo') #True
print checkInclusion('ab', 'eidboaoo') #False



