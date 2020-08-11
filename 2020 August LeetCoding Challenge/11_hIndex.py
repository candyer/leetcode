# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3420/

# H-Index
# Given an array of citations (each citation is a non-negative integer) of a researcher, 
# write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of 
# his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# Example:
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
#              received 3, 0, 6, 1, 5 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.
# Note: If there are several possible values for h, the maximum one is taken as the h-index.


from typing import List
def hIndex(citations: List[int]) -> int:
	for i, c in enumerate(sorted(citations, reverse=True)):
		if i >= c:
			return i
	return len(citations)


assert(hIndex([3,0,6,1,5]) == 3)
assert(hIndex([2,0,6,1,5]) == 2)
assert(hIndex([0,0,0,0,1]) == 1)
assert(hIndex([0,0,0,0,0]) == 0)
assert(hIndex([1,2,3,4]) == 2)
assert(hIndex([100, 100, 100, 100]) == 4)



