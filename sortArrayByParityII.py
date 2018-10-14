# https://leetcode.com/problems/sort-array-by-parity-ii/description/


# 922. Sort Array By Parity II

# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.

# Example 1:
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 
# Note:
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000


def sortArrayByParityII(A):
	"""
	:type A: List[int]
	:rtype: List[int]
	"""

	even = []
	odd = []
	for num in A:
		if num % 2:
			odd.append(num)
		else:
			even.append(num)
	res = []
	odd_index = even_index = 0
	for i in range(len(A)):
		if i % 2 == 0:
			res.append(even[even_index])
			even_index += 1
		else:
			res.append(odd[odd_index])
			odd_index += 1
	return res

assert sortArrayByParityII([4,2,5,7]) == [4, 5, 2, 7]
assert sortArrayByParityII([1,3,5,7,2,4,6,8]) == [2, 1, 4, 3, 6, 5, 8, 7]


