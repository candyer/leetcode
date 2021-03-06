# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/

# Find All Anagrams in a String


# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s 
# and p will not be larger than 20,100.

# The order of output does not matter.


# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


from typing import List
from collections import Counter
def findAnagrams(s: str, p: str) -> List[int]:
	dp = Counter(p)
	ds = Counter()
	n = len(p)
	res = []
	count = 0
	for i in range(len(s)):
		ds[s[i]] += 1
		count += 1

		if count > n:
			if ds[s[i - n]] > 1:
				ds[s[i - n]] -= 1
			else:
				ds.pop(s[i - n])
			count -= 1

		if count == n:
			if ds == dp:
				res.append(i - n + 1)

	return res


assert(findAnagrams("cbaebabacd", "abc") == [0, 6])
assert(findAnagrams("abab", "ab") == [0, 1, 2])



