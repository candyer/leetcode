# https://leetcode.com/problems/relative-sort-array/description/


# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  
# Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.


# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
 

# Constraints:
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# Each arr2[i] is distinct.
# Each arr2[i] is in arr1.


from collections import Counter as c
def relativeSortArray(arr1, arr2):
	"""
	:type arr1: List[int]
	:type arr2: List[int]
	:rtype: List[int]
	"""
	d = c(arr1)
	res,  not_in_arr2 = [], []
	for num in arr2:
		res.extend([num] * d[num])
		d.pop(num)
	
	for key, val in d.items():
		not_in_arr2.extend([key]*val)
	res.extend(sorted(not_in_arr2))
	return res

assert relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
assert relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31], [2,42,38,0,43,21]) == [2, 42, 38, 0, 43, 21, 5, 7, 12, 12, 13, 23, 24, 24, 27, 29, 30, 31, 33, 48]






