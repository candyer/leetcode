# https://leetcode.com/problems/positions-of-large-groups/description/


# 830. Positions of Large Groups

# In a string S of lowercase letters, these letters form consecutive groups of the same character.

# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

# Call a group large if it has 3 or more characters.  We would like the starting and ending 
# positions of every large group.

# The final answer should be in lexicographic order.

# Example 1:

# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# Example 2:

# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# Example 3:

# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
 
# Note:  1 <= S.length <= 1000


def largeGroupPositions(S):
	"""
	:type S: str
	:rtype: List[List[int]]
	"""
	res = []
	n = len(S)
	S += '0'
	i = 0
	while i < n:
		count = 1
		j = i + 1
		while S[j] == S[i]:
			count += 1
			j += 1
		if count >= 3:
			res.append([i, j - 1])
		i += count
	return res

assert largeGroupPositions("abbxxxxzzy") == [[3, 6]]
assert largeGroupPositions("abc") == []
assert largeGroupPositions("abcdddeeeeaabbbcd") == [[3, 5], [6, 9], [12, 14]]
assert largeGroupPositions("aaaa") == [[0, 3]]






