# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3644/

# Arithmetic Slices


# A sequence of numbers is called arithmetic if it consists of at least three elements and 
# if the difference between any two consecutive elements is the same.

# For example, these are arithmetic sequences:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9

# The following sequence is not arithmetic.
# 1, 1, 2, 5, 7
 
# A zero-indexed array A consisting of N numbers is given. A slice of that array is any 
# pair of integers (P, Q) such that 0 <= P < Q < N.

# A slice (P, Q) of the array A is called arithmetic if the sequence:
# A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
# The function should return the number of arithmetic slices in the array A.


# Example:
# A = [1, 2, 3, 4]
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

from typing import List
def numberOfArithmeticSlices(A: List[int]) -> int:
    n = len(A)
    dp = [0] * n
    for i in range(2, n):
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            dp[i] = dp[i - 1] + 1
    return sum(dp)


assert(numberOfArithmeticSlices([1,2,3,4]) == 3)
assert(numberOfArithmeticSlices([1,2,3,4,6]) == 3)
assert(numberOfArithmeticSlices([5,3,2,1,3,5]) == 2)



