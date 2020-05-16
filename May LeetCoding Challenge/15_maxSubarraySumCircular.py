# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/


# Maximum Sum Circular Subarray


# Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

# Here, a circular array means the end of the array connects to the beginning of the array.  
# (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

# Also, a subarray may only include each element of the fixed buffer A at most once.  
# (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.
# 	length = k2 % A.length.)

 
# Example 1:
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3

# Example 2:
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

# Example 3:
# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

# Example 4:
# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

# Example 5:
# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
 

# Note:
# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000


def maxSubarraySumCircular(A):
	cur_maxi, cur_min, maxi, mini = 0, 0, float('-inf'), float('inf')
	for num in A:
		cur_maxi = max(cur_maxi + num, num)
		cur_min = min(cur_min + num, num)
		maxi = max(maxi, cur_maxi)
		mini = min(mini, cur_min)
	if maxi > 0:
		return max(maxi, sum(A) - mini)
	return maxi


assert(maxSubarraySumCircular([3, -3, -2, 3, -1, 3]) == 8)
assert(maxSubarraySumCircular([-1,-2,-3,-2]) == -1)
assert(maxSubarraySumCircular([1,-2,3,-2]) == 3)
assert(maxSubarraySumCircular([5,-3,5]) == 10)
assert(maxSubarraySumCircular([3,-1,2,-1]) == 4)
assert(maxSubarraySumCircular([3,-2,2,-3]) == 3)
assert(maxSubarraySumCircular([-2,-3,-1]) == -1)
assert(maxSubarraySumCircular([1, 2, 3, 4, 5, 6]) == 21)





