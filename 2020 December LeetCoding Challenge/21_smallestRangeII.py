# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3573/


# Smallest Range II

# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).
# After this process, we have some array B.
# Return the smallest possible difference between the maximum value of B and the minimum value of B.

# Example 1:
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]

# Example 2:
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]

# Example 3:
# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]
 
# Note:
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000


from typing import List
def smallestRangeII(A: List[int], K: int) -> int:
    A.sort()
    mini, maxi = A[0], A[-1]
    res = maxi - mini
    for i in range(len(A) - 1):
        res = min(res, max(maxi - K, A[i] + K) - min(mini + K, A[i + 1] - K))
    return res


assert(smallestRangeII([1], 0) == 0)
assert(smallestRangeII([0,10], 2) == 6)
assert(smallestRangeII([1,3,6], 3) == 3)
assert(smallestRangeII([1,3,6], 4) == 5)
assert(smallestRangeII([0,0,0,0,0,1], 4) == 1)
assert(smallestRangeII([0,1,2,3,4], 3) == 4)
assert(smallestRangeII([0,1,2,3,4], 100) == 4)
assert(smallestRangeII([7,8,8,5,2], 4) == 5)
assert(smallestRangeII([7,8,8,5,2,17], 10) == 11)
assert(smallestRangeII([1,11,12,17], 7) == 6)
assert(smallestRangeII([1,2,9,17], 7) == 8)
assert(smallestRangeII([2, 7, 9, 12], 7) == 9)



