# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3448/

# Partition Labels

# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible 
# so that each letter appears in at most one part, and return a list of integers representing the size of these parts.


# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


# Note:
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.


from typing import List
from collections import defaultdict
def partitionLabels(S: str) -> List[int]:
	n = len(S)
	reversed_s = S[::-1]
	d = defaultdict(list)
	for c in set(S):
		d[c].extend([S.index(c), n - reversed_s.index(c) - 1])
	vals = sorted(d.values())
	start, end = vals[0]
	res = []
	for l, r in vals[1:]:
		if start <= l < end:
			end = max(end, r)
		elif end < l:
			res.append(end - start + 1)
			start, end = l, r
	res.append(end - start + 1)
	return res


assert(partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8])
assert(partitionLabels("aaaab") == [4, 1])
assert(partitionLabels("ababcbab") == [8])
assert(partitionLabels("a") == [1])



