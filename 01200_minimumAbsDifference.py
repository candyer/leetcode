# https://leetcode.com/problems/minimum-absolute-difference/description/

# 1200. Minimum Absolute Difference

# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

# Example 2:
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]

# Example 3:
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
 

# Constraints:
# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6


from collections import defaultdict
def minimumAbsDifference(arr):
	"""
	:type arr: List[int]
	:rtype: List[List[int]]
	"""
	arr.sort()
	d = defaultdict(list)
	mini = float('inf')
	n = len(arr)
	for i in range(n - 1):
		diff = abs(arr[i] - arr[i + 1])
		d[diff].append([arr[i], arr[i + 1]])
		mini = min(mini, diff)
	return d[mini]
	
assert minimumAbsDifference([4,2,1,3]) == [[1, 2], [2, 3], [3, 4]]
assert minimumAbsDifference([1,3,6,10,15]) == [[1, 3]]
assert minimumAbsDifference([3,8,-10,23,19,-4,-14,27]) == [[-14, -10], [19, 23], [23, 27]]


