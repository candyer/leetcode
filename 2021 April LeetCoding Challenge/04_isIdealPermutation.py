# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3697/

# Global and Local Inversions


# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
# Return true if and only if the number of global inversions is equal to the number of local inversions.


# Example 1:
# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.

# Example 2:
# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.


# Note:
# A will be a permutation of [0, 1, ..., A.length - 1].
# A will have length in range [1, 5000].
# The time limit for this problem has been reduced.

from typing import List
def isIdealPermutation(A: List[int]) -> bool:
    n = len(A)
    maxi = -1
    for i in range(n - 2):
        maxi = max(maxi, A[i])
        if maxi > A[i + 2]:
            return False
    return True


assert(isIdealPermutation([1,0,2]) == True)
assert(isIdealPermutation([1,2,0]) == False)
assert(isIdealPermutation([3,2,4,1,0]) == False)


