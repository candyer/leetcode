# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

# 599. Minimum Index Sum of Two Lists


# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, 
# output all of them with no order requirement. You could assume there always exists an answer.


# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.

from collections import defaultdict
def findRestaurant(list1, list2):
	"""
	:type list1: List[str]
	:type list2: List[str]
	:rtype: List[str]
	"""
	d = defaultdict(list)
	for idx, restaurant in enumerate(list1):
		d[restaurant].append(idx)
	for idx, restaurant in enumerate(list2):
		d[restaurant].append(idx)
	index_sum = float('inf')
	res = []
	d2 = defaultdict(list)
	for restaurant, indexs in d.items():
		if len(indexs) > 1:
			d2[sum(indexs)].append(restaurant)
	if d2:
		return d2[min(d2.keys())]
	else:
		return []



assert findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], 
					 ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) == ['Shogun']
assert findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], 
					 ["KFC", "Shogun", "Burger King"]) == ['Shogun']
assert findRestaurant(["Burger King","Shogun","KFC"], 
					 ["KFC", "Shogun", "Burger King"]) == ['Shogun', 'KFC', 'Burger King']
assert findRestaurant(["zs","KFC"], 
					 ["zs","koabb","KFC"]) == ['zs']
assert findRestaurant([], 
					 ["zs","koabb","KFC"]) == []



