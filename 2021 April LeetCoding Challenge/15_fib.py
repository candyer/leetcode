# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3709/

# Fibonacci Number

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
# Constraints:
# 0 <= n <= 30

# def fib(n: int) -> int:
#     fib = [0, 1]
#     if n < 2:
#         return fib[n]
#     for i in range(n - 1):
#         fib.append(fib[-1] + fib[-2])
#     return fib[-1]


def fib(n: int) -> int:
    if n == 0:
        return 0
    fib1, fib2 = 0, 1
    for i in range(n - 1):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


assert(fib(0) == 0)
assert(fib(1) == 1)
assert(fib(2) == 1)
assert(fib(3) == 2)
assert(fib(4) == 3)
assert(fib(5) == 5)
assert(fib(7) == 13)






