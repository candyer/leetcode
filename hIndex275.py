# https://leetcode.com/problems/h-index-ii/description/


# 275. H-Index II


# Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N - h 
# papers have no more than h citations each."

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



def hIndex(citations):
	"""
	:type citations: List[int]
	:rtype: int
	"""
	n = len(citations)
	low, high = 0, n - 1
	while low <= high:
		mid = (low + high) / 2
		if citations[mid] < n - mid:
			low = mid + 1
		else:
			high = mid - 1
	return n - low



assert hIndex([0,1,2,3,5,6]) == 3
assert hIndex([1,1,1,1,1,5,6]) == 2
assert hIndex([]) == 0
assert hIndex([0, 0, 0, 0]) == 0
assert hIndex([0, 100, 200]) == 2
assert hIndex([1,2,2,4,5]) == 2
assert hIndex([1,1,5,6]) == 2
assert hIndex([1]) == 1
assert hIndex([200, 300]) == 2
assert hIndex([900, 20, 5, 100]) == 4
assert hIndex([900,900, 900]) == 3






