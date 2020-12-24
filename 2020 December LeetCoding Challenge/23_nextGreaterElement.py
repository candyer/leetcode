# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3578/


# Next Greater Element III


# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and 
# is greater in value than n. If no such positive integer exists, return -1.
# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit 
# in 32-bit integer, return -1.


# Example 1:
# Input: n = 12
# Output: 21

# Example 2:
# Input: n = 21
# Output: -1
 

# Constraints:
# 1 <= n <= 2^31 - 1

def nextGreaterElement(n: int) -> int:
    maxi = 2 ** 31
    arr = list(str(n))
    for left in range(len(arr) - 2, -1, -1):
        for right in range(len(arr) - 1, left, -1):
            if arr[left] < arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
                arr[left + 1:] = list(sorted(arr[left + 1:]))
                res = int(''.join(arr))
                if res <= maxi:
                    return res
    return -1


assert(nextGreaterElement(12) == 21)
assert(nextGreaterElement(21) == -1)
assert(nextGreaterElement(6172) == 6217)
assert(nextGreaterElement(1598876) == 1657889)
assert(nextGreaterElement(1487766) == 1646778)
assert(nextGreaterElement(770223) == 770232)
assert(nextGreaterElement(232675) == 232756)
assert(nextGreaterElement(1999999999) == -1)

