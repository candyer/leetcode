# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3726/

# Powerful Integers

# Given three integers x, y, and bound, return a list of all the powerful integers 
# that have a value less than or equal to bound.
# An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.
# You may return the answer in any order. In your answer, each value should occur at most once.

 
# Example 1:
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 20 + 30
# 3 = 21 + 30
# 4 = 20 + 31
# 5 = 21 + 31
# 7 = 22 + 31
# 9 = 23 + 30
# 10 = 20 + 32

# Example 2:
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
 

# Constraints:
# 1 <= x, y <= 100
# 0 <= bound <= 10^6

from typing import List
from math import log

def powerfulIntegers(x: int, y: int, bound: int) -> List[int]:
    if bound < 2:
        return []

    m = 2 if x == 1 else int(log(bound) / log(x) + 1)
    n = 2 if y == 1 else int(log(bound) / log(y) + 1)
    res = set()
    for i in range(m):
        for j in range(n):
            p = x**i + y**j
            if p <= bound:
                res.add(p)
            else:
                break
    return res


print(powerfulIntegers(2, 3, 10))
print(powerfulIntegers(3, 5, 15))
print(powerfulIntegers(1, 1, 10))



