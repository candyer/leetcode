# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3682/

# 3Sum With Multiplicity


# Given an integer array arr, and an integer target, return the number of tuples i, j, k 
# such that i < j < k and arr[i] + arr[j] + arr[k] == target.
# As the answer can be very large, return it modulo 109 + 7.

 
# Example 1:
# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.

# Example 2:
# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
 

# Constraints:
# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300

from typing import List
from collections import Counter

def threeSumMulti(arr: List[int], target: int) -> int:
    mod = 10**9 + 7
    counts = Counter(arr)
    res = 0
    for a in counts:
        for b in counts:
            if a <= b:
                c = target - a - b
                # a <= b <= c
                if a == b == c: #combinations(counts[c], 3)
                    res += counts[a] * (counts[a] - 1) * (counts[a] - 2) // 6
                elif a == b != c: #combinations(counts[a], 2) * combinations(counts[c], 1)
                    res += counts[a] * (counts[a] - 1) // 2 * counts[c] 
                elif c > a and c > b: #combinations(counts[a], 1) * combinations(counts[b], 1) * combinations(counts[c], 1)
                    res += counts[a] * counts[b] * counts[c]
    return res % mod


assert(threeSumMulti([1,1,2,2,3,3,4,4,5,5], target = 8) == 20)
assert(threeSumMulti([1,1,2,2,2,2], target = 5) == 12)

