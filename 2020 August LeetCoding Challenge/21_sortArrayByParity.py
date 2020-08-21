# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3431/

# Sort Array By Parity

# Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
# followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

 
# Example 1:
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

# Note:
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000


##################################################
from typing import List
def sortArrayByParity(A: List[int]) -> List[int]:
	even, odd = [], []
	for num in A:
		if num % 2:
			odd.append(num)
		else:
			even.append(num)
	return even + odd


##################################################
def sortArrayByParity(A: List[int]) -> List[int]:
	return sorted(A, key=lambda x: x%2)


assert(sortArrayByParity([3, 1, 2, 4]) == [2, 4, 3, 1])

