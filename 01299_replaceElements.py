# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

# 1299. Replace Elements with Greatest Element on Right Side

# Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
# and replace the last element with -1.
# After doing so, return the array.
 

# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
 

# Constraints:
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5

# from typing import List
# def replaceElements(arr: List[int]) -> List[int]:
# 	print()
# 	n = len(arr)
# 	res = []
# 	for i in range(n - 1):
# 		print(max(arr[i+1:]))
# 		res.append(max(arr[i+1:]))
# 	return res + [-1]

from typing import List
def replaceElements(arr: List[int]) -> List[int]:
	n = len(arr)
	res = [-1] * n
	for i in range(n - 1, 0, -1):
		if arr[i] > res[i]:
			res[i - 1] = arr[i]
		else:
			res[i - 1] = res[i]
	return res


assert(replaceElements([17,18,5,4,6,1]) == [18, 6, 6, 6, 1, -1])
assert(replaceElements([5,4,3,2,1]) == [4, 3, 2, 1, -1])
assert(replaceElements([1]) == [-1])

