# https://leetcode.com/contest/weekly-contest-140/problems/letter-tile-possibilities/

# 1079. Letter Tile Possibilities

# You have a set of tiles, where each tile has one letter tiles[i] printed on it.  
# Return the number of possible non-empty sequences of letters you can make.

# Example 1:
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

# Example 2:
# Input: "AAABBC"
# Output: 188
 
# Note:
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

from itertools import permutations as p
def numTilePossibilities(tiles):
	"""
	:type tiles: str
	:rtype: int
	"""
	res = 0
	for i in range(1, len(tiles) + 1):
		res += len(set(p(tiles, i)))
	return res

assert numTilePossibilities("AAB") == 8
assert numTilePossibilities("AAABBC") == 188
assert numTilePossibilities("ABCDEF") == 1956

