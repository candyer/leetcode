# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/

# 1128. Number of Equivalent Domino Pairs


# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if 
# either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 
# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
 

# Constraints:
# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9

from collections import defaultdict
def numEquivDominoPairs(dominoes):
	"""
	:type dominoes: List[List[int]]
	:rtype: int
	"""
	d = defaultdict(int)
	for a, b in dominoes:
		if a > b:
			a, b = b, a
		d[(a, b)] += 1

	res = 0
	for val in d.values():
		if val > 1:
			res += val * (val - 1) / 2
	return res


assert numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6],[6,5],[5,6]]) == 4
assert numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]) == 1
assert numEquivDominoPairs([[1,2]]) == 0