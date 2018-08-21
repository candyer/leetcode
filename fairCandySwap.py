# https://leetcode.com/problems/fair-candy-swap/description/

# 888. Fair Candy Swap

# Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of 
# candy that Bob has.

# Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  
# (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

# Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob 
# must exchange.

# If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

 
# Example 1:
# Input: A = [1,1], B = [2,2]
# Output: [1,2]

# Example 2:
# Input: A = [1,2], B = [2,3]
# Output: [1,2]

# Example 3:
# Input: A = [2], B = [1,3]
# Output: [2,3]

# Example 4:
# Input: A = [1,2,5], B = [2,4]
# Output: [5,4]
 
# Note:
# 1 <= A.length <= 10000
# 1 <= B.length <= 10000
# 1 <= A[i] <= 100000
# 1 <= B[i] <= 100000
# It is guaranteed that Alice and Bob have different total amounts of candy.
# It is guaranteed there exists an answer.


############################
##### brute force, TLE #####
############################
def fairCandySwap(A, B):
	"""
	:type A: List[int]
	:type B: List[int]
	:rtype: List[int]
	"""
	total_a, total_b = sum(A), sum(B)
	A.sort()
	B.sort()
	if total_a > total_b:
		diff = (total_a - total_b) / 2
		for i in A:
			for j in B:
				if i - j == diff:
					return [i, j]
	else:
		diff = (total_b - total_a) / 2
		for i in A:
			for j in B:
				if j - i == diff:
					return [i, j]



############################
##### binary search AC #####
############################
def fairCandySwap(A, B):
	"""
	:type A: List[int]
	:type B: List[int]
	:rtype: List[int]
	"""
	total_a, total_b = sum(A), sum(B)
	diff = (total_b - total_a) / 2
	B.sort()
	for num in A:
		low, high = 0, len(B) - 1
		while low <= high:
			mid = (low + high) / 2
			if num + diff == B[mid]:
				return [num, B[mid]]
			elif num + diff < B[mid]:
				high = mid - 1
			else:
				low = mid + 1



def fairCandySwap(A, B):
	"""
	:type A: List[int]
	:type B: List[int]
	:rtype: List[int]
	"""
	total_a, total_b = sum(A), sum(B)
	diff = (total_b - total_a) / 2
	b = set(B)
	for num in A:
		if num + diff in b:
			return [num, num + diff]



assert fairCandySwap([1,1], [2,2]) == [1, 2]
assert fairCandySwap([1,2], [2,3]) == [1, 2]
assert fairCandySwap([2], [1,3]) == [2, 3]
assert fairCandySwap([1,2,5], [2,4]) == [5, 4]
assert fairCandySwap([2,3,3,4,8], [1,1,3,5]) == [8,3]



















