# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3698/


# Minimum Operations to Make Array Equal


# You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

# In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and 
# add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. 
# It is guaranteed that all the elements of the array can be made equal using some operations.

# Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

 
# Example 1:
# Input: n = 3
# Output: 2
# Explanation: arr = [1, 3, 5]
# First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
# In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

# Example 2:
# Input: n = 6
# Output: 9
 

# Constraints:
# 1 <= n <= 10^4



def minOperations(n: int) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if n % 2:
        return sum(range(2, n, 2))
    else:
        return sum(range(1, n, 2))


def minOperations(n: int) -> int:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    half = n // 2
    return half * (n - half)


def minOperations(n: int) -> int:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return n * n // 4
    

assert(minOperations(3) == 2)
assert(minOperations(6) == 9)
assert(minOperations(7) == 12)





