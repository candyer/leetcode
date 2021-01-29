# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3619/


# Smallest String With A Given Numeric Value

# The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, 
# so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

# The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' 
# numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

# You are given two integers n and k. Return the lexicographically smallest string with length equal to n 
# and numeric value equal to k.

# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, 
# that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes 
# before y[i] in alphabetic order.


# Example 1:
# Input: n = 3, k = 27
# Output: "aay"
# Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string 
# with such a value and length equal to 3.

# Example 2:
# Input: n = 5, k = 73
# Output: "aaszz"

# Constraints:
# 1 <= n <= 10^5
# n <= k <= 26 * n


def getSmallestString(n: int, k: int) -> str:
    res = ['a'] * n
    for i in range(n - 1, -1, -1):
        if i + 1 == k:
            break
        cur_max_val = min(k - i, 26)
        res[i] = chr(ord('a') + cur_max_val - 1)
        k -= cur_max_val
    return ''.join(res)



##########################################################################################
#the result will start with 'a's, end with 'z's, with at most one other letter in between.
##########################################################################################
def getSmallestString(n: int, k: int) -> str:
    num_z = (k - n) // 25
    if num_z == n:
        return 'z' * n
    num_a = n - num_z - 1
    mid = k - num_a - num_z * 26
    return ''.join(['a'] * num_a + [chr(ord('a') + mid - 1)] +  ['z'] * num_z)


assert(getSmallestString(3, 27) == 'aay')
assert(getSmallestString(5, 73) == 'aaszz')
assert(getSmallestString(10, 23) == 'aaaaaaaaan')
assert(getSmallestString(4, 104) == 'zzzz')








