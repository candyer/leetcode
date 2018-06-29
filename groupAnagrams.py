# https://leetcode.com/problems/group-anagrams/description/

# 49. Group Anagrams

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.

from collections import defaultdict
def groupAnagrams(strs):
	"""
	:type strs: List[str]
	:rtype: List[List[str]]
	"""
	d = defaultdict(list)
	n = len(strs)
	for i in range(n):
		d[''.join(sorted(strs[i]))].append(i)

	res = []
	for key, vals in d.items():
		tmp = []
		for val in vals:
			tmp.append(strs[val])
		res.append(tmp)
	return res



print groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']]


