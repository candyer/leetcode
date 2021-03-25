# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3683/

# Advantage Shuffle


# Given two arrays A and B of equal size, the advantage of A with respect to B is the number of 
# indices i for which A[i] > B[i].
# Return any permutation of A that maximizes its advantage with respect to B.


# Example 1:
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]

# Example 2:
# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
 

# Note:
# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9


from typing import List
from collections import defaultdict

def advantageCount(A, B):
    n = len(A)
    A.sort()
    match = defaultdict(list)
    notMatch = []
    i = 0
    for b in sorted(B):
        while i < n and b >= A[i]:
            notMatch.append(A[i])
            i += 1
        if i < n:
            match[b].append(A[i])
        i += 1
    return [(match[b] or notMatch).pop() for b in B]

assert(advantageCount([2,7,11,15], [1,10,4,11]) == [2,11,7,15])
assert(advantageCount([12,24,8,32], [13,25,32,11]) == [24,32,8,12])
assert(advantageCount([1,2,10, 17, 20], [3,4,5,7,10]) == [10, 17, 20, 2, 1])
assert(advantageCount([1,2,6,6,8,11], [3,4,5,6,7,12]) == [6, 6, 8, 11, 2, 1])
assert(advantageCount([1,2,3], [7, 8, 9]) == [3, 2, 1])
assert(advantageCount([8,4,0,2,4], [7,6,3,4,10]) == [4, 2, 4, 8, 0])
assert(advantageCount([3,6,0,5,2], [2,5,2,1,5]) == [5, 6, 3, 2, 0])
assert(advantageCount([2,5,4,1,8], [4,1,5,8,2]) == [5, 2, 8, 1, 4])
assert(advantageCount([1,2,4,5,6], [3,5,7,10,17]) == [4, 6, 5, 2, 1])



