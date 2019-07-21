# https://leetcode.com/problems/maximum-of-absolute-value-expression/description/

# 1131. Maximum of Absolute Value Expression


# Given two arrays of integers with equal lengths, return the maximum value of:
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# where the maximum is taken over all 0 <= i, j < arr1.length.

# Example 1:
# Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
# Output: 13

# Example 2:
# Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
# Output: 20

# Constraints:
# 2 <= arr1.length == arr2.length <= 40000
# -10^6 <= arr1[i], arr2[i] <= 10^6


#brute force, TLE
# def maxAbsValExpr(arr1, arr2):
# 	"""
# 	:type arr1: List[int]
# 	:type arr2: List[int]
# 	:rtype: int
# 	"""
# 	n = len(arr1)
# 	res = 0
# 	for i in range(n - 1):
# 		for j in range(i + 1, n):
# 			tmp = abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j)
# 			print i, j, tmp
# 			res = max(res, tmp)
# 	return res


def maxAbsValExpr(arr1, arr2):
	"""
	:type arr1: List[int]
	:type arr2: List[int]
	:rtype: int
	"""
	n = len(arr1)
	mini1 = mini2 = mini3 = mini4 = float('inf')
	maxi1 = maxi2 = maxi3 = maxi4 = 0
	for i in range(n):
		a = arr1[i] + arr2[i] + i
	 	b = arr1[i] + arr2[i] - i
		c = arr1[i] - arr2[i] + i
		d = arr1[i] - arr2[i] - i

		mini1 = min(mini1, a)
		mini2 = min(mini2, b)
		mini3 = min(mini3, c)
		mini4 = min(mini4, d)

		maxi1 = max(maxi1, a)
		maxi2 = max(maxi2, b)
		maxi3 = max(maxi3, c)
		maxi4 = max(maxi4, d)
	return max(maxi1 - mini1, maxi2 - mini2, maxi3 - mini3, maxi4 - mini4)


assert maxAbsValExpr([1,2,3,4], [-1,4,5,6]) == 13
assert maxAbsValExpr([1,-2,-5,0,10], [0,-2,-1,-7,-4]) == 20


