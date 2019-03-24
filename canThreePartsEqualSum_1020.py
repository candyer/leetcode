# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/


# 1020. Partition Array Into Three Parts With Equal Sum


# Given an array A of integers, return true if and only if we can partition the array into three non-empty parts 
# with equal sums.

# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + 
# A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 
# Example 1:
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

# Example 2:
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false

# Example 3:
# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 
# Note:
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000

def canThreePartsEqualSum(A):
	"""
	:type A: List[int]
	:rtype: bool
	"""
	total = sum(A)
	if total % 3 != 0:
		return False
	avg = total / 3
	tmp = 0
	count = 0
	running_sum = []
	for num in A:
		tmp += num
		running_sum.append(tmp)

	target = avg
	n = len(A)
	target = avg
	if target in running_sum[:-1]:
		first_pos = running_sum.index(target)
	else:
		return False
	target += avg
	if target in running_sum[first_pos + 1:-1]:
		second_pos = running_sum.index(target)
		return True
	else:
		return False	


assert canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]) == True
assert canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]) == False
assert canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]) == True
assert canThreePartsEqualSum([0,0,0,0,0,0,0,0]) == True
assert canThreePartsEqualSum([1,1,1,0,0,0,0,0]) == True

