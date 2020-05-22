# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/

# Sort Characters By Frequency

# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:
# Input: "tree"
# Output: "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input: "cccaaa"
# Output:"cccaaa"
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input: "Aabb"
# Output: "bbAa"
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

from collections import Counter
def frequencySort(s: str) -> str:
	res = []
	for key, val in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True):
		res.extend([key] * val)
	return ''.join(res)

assert(frequencySort("tree") == 'eetr')
assert(frequencySort("cccaaa") == 'cccaaa')
assert(frequencySort("Aabb") == 'bbAa')