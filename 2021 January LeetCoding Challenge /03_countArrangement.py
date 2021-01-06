# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3591/


# Beautiful Arrangement


# Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed 
# by these n numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Given an integer n, return the number of the beautiful arrangements that you can construct.



# Example 1:
# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1, 2]:
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# The second beautiful arrangement is [2, 1]:
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

# Example 2:
# Input: n = 1
# Output: 1
 

# Constraints:
# 1 <= n <= 15


def countArrangement(n: int) -> int:
    def dfs(visited, n, pos):
        if pos == n:
            res[0] += 1
            return 
        for num in range(1, n + 1):
            divisible = (pos + 1) % num == 0 or num % (pos + 1) == 0
            if not visited[num - 1] and divisible:
                visited[num - 1] = True
                dfs(visited, n, pos + 1)
                visited[num - 1] = False
    visited = [False] * n
    res = [0]
    dfs(visited, n, 0)
    return res[0]

assert(countArrangement(1) == 1)
assert(countArrangement(3) == 3)
assert(countArrangement(10) == 700)
assert(countArrangement(15) == 24679)



