# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3393/

# Top K Frequent Elements

# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.


# from typing import List
# from collections import Counter
# def topKFrequent(nums: List[int], k: int) -> List[int]:
# 	return [k for k, v in sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True)][:k]




from typing import List
from collections import Counter
from  heapq import nlargest
def topKFrequent(nums: List[int], k: int) -> List[int]:
	d = Counter(nums)
	return nlargest(k, d.keys(), key=d.get) 


assert(topKFrequent([1,1,1,2,2,3], 2) == [1, 2])
assert(topKFrequent([1], 1) == [1])



