# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/


# Valid Mountain Array


# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < A[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
 

# Constraints:
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4


from typing import List
def validMountainArray(arr: List[int]) -> bool:
    n = len(arr)
    if n < 3:
        return False
    pos = arr.index(max(arr))
    if pos in [0, n - 1]:
        return False
    for i in range(pos - 1):
        if arr[i] >= arr[i + 1]:
            return False
    for i in range(pos, n - 1):
        if arr[i] <= arr[i + 1]:
            return False
    return True



from typing import List
def validMountainArray(arr: List[int]) -> bool:
        n = len(arr)
        if n < 3 or arr[0] > arr[1]:
            return False
        up = True
        for i in range(1, n):
            if up:
                if arr[i - 1] >= arr[i]:
                    up = False
            if not up:
                if arr[i - 1] <= arr[i]:
                    return False
        return not up

assert(validMountainArray([2,1]) == False)
assert(validMountainArray([3,5,5]) == False)
assert(validMountainArray([0,3,2,1]) == True)
assert(validMountainArray([0,1,2,1]) == True)
assert(validMountainArray([0,1,2,3]) == False)
assert(validMountainArray([4,3,2,1]) == False)





