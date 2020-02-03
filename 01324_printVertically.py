# https://leetcode.com/problems/print-words-vertically/description/

# 1324. Print Words Vertically


# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word.

# Example 1:
# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]
# Explanation: Each word is printed vertically. 
#  "HAY"
#  "ORO"
#  "WEU"

# Example 2:
# Input: s = "TO BE OR NOT TO BE"
# Output: ["TBONTB","OEROOE","   T"]
# Explanation: Trailing spaces is not allowed. 
# "TBONTB"
# "OEROOE"
# "   T"

# Example 3:
# Input: s = "CONTEST IS COMING"
# Output: ["CIC","OSO","N M","T I","E N","S G","T"]
 
# Constraints:
# 1 <= s.length <= 200
# s contains only upper case English letters.
# It's guaranteed that there is only one space between 2 words.

from typing import List
def printVertically(s: str) -> List[str]:
	arr = s.split()
	row = len(arr)
	col = len(max(arr, key=len))
	res = [['' for c in range(row)] for r in range(col)]
	
	for r in range(row):
		m = len(arr[r])
		if m < col:
			arr[r] = arr[r] + ' ' * (col - m)

	for i in range(col):
		for j in range(row):
			res[i][j] = arr[j][i]

	for i in range(col):
		res[i] = ''.join(res[i]).rstrip()

	return res

assert(printVertically("HOW ARE YOU") == ["HAY","ORO","WEU"])
assert(printVertically("TO BE OR NOT TO BE") == ["TBONTB","OEROOE","   T"])
assert(printVertically("CONTEST IS COMING") == ["CIC","OSO","N M","T I","E N","S G","T"])









