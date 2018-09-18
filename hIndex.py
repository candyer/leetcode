# https://leetcode.com/problems/h-index/description/


# 274. H-Index

# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, 
# and the other N - h papers have no more than h citations each."

# Example:

# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
#              received 3, 0, 6, 1, 5 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.
# Note: If there are several possible values for h, the maximum one is taken as the h-index.



def hIndex(citations):
	"""
	:type citations: List[int]
	:rtype: int
	"""
	n = len(citations)
	citations.sort(reverse=True)
	if not citations or citations[0] == 0:
		return 0
	for i, c in enumerate(citations):
		if i >= c:
			return i
	return n 


assert hIndex([3,0,6,1,5]) == 3
assert hIndex([1,2,2,4,5]) == 2
assert hIndex([1,1,5,6]) == 2
assert hIndex([1]) == 1
assert hIndex([200, 300]) == 2
assert hIndex([900, 20, 5, 100]) == 4
assert hIndex([900,900, 900]) == 3
assert hIndex([0, 0, 0, 0]) == 0
assert hIndex([0, 100, 200]) == 2
assert hIndex([]) == 0










