# https://leetcode.com/problems/top-k-frequent-elements/description/

# 347. Top K Frequent Elements

# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Note:
# You may assume k is always valid, 1 <= k <= number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

#################
## solution 1 ###
#################
from collections import Counter as c
def topKFrequent(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: List[int]
	"""

	count = []
	for key, val in c(nums).items():
		count.append([val, key])
	
	count.sort(reverse=True)
	res = []
	i = 0
	while i < k:
		res.append(count[i][1])
		i += 1
	return res



#################
## solution 2###
#################
from collections import Counter as c
def topKFrequent(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: List[int]
	"""

	return [num for num, count in c(nums).most_common(k)]


assert topKFrequent([1,1,1,2,2,3], 2) == [1, 2]
assert topKFrequent([1], 1) == [1]



