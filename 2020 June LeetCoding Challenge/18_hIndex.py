# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3364/

# H-Index II

# Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, 
# write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at 
# least h citations each, and the other N − h papers have no more than h citations each."

# Example:
# Input: citations = [0,1,3,5,6]
# Output: 3 
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
#              received 0, 1, 3, 5, 6 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.
# Note:
# If there are several possible values for h, the maximum one is taken as the h-index.

# Follow up:
# This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
# Could you solve it in logarithmic time complexity?

from typing import List
def hIndex(citations: List[int]) -> int:
	n = len(citations)
	for i in range(n):
		if n - i <=  citations[i]:
			return n - i
	return 0



def hIndex(citations: List[int]) -> int:
	n = len(citations)
	l, r = 0, n - 1
	while l < r:
		mid = (l + r) // 2
		if citations[mid] < n - mid:
			l = mid + 1
		else:
			r = mid 
	if l <= r and citations[l] >= n - l:
		return n - l
	return 0


assert(hIndex([0, 1, 3, 5, 6]) == 3)
assert(hIndex([2, 6, 8, 10, 11]) == 4)
assert(hIndex([2, 3, 5, 10, 11]) == 3)
assert(hIndex([2, 3, 5, 10, 11]) == 3)
assert(hIndex([100, 100, 100, 100, 100, 100, 100]) == 7)
assert(hIndex([0, 0, 0, 0, 0, 0, 0]) == 0)
assert(hIndex([]) == 0)






