# https://leetcode.com/problems/partition-labels/description/

# 763. Partition Labels

# A string S of lowercase letters is given. We want to partition this string into as 
# many parts as possible so that each letter appears in at most one part, and return 
# a list of integers representing the size of these parts.

# Example 1:   Input: S = "ababcbacadefegdehijhklij"    Output: [9,7,8]

# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, 
# because it splits S into less parts.

# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.


from collections import defaultdict
def partitionLabels(S):
	"""
	:type S: str
	:rtype: List[int]
	"""
	d = defaultdict(list)
	n = len(S)
	for i in range(n):
		d[S[i]].append(i)
	i = 0
	res = []
	while i < n:
		end = d[S[i]][-1]
		j = i + 1
		while j < end:
			if d[S[j]][-1] > end:
				end = d[S[j]][-1]
			j += 1
		res.append(end - i + 1)
		i = end
		i += 1
	return res


assert partitionLabels('ababfcbacadefegdehijhklij') == [17, 8]
assert partitionLabels('ababcbacadefegdehijhklij') == [9,7,8]
assert partitionLabels('ababcbacadefegdehijhklija') == [25]

